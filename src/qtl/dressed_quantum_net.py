"""
Quantum Transfer Learning (QTL) with Dressed Quantum Circuit Architecture.
Combines a pre-trained ResNet-18 feature extractor with a variational quantum
circuit embedded between classical linear pre- and post-processing layers.
Based on Mari et al., arXiv:1912.08278 (2019).
"""

from typing import Tuple, List, Optional
import torch
import torch.nn as nn
import torchvision
import pennylane as qml
from pennylane import numpy as pnp


def create_quantum_layers(n_qubits: int, q_depth: int, dev: qml.Device):
    """
    Define variational quantum circuit with Hadamard initialization,
    angle encoding, CNOT ring entanglement, and parameterized RY rotations.
    """
    def H_layer():
        for idx in range(n_qubits):
            qml.Hadamard(wires=idx)

    def RY_layer(w):
        for idx, element in enumerate(w):
            qml.RY(element, wires=idx)

    def entangling_layer():
        for i in range(0, n_qubits - 1, 2):
            qml.CNOT(wires=[i, i + 1])
        for i in range(1, n_qubits - 1, 2):
            qml.CNOT(wires=[i, i + 1])

    @qml.qnode(dev, interface="torch", diff_method="best")
    def quantum_circuit(q_input_features, q_weights_flat):
        q_weights = q_weights_flat.reshape(q_depth, n_qubits)

        # Initialize in unbiased superposition |+>^n
        H_layer()

        # Embed classical features into quantum rotation angles
        RY_layer(q_input_features)

        # Variational trainable blocks
        for k in range(q_depth):
            entangling_layer()
            RY_layer(q_weights[k])

        # Expectation values of Pauli-Z on each qubit
        return [qml.expval(qml.PauliZ(position)) for position in range(n_qubits)]

    return quantum_circuit


class DressedQuantumNet(nn.Module):
    """
    'Dressed' Quantum Network Module.
    Pre-processing linear layer -> Variational Quantum Circuit -> Post-processing linear layer.
    """

    def __init__(
        self,
        in_features: int = 512,
        out_features: int = 2,
        n_qubits: int = 4,
        q_depth: int = 6,
        q_delta: float = 0.01,
        device_name: str = "default.qubit",
    ):
        super().__init__()
        self.n_qubits = n_qubits
        self.q_depth = q_depth

        self.dev = qml.device(device_name, wires=n_qubits)
        self.q_circuit = create_quantum_layers(n_qubits, q_depth, self.dev)

        # Classical pre-processing: 512 -> n_qubits
        self.pre_net = nn.Linear(in_features, n_qubits)

        # Variational quantum parameters
        self.q_params = nn.Parameter(q_delta * torch.randn(q_depth * n_qubits))

        # Classical post-processing: n_qubits -> num_classes
        self.post_net = nn.Linear(n_qubits, out_features)

    def forward(self, input_features: torch.Tensor) -> torch.Tensor:
        """
        Forward propagation through dressed quantum pipeline.
        Args:
            input_features: Batch of feature vectors of shape (B, in_features).
        Returns:
            torch.Tensor: Classification logits of shape (B, out_features).
        """
        pre_out = self.pre_net(input_features)
        q_in = torch.tanh(pre_out) * (torch.pi / 2.0)

        # Evaluate quantum circuit for each element in batch
        batch_q_out = []
        for elem in q_in:
            q_out_elem = torch.stack(self.q_circuit(elem, self.q_params)).float()
            batch_q_out.append(q_out_elem)

        q_out = torch.stack(batch_q_out)
        return self.post_net(q_out)


def create_hybrid_resnet(
    num_classes: int = 2,
    n_qubits: int = 4,
    q_depth: int = 6,
    pretrained: bool = True,
    freeze_backbone: bool = True,
    device: Optional[torch.device] = None,
) -> nn.Module:
    """
    Construct Hybrid ResNet-18 model with DressedQuantumNet classification head.
    """
    weights = torchvision.models.ResNet18_Weights.IMAGENET1K_V1 if pretrained else None
    model = torchvision.models.resnet18(weights=weights)

    if freeze_backbone:
        for param in model.parameters():
            param.requires_grad = False

    # Replace classical FC head with dressed quantum circuit
    model.fc = DressedQuantumNet(
        in_features=512,
        out_features=num_classes,
        n_qubits=n_qubits,
        q_depth=q_depth,
    )

    if device is not None:
        model = model.to(device)

    return model
