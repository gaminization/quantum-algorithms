# 06. Quantum Fourier Transform (QFT): Theory, Circuit Synthesis, and Applications

A complete mathematical and implementation guide to the Quantum Fourier Transform (QFT) using controlled phase-shift gates in Qiskit and PennyLane.

---

## 1. Classical Fourier Transform vs. Quantum Fourier Transform

### 1.1 The Classical Discrete Fourier Transform (DFT)
In classical signal processing, the Discrete Fourier Transform maps a sequence of $N$ complex numbers $x_0, x_1, \dots, x_{N-1}$ from the time domain to the frequency domain:

$$y_k = \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j e^{2\pi i j k / N}$$

It decomposes signals into their constituent sinusoidal frequencies with algorithmic complexity $O(N \log N)$ using the Fast Fourier Transform (FFT).

---

### 1.2 The Quantum Fourier Transform (QFT)
The Quantum Fourier Transform performs the exact same mathematical transformation directly on the **probability amplitudes** of an $n$-qubit quantum state ($N = 2^n$):

$$|\psi\rangle = \sum_{x=0}^{N-1} a_x |x\rangle \quad \xrightarrow{\text{QFT}} \quad |\psi'\rangle = \sum_{y=0}^{N-1} \tilde{a}_y |y\rangle$$

Acting on an individual computational basis state $|x\rangle$:

$$\boxed{\text{QFT}|x\rangle = \frac{1}{\sqrt{N}} \sum_{y=0}^{N-1} e^{2\pi i x y / N} |y\rangle}$$

> **Key Insight**: While classical FFT requires $O(N \log N) = O(n 2^n)$ operations on a vector of size $2^n$, the Quantum Fourier Transform executes in **$O(n^2)$ quantum gates**! This is an **exponential speedup** in the number of operations required to transform amplitudes.

---

## 2. Mathematical Building Blocks: Phase and Controlled Phase Gates

### 2.1 The Concept of Relative Quantum Phase
Consider two states:
$$|\psi_+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \qquad |\psi_-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}$$
Both yield equal $50\%$ measurement probabilities in the computational basis. However, their relative phase differs by $\pi$. More generally:
$$|\psi(\phi)\rangle = \frac{|0\rangle + e^{i\phi}|1\rangle}{\sqrt{2}}$$
This relative phase controls constructive and destructive interference when subsequent gates are applied.

---

### 2.2 The Phase-Shift Gate $P(\theta)$
The single-qubit phase gate leaves $|0\rangle$ invariant and imparts a phase shift $e^{i\theta}$ to $|1\rangle$:

$$P(\theta) = \begin{bmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{bmatrix} \implies P(\theta)|0\rangle = |0\rangle, \quad P(\theta)|1\rangle = e^{i\theta}|1\rangle$$

- $\theta = \frac{\pi}{2}$: $S$ gate ($P(\pi/2) = \begin{bmatrix} 1 & 0 \\ 0 & i \end{bmatrix}$).
- $\theta = \pi$: Pauli-$Z$ gate ($P(\pi) = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$).
- $\theta = \frac{\pi}{4}$: $T$ gate.

---

### 2.3 The Controlled Phase-Shift Gate $CP(\theta)$
The $CP(\theta)$ gate applies the phase shift $e^{i\theta}$ **if and only if both qubits are in state $|1\rangle$**:

$$CP(\theta) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & e^{i\theta} \end{bmatrix}$$

Action on computational basis states:
$$CP(\theta)|00\rangle = |00\rangle, \quad CP(\theta)|01\rangle = |01\rangle, \quad CP(\theta)|10\rangle = |10\rangle, \quad CP(\theta)|11\rangle = e^{i\theta}|11\rangle$$

```
Control: ───■───
            │
Target:  ───P(θ)
```

---

## 3. Two-Qubit QFT Circuit Derivation

For $n=2$ qubits ($N=4$):

$$\text{QFT}|x\rangle = \frac{1}{2} \sum_{y=0}^3 e^{2\pi i x y / 4} |y\rangle$$

### Circuit Sequence:
1. **Hadamard on Qubit 0**:
   $$|x_1 x_0\rangle \xrightarrow{H_0} \frac{|0\rangle + (-1)^{x_0}|1\rangle}{\sqrt{2}} \otimes |x_1\rangle$$
2. **Controlled Phase Shift $CP_{1, 0}(\pi/2)$**:
   Adds phase $e^{i\pi/2} = i$ if both $x_0=1$ and $x_1=1$.
3. **Hadamard on Qubit 1**:
   Converts the accumulated phase relationships into interference amplitudes.
4. **SWAP Gate**:
   Reverses output wire ordering to match the standard binary convention.

$$\boxed{H_0 \;\longrightarrow\; CP_{1, 0}\left(\frac{\pi}{2}\right) \;\longrightarrow\; H_1 \;\longrightarrow\; \text{SWAP}(0, 1)}$$

---

## 4. General $n$-Qubit QFT Synthesis

For an arbitrary $n$-qubit register, the controlled phase angles scale with qubit separation distance $k = \text{control} - \text{target}$:

$$\boxed{\theta_k = \frac{2\pi}{2^{k+1}} = \frac{\pi}{2^{k-1}}}$$

The sequence of phase angles is:
$$\frac{\pi}{2}, \quad \frac{\pi}{4}, \quad \frac{\pi}{8}, \quad \dots, \quad \frac{\pi}{2^{n-1}}$$

```
q_0: ──H──CP(π/2)──CP(π/4)──CP(π/8)─────────────────────────────X──
            │        │        │                                 │
q_1: ───────■────────┼────────┼─────H──CP(π/2)──CP(π/4)─────────┼──
                     │        │          │        │             │
q_2: ────────────────■────────┼──────────■────────┼─────H───────┼──
                              │                   │             │
q_3: ─────────────────────────■───────────────────■─────────────X──
```

Total number of gates required:
$$N_{\text{gates}} = \sum_{j=1}^n j = \frac{n(n+1)}{2} + \left\lfloor\frac{n}{2}\right\rfloor (\text{SWAPs}) \in O(n^2)$$

---

## 5. Implementations in Qiskit and PennyLane

### 5.1 Reusable $n$-Qubit QFT in Qiskit
```python
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def build_qft_circuit(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n, name=f"QFT_{n}")
    for target in range(n):
        qc.h(target)
        for control in range(target + 1, n):
            k = control - target
            angle = 2 * np.pi / (2 ** (k + 1))
            qc.cp(angle, control, target)
    
    # Reverse qubit order
    for i in range(n // 2):
        qc.swap(i, n - i - 1)
    return qc

# Test on 3 qubits
qc_qft3 = build_qft_circuit(3)
print(qc_qft3.draw())
```

### 5.2 Built-in QFT and Inverse QFT in PennyLane
```python
import pennylane as qml

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def forward_qft_circuit():
    qml.PauliX(wires=0)            # Prepare |01>
    qml.QFT(wires=[0, 1])          # Forward QFT
    return qml.state()

@qml.qnode(dev)
def inverse_qft_circuit():
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.adjoint(qml.QFT)(wires=[0, 1]) # Inverse QFT (QFT dagger)
    return qml.state()

print("Forward QFT state:", forward_qft_circuit())
print("Inverse QFT recovered state:", inverse_qft_circuit()) # Recovers |00>
```

---

## 6. The Inverse QFT ($\text{QFT}^\dagger$)

The inverse Quantum Fourier Transform reconstructs the time/computational basis representation from the frequency/phase representation:

$$\text{QFT}^\dagger = \left(\text{QFT}\right)^\dagger = \text{QFT}^{-1}$$

Circuit construction:
1. Reverse the order of all gates.
2. Replace all phase angles $\theta$ with negative angles $-\theta$ ($CP(-\theta)$).
3. Invert SWAP gates.

---

## 7. Major Applications in Quantum Computing

1. **Shor's Factoring Algorithm**: Extracts the order $r$ of modular exponentiation $a^x \pmod N$ using inverse QFT.
2. **Quantum Phase Estimation (QPE)**: Estimates the eigenvalue phase $\theta$ in $U|\psi\rangle = e^{2\pi i \theta}|\psi\rangle$.
3. **Quantum Chemistry & Hamiltonian Simulation**: Transforms between real-space atomic coordinates and momentum-space representations.
4. **Discrete Logarithms & Cryptanalysis**: Exponential speedup over classical RSA and elliptic-curve cryptography.
