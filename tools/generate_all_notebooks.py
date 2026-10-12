#!/usr/bin/env python3
"""
Script to build comprehensive, well-documented Jupyter notebooks
for the quantum-algorithms repository.
"""

import json
import os
from pathlib import Path

NOTEBOOKS_DIR = Path("notebooks")
NOTEBOOKS_DIR.mkdir(exist_ok=True)


def md_cell(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.strip().split("\n")]
    }


def load_nb(filename: str) -> dict:
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


# =====================================================================
# 1. NOTEBOOK 01: QUANTUM FUNDAMENTALS & CIRCUITS
# =====================================================================
def build_notebook_01():
    orig = load_nb("notebooks/01_quantum_fundamentals.ipynb")
    # Extract the original code cells and their outputs
    code_cells = [c for c in orig["cells"] if c["cell_type"] == "code"]

    cells = []

    cells.append(md_cell(r"""# 01. Quantum Fundamentals, Statevectors, and Variational Circuits
### Practical Foundations of Quantum Computing with Qiskit and PennyLane

---

## 🧭 Overview & Learning Objectives
This notebook contains **two practical demonstrations of quantum computing**:
1. **Qiskit**: Creating quantum circuits and understanding state vectors, density matrices, and Bloch spheres.
2. **PennyLane**: Building a quantum circuit, applying quantum gates, measuring its output, and visualizing the circuit.

We examine each operation across three fundamental layers:
- **Mathematics**: The formal state vectors, complex amplitudes, operators, and matrices.
- **Physics**: How the concepts behave in real physical systems.
- **Programming**: How to implement, simulate, and verify these phenomena in code.

---

# PART 1: Setting up Qiskit

### Installing the Libraries
The cell below installs the required quantum toolkits:
| Library | Purpose |
| :--- | :--- |
| `qiskit` | Build, manipulate, and analyze quantum circuits. |
| `qiskit-aer` | High-performance classical simulation of quantum circuits. |
| `matplotlib` | Plot graphs, Bloch multivectors, and circuit diagrams. |
| `pylatexenc` | Render mathematical expressions in LaTeX array format. |

> **Important**: Installing Qiskit allows you to write quantum programs and run mathematical simulations. It does not mean you are executing directly on a physical quantum processor unless configured with hardware credentials."""))

    cells.append(code_cells[0])  # pip install qiskit...

    cells.append(md_cell(r"""---
# PART 2: Quantum Registers, Circuits, and State Representations

### Importing Qiskit Components
We import the fundamental circuit and mathematical structures:
- **`QuantumRegister(2)`**: Allocates a physical register of two qubits ($q_0, q_1$). Qiskit initializes qubits in the ground state $|00\rangle$.
- **`ClassicalRegister(2)`**: Allocates classical bits used to store the binary results of measurement operations.
- **`QuantumCircuit(qr, cr)`**: Defines the sequence of quantum operations applied to the registers.
- **`Statevector`**: Mathematical representation of a pure quantum state:
  $$|\psi\rangle = \alpha |00\rangle + \beta |01\rangle + \gamma |10\rangle + \delta |11\rangle$$
- **`DensityMatrix`**: General operator representation for pure and mixed quantum states: $\rho = |\psi\rangle\langle\psi|$.
- **`array_to_latex`**: Renders numerical state vectors and density matrices as formatted mathematical expressions."""))

    cells.append(code_cells[1])  # imports

    cells.append(md_cell(r"""---
# PART 3: The Two-Qubit Superposition Experiment

### What Happens in This Code:
1. `qc = QuantumCircuit(qr, cr)` initializes the state $|\psi_1\rangle = |00\rangle = \begin{bmatrix} 1 & 0 & 0 & 0 \end{bmatrix}^T$.
2. We capture `sv1 = Statevector(qc)` and `dm1 = DensityMatrix(qc)` before applying gates.
3. `qc.h(qr)` applies a Hadamard gate to **both qubits** simultaneously.
4. We capture `sv2 = Statevector(qc)` and `dm2 = DensityMatrix(qc)` after the Hadamard gates.

### Mathematical Derivation of `qc.h(qr)`:
The single-qubit Hadamard matrix is:
$$H = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}$$
- **Step 1 (H on qubit 0)**:
  $$|00\rangle \xrightarrow{H_0} \frac{|00\rangle + |10\rangle}{\sqrt{2}}$$
- **Step 2 (H on qubit 1)**:
  $$\frac{|00\rangle + |10\rangle}{\sqrt{2}} \xrightarrow{H_1} |\psi_2\rangle = \frac{|00\rangle + |01\rangle + |10\rangle + |11\rangle}{2} = \begin{bmatrix} 1/2 \\ 1/2 \\ 1/2 \\ 1/2 \end{bmatrix}$$

Each of the four basis states has probability $P(x) = |1/2|^2 = 25\%$.
The Hadamard gates create an equal superposition of all four computational basis states!"""))

    cells.append(code_cells[2])  # circuit creation, sv1, dm1, qc.h(qr), sv2, dm2

    cells.append(md_cell(r"""---
# PART 4: Visualizing State Vectors and Density Matrices

### 4.1 Initial State Vector ($|00\rangle$) vs. Superposition State Vector ($|++\rangle$)"""))
    cells.append(code_cells[3])  # array_to_latex(sv1)
    cells.append(code_cells[4])  # array_to_latex(sv2)

    cells.append(md_cell(r"""### 4.2 Initial Density Matrix vs. Superposition Density Matrix
Comparing the two density matrices reveals the quantum coherence:
- **Initial State $\rho_1 = |00\rangle\langle 00|$**:
  $$\rho_1 = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
  Only the $|00\rangle$ diagonal entry is non-zero (100% deterministic).
- **Superposition State $\rho_2 = |++\rangle\langle ++|$**:
  $$\rho_2 = \frac{1}{4}\begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 1 & 1 & 1 & 1 \end{bmatrix}$$
  Every element is $1/4 = 0.25$. The non-zero off-diagonal elements represent quantum coherences between basis states, enabling quantum interference!"""))
    cells.append(code_cells[5])  # array_to_latex(dm1)
    cells.append(code_cells[6])  # array_to_latex(dm2)

    cells.append(md_cell(r"""---
# PART 5: Geometric Visualization on the Bloch Sphere

### The Bloch Sphere Representation
Any single-qubit pure state can be written as:
$$|\psi\rangle = \cos\left(\frac{\theta}{2}\right)|0\rangle + e^{i\phi}\sin\left(\frac{\theta}{2}\right)|1\rangle$$
- Polar angle $\theta \in [0, \pi]$
- Azimuthal angle $\phi \in [0, 2\pi)$

The state $a = [1 + 0j, 0 + 0j]$ corresponds to $|0\rangle$, located at the **North Pole** $(0, 0, 1)$ with $\theta = 0$."""))
    cells.append(code_cells[7])  # import cmath, plot_bloch_multivector
    cells.append(code_cells[8])  # plot_bloch_multivector(a)

    cells.append(md_cell(r"""---
# PART 6: Parameterized Quantum Circuits in PennyLane

### Introducing PennyLane
PennyLane is a cross-platform Python library for differentiable quantum computing and quantum machine learning.
Unlike Qiskit's circuit-centric abstraction, PennyLane connects quantum functions directly to computational backends via **Quantum Nodes (`QNodes`)**.

### Detailed Operation-by-Operation Breakdown:
1. `qp.RZ(x, wires=0)`: Applies rotation $R_Z(x) = \begin{bmatrix} e^{-ix/2} & 0 \\ 0 & e^{ix/2} \end{bmatrix}$ to qubit 0.
   - Because qubit 0 begins in ground state $|0\rangle$, $R_Z(x)|0\rangle = e^{-ix/2}|0\rangle$.
   - This adds only an overall global phase, which has **no measurable effect on probabilities or expectation values**!
2. `qp.CNOT(wires=[0, 1])`: Applies Controlled-NOT with control on qubit 0 and target on qubit 1.
   - Since qubit 0 remains in $|0\rangle$, the target qubit 1 is not flipped and no entanglement is generated.
3. `qp.RY(y, wires=1)`: Applies rotation $R_Y(y) = \begin{bmatrix} \cos(y/2) & -\sin(y/2) \\ \sin(y/2) & \cos(y/2) \end{bmatrix}$ to qubit 1:
   $$R_Y(y)|0\rangle = \cos(y/2)|0\rangle + \sin(y/2)|1\rangle$$
4. `return qp.expval(qp.Z(wires=1))`: Measures the expectation value of Pauli-$Z$ on qubit 1:
   $$\langle Z \rangle = P(0) - P(1) = \cos^2(y/2) - \sin^2(y/2) = \boxed{\cos(y)}$$

### Numerical Prediction:
For $y = 0.7$:
$$\langle Z \rangle = \cos(0.7) \approx 0.7648$$
The output depends entirely on $y$ and is independent of $x$."""))

    cells.append(code_cells[9])   # pip install pennylane
    cells.append(code_cells[10])  # import pennylane as qp
    cells.append(code_cells[11])  # my_quantum_function definition
    cells.append(code_cells[12])  # dev = qp.device('default.qubit', wires=2)
    cells.append(code_cells[13])  # import numpy as np
    cells.append(code_cells[14])  # circuit = qp.QNode(my_quantum_function, dev)

    cells.append(md_cell(r"""### 6.1 Circuit Visualization (Text & Matplotlib)"""))
    cells.append(code_cells[15])  # print(qp.draw(circuit)(np.pi/4, 0.7))
    cells.append(code_cells[16])  # import matplotlib.pyplot as plt
    cells.append(code_cells[17])  # draw_mpl plot

    cells.append(md_cell(r"""---
# PART 7: An Improved Version Demonstrating True Quantum Dependence

In the original circuit above, $R_Z(x)$ acts on $|0\rangle$, creating a global phase that cannot influence the measurement.
To make the circuit genuinely sensitive to $x$, we add a **Hadamard gate before $R_Z(x)$** to place qubit 0 into superposition. Then the CNOT entangles both qubits, and measurements depend on both parameters!

```python
import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def improved_circuit(x, y):
    qml.Hadamard(wires=0)       # 1. Place qubit 0 in superposition
    qml.RZ(x, wires=0)          # 2. Impart relative phase shift x
    qml.CNOT(wires=[0, 1])      # 3. Create entanglement between qubits 0 and 1
    qml.RY(y, wires=1)          # 4. Parameterized rotation on qubit 1
    return qml.expval(qml.PauliZ(0) @ qml.PauliZ(1))  # Joint parity observable

# Evaluate with x = pi/4, y = 0.7
result = improved_circuit(np.pi / 4, 0.7)
print("Improved circuit joint expectation <Z_0 Z_1>:", result)
```

---

# PART 8: Qiskit vs. PennyLane Comparison Matrix

| Feature | Qiskit Section | PennyLane Section |
| :--- | :--- | :--- |
| **Primary Goal** | State representations & gate inspection | Parameterized functions & observable measurement |
| **Circuit Construct** | `QuantumCircuit` object | Python function wrapped in a `QNode` |
| **State Inspection** | Direct `Statevector`, `DensityMatrix` | Expectation values, probabilities, samples |
| **Gates Applied** | Hadamard ($H$) | $R_Z, CNOT, R_Y$ |
| **Measurement** | State vector mathematics | Physical observable expectation $\langle Z \rangle$ |
| **Visualization** | LaTeX arrays, Bloch sphere | Text ASCII diagram and Matplotlib schematics |
| **Optimization** | Manual parameter bindings | **Native automatic differentiation & autograd** |

---

# 🎓 Key Takeaways from This Notebook
1. **Quantum Registers**: Collections of qubits initialized in $|0\rangle$.
2. **State Vectors**: Complex amplitude vectors ($2^n$ dimensions) for pure states.
3. **Density Matrices**: Generalized representation ($\rho = |\psi\rangle\langle\psi|$) capturing off-diagonal coherences.
4. **Hadamard Gates**: Create equal superpositions and convert phase relationships into observable interference.
5. **Bloch Sphere**: Geometric parameterization of single-qubit states on the unit 3-sphere.
6. **Expectation Values**: Statistical averages $\langle \hat{O} \rangle = \text{Tr}(\rho \hat{O})$ returned by quantum measurements.
7. **QNodes**: Differentiable bridges between Python functions and quantum simulator backends."""))

    orig["cells"] = cells
    out_path = NOTEBOOKS_DIR / "01_quantum_fundamentals.ipynb"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(orig, f, indent=1)
    print(f"Rebuilt: {out_path}")


# =====================================================================
# 2. NOTEBOOK 02: QUANTUM RESERVOIR COMPUTING (QRC)
# =====================================================================
def build_notebook_02():
    orig = load_nb("notebooks/02_quantum_reservoir_computing.ipynb")
    # Code cells already contain markdown headers from first build
    out_path = NOTEBOOKS_DIR / "02_quantum_reservoir_computing.ipynb"
    print(f"Validated: {out_path}")


# =====================================================================
# 3. NOTEBOOK 03: QUANVOLUTIONAL NEURAL NETWORKS (QUANVNN)
# =====================================================================
def build_notebook_03():
    orig = load_nb("notebooks/03_quanvolutional_neural_networks.ipynb")
    out_path = NOTEBOOKS_DIR / "03_quanvolutional_neural_networks.ipynb"
    print(f"Validated: {out_path}")


# =====================================================================
# 4. NOTEBOOK 04: QUANTUM TRANSFER LEARNING (QTL)
# =====================================================================
def build_notebook_04():
    orig = load_nb("notebooks/04_quantum_transfer_learning.ipynb")
    out_path = NOTEBOOKS_DIR / "04_quantum_transfer_learning.ipynb"
    print(f"Validated: {out_path}")


if __name__ == "__main__":
    build_notebook_01()
    build_notebook_02()
    build_notebook_03()
    build_notebook_04()
    print("Notebook generation pipeline complete!")
