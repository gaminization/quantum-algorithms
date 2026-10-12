"""
Circuit builders and quantum state utilities using Qiskit and PennyLane.
"""

from typing import Tuple, List
import numpy as np


def create_bell_state_circuit():
    """
    Construct a 2-qubit Bell state |Phi+> = (|00> + |11>) / sqrt(2) in Qiskit.
    Returns:
        QuantumCircuit: 2-qubit circuit with H on q0 and CNOT(0, 1).
    """
    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

    qr = QuantumRegister(2, "q")
    cr = ClassicalRegister(2, "c")
    qc = QuantumCircuit(qr, cr)
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    return qc


def compute_density_matrix(circuit):
    """
    Compute statevector and density matrix of a Qiskit circuit.
    """
    from qiskit.quantum_info import Statevector, DensityMatrix

    sv = Statevector(circuit)
    dm = DensityMatrix(circuit)
    return sv, dm


def bloch_coordinates_from_state(alpha: complex, beta: complex) -> Tuple[float, float, float]:
    """
    Map single-qubit amplitude coefficients alpha, beta to Cartesian Bloch sphere coordinates (x, y, z).
    |psi> = alpha |0> + beta |1>
    """
    norm = np.sqrt(np.abs(alpha) ** 2 + np.abs(beta) ** 2)
    a, b = alpha / norm, beta / norm

    # Density matrix elements
    # rho = [[ |a|^2, a * conj(b) ],
    #        [ conj(a) * b, |b|^2 ]]
    rho00 = np.abs(a) ** 2
    rho11 = np.abs(b) ** 2
    rho01 = a * np.conj(b)

    x = float(2 * np.real(rho01))
    y = float(2 * np.imag(rho01))
    z = float(rho00 - rho11)
    return x, y, z


def create_pennylane_demo_circuit(device_name: str = "default.qubit", wires: int = 2):
    """
    Create a parameterized PennyLane variational circuit demonstration.
    Applies RZ on wire 0, CNOT(0, 1), RY on wire 1, and returns expval(Z_1).
    """
    import pennylane as qml

    dev = qml.device(device_name, wires=wires)

    @qml.qnode(dev)
    def circuit(x: float, y: float):
        qml.RZ(x, wires=0)
        qml.CNOT(wires=[0, 1])
        qml.RY(y, wires=1)
        return qml.expval(qml.PauliZ(1))

    return circuit, dev
