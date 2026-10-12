# 04. Quantum Transfer Learning (QTL) with Dressed Quantum Circuits

A comprehensive theoretical, mathematical, and implementation guide to Quantum Transfer Learning (QTL), combining pre-trained classical deep neural networks with variational quantum circuits.

---

## 🎯 1. The Transfer Learning Problem: Dataset A vs. Dataset B

### 1.1 The Challenge of Small Datasets & Overfitting
Suppose you want to classify a specialized dataset (e.g., distinguishing Cars vs. Motorcycles, or Ants vs. Bees).
- **Dataset A**: A massive benchmark dataset (e.g., ImageNet-1K with $1.2$ million images across 1,000 classes).
- **Dataset B**: Your target dataset containing only $500$ labeled training images.

Training a deep neural network from scratch on Dataset B is prone to **severe overfitting**—the network memorizes training samples instead of learning generalizable visual representations.

### 1.2 Classical Transfer Learning Solution
1. **Train Backbone on Dataset A**: A Convolutional Neural Network (CNN) learns hierarchical visual primitives (edges, textures, shapes, object parts).
2. **Remove Original Classification Head**: Strip away the final 1,000-class fully connected layer, retaining the learned feature extractor:
   $$\mathbf{x} \in \mathbb{R}^{224 \times 224 \times 3} \quad \xrightarrow{\text{CNN Backbone}} \quad \mathbf{h} \in \mathbb{R}^{512}$$
3. **Train Lightweight Classifier on Dataset B**: Attach a new classifier trained on the compact 512-dimensional embedding using Dataset B.

---

## ⚡ 2. The Input Dimensionality Bottleneck in Quantum Computing

Why can't we feed raw images directly into a quantum circuit?
- A standard RGB image has:
  $$224 \times 224 \times 3 = 150,528 \text{ numerical pixel values}$$
- A 4-qubit register has a Hilbert space dimension of $2^4 = 16$.
- An 8-qubit register has dimension $2^8 = 256$.
- A 10-qubit register has dimension $2^{10} = 1,024$.

Directly encoding $150,528$ values into quantum states would require prohibitive circuit depth that exceeds the **coherence time ($T_2$)** of any existing NISQ hardware.

### The Quantum Transfer Learning (QTL) Solution
Pioneered by Andrea Mari et al. (2019) (*arXiv:1912.08278*), QTL delegates high-dimensional visual feature extraction to a pre-trained classical network and uses a compact **Dressed Quantum Circuit** as the decision head:

$$150,528 \text{ image pixels} \xrightarrow{\text{ResNet-18 (frozen)}} 512 \text{ features} \xrightarrow{\text{Pre-Net}} 4 \text{ quantum angles} \xrightarrow{\text{4-Qubit VQC}} \text{Predictions}$$

---

## 🏛️ 3. The Complete 7-Stage QTL Architecture

```
[ Image X (224x224x3) ]
           │
           ▼
[ Stage 1: Pre-Trained ResNet-18 Backbone ] (Frozen ImageNet Weights)
           │
           ▼  h in R^512
[ Stage 2: Classical Feature Reduction ]     Linear(512 -> 4)
           │
           ▼  u in R^4
[ Stage 3: Angle Scaling ]                   theta_i = pi * tanh(u_i) in (-pi, pi)
           │
           ▼
[ Stage 4: Quantum State Encoding ]          RY(theta_i) on Qubits 0..3
           │
           ▼
[ Stage 5: Trainable Variational Layers ]    Depth-6 CNOT Rings + Parameterized RY(w)
           │
           ▼
[ Stage 6: Quantum Observable Measurement ]  <Z_0>, <Z_1>, <Z_2>, <Z_3> in [-1, 1]
           │
           ▼  q in R^4
[ Stage 7: Classical Post-Processing ]       Linear(4 -> 2) -> Cross-Entropy Loss
```

---

### Mathematical Breakdown of Every Stage

#### Stage 1: Classical Feature Extractor
An ImageNet pre-trained ResNet-18 extracts feature vector $\mathbf{h} = f_{\text{ResNet}}(\mathbf{x}) \in \mathbb{R}^{512}$. Backbone weights are frozen ($\nabla_{\theta_{\text{CNN}}} \mathcal{L} = 0$).

#### Stage 2 & 3: Feature Reduction & Angle Scaling
A trainable linear layer reduces dimension from 512 to 4:
$$\mathbf{u} = \mathbf{W}_{\text{pre}} \mathbf{h} + \mathbf{b}_{\text{pre}} \in \mathbb{R}^4$$
We map each value into valid rotation angles via scaled hyperbolic tangent:
$$\theta_i = \pi \tanh(u_i) \in (-\pi, \pi), \quad i \in \{0, 1, 2, 3\}$$

#### Stage 4: Quantum Angle Encoding
The 4 qubits start in ground state $|0000\rangle$. Single-qubit $Y$-rotations prepare the state:
$$|\psi(\vec{\theta})\rangle = \left( \bigotimes_{i=0}^3 R_Y(\theta_i) \right) |0000\rangle$$
where $R_Y(\theta) = \begin{bmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{bmatrix}$.

#### Stage 5: Trainable Variational Circuit (Ansatz)
We apply $q_{\text{depth}} = 6$ variational blocks. Each block comprises:
1. **Entangling CNOT Ring Layers**:
   - Even pairs: $CNOT(0, 1), \; CNOT(2, 3)$
   - Odd pairs: $CNOT(1, 2)$
2. **Parameterized Single-Qubit Rotations**:
   $$\bigotimes_{i=0}^3 R_Y(w_{l, i})$$
Total trainable quantum weights: $N = q_{\text{depth}} \times n = 6 \times 4 = 24$ parameters.

#### Stage 6: Quantum Measurement
We measure expectation values of Pauli-$Z$ on each of the 4 qubits:
$$q_i = \langle \psi_{\text{out}} | \hat{Z}_i | \psi_{\text{out}} \rangle \in [-1, 1], \quad i \in \{0, 1, 2, 3\}$$

#### Stage 7: Classical Post-Processing & Loss
A final linear layer maps the 4 quantum expectation values to class logits $\mathbf{y} \in \mathbb{R}^2$:
$$\mathbf{y} = \mathbf{W}_{\text{post}} \mathbf{q} + \mathbf{b}_{\text{post}}$$
Class probabilities are computed via Softmax, trained with Cross-Entropy Loss:
$$\mathcal{L} = -\sum_{k} y_k \log P(y = k \mid \mathbf{x})$$

---

## 🔁 4. Hybrid Backpropagation & The Parameter-Shift Rule

The hybrid model is trained end-to-end. While classical layers use standard autograd chain rule, quantum gradients cannot be evaluated via standard symbolic backprop on physical hardware.
Instead, gradients are evaluated analytically using the **Parameter-Shift Rule**:

$$\boxed{\frac{\partial \langle \hat{O} \rangle}{\partial w_k} = \frac{1}{2} \left[ \langle \hat{O} \rangle_{w_k + \frac{\pi}{2}} - \langle \hat{O} \rangle_{w_k - \frac{\pi}{2}} \right]}$$

The classical pre-net gradients flow seamlessly through the quantum node via:
$$\frac{\partial \mathcal{L}}{\partial \mathbf{W}_{\text{pre}}} = \left( \frac{\partial \mathcal{L}}{\partial \mathbf{y}} \cdot \mathbf{W}_{\text{post}} \cdot \frac{\partial \mathbf{q}}{\partial \vec{\theta}} \odot \pi(1 - \tanh^2(\mathbf{u})) \right) \mathbf{h}^T$$

---

## ⏱️ 5. Coherence Time vs. Quantum Transfer Learning

| Dimension | Coherence Time ($T_1, T_2$) | Quantum Transfer Learning (QTL) |
| :--- | :--- | :--- |
| **Nature** | Hardware-level physical limitation | Machine-learning algorithmic strategy |
| **Core Concern** | How long physical quantum states survive noise before dephasing | How to train high-accuracy models when target data is scarce |
| **Equation** | $\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}$ | $\mathbf{x} \to \text{CNN}_{\text{frozen}}(\mathbf{x}) \to \text{VQC}(\vec{\theta}) \to \mathbf{y}$ |
| **Synergy** | Deep circuits fail because $t_{\text{circuit}} > T_2$ | **QTL enables shallow circuits ($t_{\text{circuit}} \ll T_2$)**, making quantum ML viable on NISQ hardware! |

---

## 💻 6. Complete Python Implementation (PennyLane + PyTorch)

### 6.1 Building the Hybrid Quantum Layer
```python
import pennylane as qml
import torch
import torch.nn as nn
from torchvision.models import resnet18, ResNet18_Weights

n_qubits = 4
q_depth = 6
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev, interface="torch", diff_method="best")
def quantum_net(q_input_features, q_weights_flat):
    q_weights = q_weights_flat.reshape(q_depth, n_qubits)
    
    # Hadamard initialization
    for i in range(n_qubits):
        qml.Hadamard(wires=i)
        
    # Angle embedding
    for i in range(n_qubits):
        qml.RY(q_input_features[i], wires=i)
        
    # Variational layers
    for k in range(q_depth):
        for i in range(0, n_qubits - 1, 2):
            qml.CNOT(wires=[i, i + 1])
        for i in range(1, n_qubits - 1, 2):
            qml.CNOT(wires=[i, i + 1])
        for i in range(n_qubits):
            qml.RY(q_weights[k, i], wires=i)
            
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]
```

### 6.2 The Dressed Quantum Network Module
```python
class DressedQuantumNet(nn.Module):
    def __init__(self, in_features=512, out_features=2):
        super().__init__()
        self.pre_net = nn.Linear(in_features, n_qubits)
        self.q_params = nn.Parameter(0.01 * torch.randn(q_depth * n_qubits))
        self.post_net = nn.Linear(n_qubits, out_features)

    def forward(self, x):
        pre_out = self.pre_net(x)
        q_in = torch.tanh(pre_out) * (torch.pi / 2.0)
        
        batch_out = []
        for elem in q_in:
            q_out = torch.stack(quantum_net(elem, self.q_params)).float()
            batch_out.append(q_out)
            
        return self.post_net(torch.stack(batch_out))

# Assemble Hybrid Model
weights = ResNet18_Weights.DEFAULT
model_hybrid = resnet18(weights=weights)

# Freeze classical backbone
for param in model_hybrid.parameters():
    param.requires_grad = False

# Replace final FC layer with Dressed Quantum Circuit
model_hybrid.fc = DressedQuantumNet(in_features=512, out_features=2)
```

---

## 📊 7. Benchmark Results on Hymenoptera (Ants vs. Bees)

- **Dataset**: Ants vs. Bees (397 images, train/val split).
- **Optimizer**: Adam ($\text{lr} = 0.0004$) applied to `model_hybrid.fc.parameters()`.
- **Validation Accuracy**: Achieves **$> 75-85\%$ within 5 epochs**, verifying rapid convergence in the limited-data regime without overfitting.
