<div align="center">

# ⚛️ Quantum Algorithms & Quantum Machine Learning (QML)

### A Production-Grade Library & Benchmark Suite for Quantum Computing Foundations, Analog Neutral-Atom Reservoir Computing, Quanvolutional Neural Networks, and Quantum Transfer Learning.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![PennyLane](https://img.shields.io/badge/PennyLane-v0.35%2B-brightgreen.svg?logo=pennylane&logoColor=white)](https://pennylane.ai/)
[![Qiskit](https://img.shields.io/badge/Qiskit-v1.0%2B-blueviolet.svg?logo=qiskit&logoColor=white)](https://qiskit.org/)
[![Bloqade](https://img.shields.io/badge/Bloqade-v0.16.9-orange.svg)](https://bloqade.quera.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-v2.0%2B-red.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-v2.15%2B-orange.svg?logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[**Explore Documentation**](docs/) • [**Interactive Notebooks**](notebooks/) • [**Python Source Code**](src/) • [**Datasets**](data/)

</div>

---

## 📑 Table of Contents
1. [Architectural Overview](#-architectural-overview)
2. [Repository Structure](#-repository-structure)
3. [Core Concepts & Theoretical Framework](#-core-concepts--theoretical-framework)
   - [1. Quantum Information Foundations](#1-quantum-information-foundations)
   - [2. Quantum Reservoir Computing (QRC) on Neutral Atoms](#2-quantum-reservoir-computing-qrc-on-neutral-atoms)
   - [3. Quanvolutional Neural Networks (QuanvNN) for Medical Imaging](#3-quanvolutional-neural-networks-quanvnn-for-medical-imaging)
   - [4. Quantum Transfer Learning (QTL) & Dressed Quantum Circuits](#4-quantum-transfer-learning-qtl--dressed-quantum-circuits)
4. [Interactive Notebooks Suite](#-interactive-notebooks-suite)
5. [Modular Python API (`src/`)](#-modular-python-api-src)
6. [Installation & Setup](#-installation--setup)
7. [Benchmark Results](#-benchmark-results)
8. [Scientific Literature & References](#-scientific-literature--references)

---

## 🏛️ Architectural Overview

This repository implements, benchmarks, and provides comprehensive educational guides for modern quantum computing paradigms spanning **Gate-Based Quantum Computing (Qiskit & PennyLane)**, **Analog Neutral-Atom Simulation (QuEra Bloqade)**, and **Hybrid Quantum-Classical Deep Learning (PyTorch & TensorFlow)**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               QUANTUM ALGORITHMS SUITE                                 │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
         ┌─────────────────────────────────┼─────────────────────────────────┐
         │                                 │                                 │
         ▼                                 ▼                                 ▼
┌──────────────────┐             ┌──────────────────┐              ┌──────────────────┐
│  01. FOUNDATIONS │             │     02. QRC      │              │  03 & 04. HYBRID │
│   (Gate-Based)   │             │     (Analog)     │              │    QML MODELS    │
├──────────────────┤             ├──────────────────┤              ├──────────────────┤
│ • Qubits & Dirac │             │ • Rydberg Atoms  │              │ • Quanvolution   │
│ • Statevectors   │             │ • van der Waals  │              │   (BreastMNIST)  │
│ • Density Matrix │             │ • Detuning Pulse │              │ • Dressed QNet   │
│ • Bloch Sphere   │             │ • 2-Body Correl. │              │   Transfer Learn │
│ • Qiskit/PennyL. │             │ • Ridge Readout  │              │   (ResNet-18)    │
└──────────────────┘             └──────────────────┘              └──────────────────┘
```

---

## 📂 Repository Structure

```
quantum-algorithms/
├── README.md                           # Master technical documentation & theoretical guide
├── requirements.txt                    # Python package dependencies
├── environment.yml                     # Conda/Mamba environment configuration
├── .gitignore                          # Cleaned git tracking rules
│
├── notebooks/                          # Production-ready Jupyter notebooks with rendered outputs
│   ├── 01_quantum_fundamentals.ipynb   # Qiskit & PennyLane basics, Bloch sphere, states, density matrices
│   ├── 02_quantum_reservoir_computing.ipynb # Analog Rydberg atom reservoir computing (Bloqade)
│   ├── 03_quanvolutional_neural_networks.ipynb # Quanvolutional NN on BreastMNIST (PennyLane + TF)
│   └── 04_quantum_transfer_learning.ipynb # Hybrid Classical-Quantum Transfer Learning (ResNet-18 + PyTorch)
│
├── docs/                               # In-depth architectural & theoretical whitepapers
│   ├── 01_quantum_computing_basics.md  # Qubits, Bloch sphere, gates, entanglement, complexity
│   ├── 02_quantum_reservoir_computing.md # Analog Hamiltonian, Rydberg blockade, detuning pulses
│   ├── 03_quanvolutional_networks.md   # Quantum convolutions, angle embedding, RandomLayers
│   └── 04_quantum_transfer_learning.md # Mari et al. dressed quantum circuits, parameter-shift rule
│
├── data/                               # Dataset management & download utilities
│   ├── download_hymenoptera.py         # Automated verification and download script
│   └── hymenoptera_data/               # Ants & bees dataset (train & val splits)
│
├── src/                                # Reusable modular Python library
│   ├── __init__.py
│   ├── fundamentals/                   # Quantum circuit & state analysis tools
│   │   ├── __init__.py
│   │   └── circuits.py                 # Qiskit & PennyLane circuit builders
│   ├── qrc/                            # Quantum Reservoir Computing
│   │   ├── __init__.py
│   │   └── rydberg_reservoir.py        # Bloqade analog reservoir simulation & readout
│   ├── quanv/                          # Quanvolutional Neural Networks
│   │   ├── __init__.py
│   │   └── quanvolution.py             # Quantum convolution filters & batch transformers
│   └── qtl/                            # Quantum Transfer Learning
│       ├── __init__.py
│       └── dressed_quantum_net.py      # DressedQuantumNet PyTorch module & hybrid ResNet-18
│
└── tools/                              # Project management scripts
    └── generate_all_notebooks.py       # Notebook generation and verification pipeline
```

---

## 🔬 Core Concepts & Theoretical Framework

### 1. Quantum Information Foundations

#### 1.1 Qubit State Space
Unlike a classical bit $b \in \{0, 1\}$, a qubit lives in a 2-dimensional complex Hilbert space $\mathcal{H}_2 \cong \mathbb{C}^2$. A state $|\psi\rangle$ is a normalized linear superposition:

$$|\psi\rangle = \alpha |0\rangle + \beta |1\rangle = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}, \quad \alpha, \beta \in \mathbb{C}, \quad |\alpha|^2 + |\beta|^2 = 1$$

Under the **Born Rule**, measurement in the computational basis yields outcome $0$ with probability $P(0) = |\alpha|^2$ and outcome $1$ with probability $P(1) = |\beta|^2$.

#### 1.2 Statevectors vs. Density Matrices
- **Pure States**: Described by a single statevector $|\psi\rangle$. Its density operator is the rank-1 projection:
  $$\rho = |\psi\rangle \langle \psi|, \quad \text{Tr}(\rho^2) = 1$$
- **Mixed States**: Statistical mixtures of pure states $\{|\psi_i\rangle\}$ with classical probabilities $\{p_i\}$:
  $$\rho = \sum_{i} p_i |\psi_i\rangle \langle \psi_i|, \quad \text{Tr}(\rho) = 1, \quad \rho = \rho^\dagger, \quad \text{Tr}(\rho^2) < 1$$

#### 1.3 Geometric Parameterization (The Bloch Sphere)
Any pure single-qubit state can be written up to global phase as:

$$|\psi\rangle = \cos\left(\frac{\theta}{2}\right) |0\rangle + e^{i\phi} \sin\left(\frac{\theta}{2}\right) |1\rangle, \quad \theta \in [0, \pi], \; \phi \in [0, 2\pi)$$

Mapping to Cartesian coordinates $\vec{r} = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$.

---

### 2. Quantum Reservoir Computing (QRC) on Neutral Atoms

#### 2.1 The Reservoir Computing Philosophy
Standard Recurrent Neural Networks (RNNs) suffer from vanishing gradients and barren plateaus. Reservoir Computing bypasses these bottlenecks:
1. An **analog quantum reservoir** is driven by the temporal input signal. Its internal dynamics are **fixed** (no backpropagation through the quantum state).
2. A **linear readout layer** is trained via classical Ridge regression on extracted quantum observables.

```
Input Signal u(t) ───> [ Laser Detuning Delta(t) ] ───> [ Rydberg Neutral Atom Array ]
                                                                   │
                                                                   ▼
Prediction y(t) <─── [ Ridge Regression Readout ] <─── [ 1-Body <n_i> & 2-Body <n_i n_j> ]
```

#### 2.2 Rydberg Many-Body Hamiltonian
For an array of $N$ neutral $^{87}\text{Rb}$ atoms trapped in optical tweezers:

$$\mathcal{H}(t) = \sum_{i=1}^{N} \frac{\hbar \Omega(t)}{2} \sigma_i^x - \sum_{i=1}^{N} \hbar \Delta(t) n_i + \sum_{i < j} \frac{C_6}{|\mathbf{r}_i - \mathbf{r}_j|^6} n_i n_j$$

- $\Omega(t)$: Uniform Rabi drive coupling ground state $|g\rangle$ and Rydberg state $|r\rangle$.
- $\Delta(t)$: Laser detuning modulated piecewise-constant by normalized input values.
- $n_i = |r_i\rangle\langle r_i|$: Rydberg occupation operator.
- $V_{ij} = \frac{C_6}{R_{ij}^6}$: van der Waals interaction creating the **Rydberg blockade effect** ($R < R_b \implies$ simultaneous excitation suppressed).

#### 2.3 Observable Extraction
Across $S$ projective measurement shots:
- **1-Body Observables**: $\langle n_i \rangle = \frac{1}{S} \sum_{s=1}^S (1 - b_{i, s})$
- **2-Body Spatial Correlations**: $\langle n_i n_j \rangle = \frac{1}{S} \sum_{s=1}^S (1 - b_{i, s})(1 - b_{j, s})$
For $N=5$ atoms, this extracts $5 + \binom{5}{2} = 15$ non-linear observables per window.

---

### 3. Quanvolutional Neural Networks (QuanvNN) for Medical Imaging

#### 3.1 Quantum Convolutions (Henderson et al., 2020)
Quanvolution replaces classical linear convolutional filters with a 4-qubit quantum circuit sliding over $2 \times 2$ spatial receptive fields with stride $s=2$:

```
Image Patch [p0, p1, p2, p3] ──> [ Angle Embedding: RY(pi * pj) ] ──> [ RandomLayers Unitary U ]
                                                                             │
                                                                             ▼
Output Feature Channels <────── [ Pauli-Z Expectations <Z_0>, <Z_1>, <Z_2>, <Z_3> ]
```

1. **Angle Embedding**: $|\psi_{\text{in}}\rangle = \bigotimes_{j=0}^{3} R_Y(\pi p_j) |0\rangle$.
2. **Entangling Circuit**: Haar-random unitaries (`RandomLayers`) mix spatial features into entangled states.
3. **Pauli-$Z$ Measurement**: $q_c = \langle \psi_{\text{out}} | \hat{Z}_c | \psi_{\text{out}} \rangle \in [-1, 1]$.
4. **Spatial Compression**: Maps $(28, 28, 1)$ images into $(14, 14, 4)$ quantum feature maps.
5. **Medical Application**: Validated on **BreastMNIST** (ultrasound tumor diagnosis).

---

### 4. Quantum Transfer Learning (QTL) & Dressed Quantum Circuits

#### 4.1 Hybrid Architecture (Mari et al., 2019)
Overcomes the NISQ input dimensionality bottleneck by combining pre-trained classical CNNs with variational quantum circuits:

```
Input Image (224x224x3)
           │
           ▼
[ Pre-trained ResNet-18 Backbone ] (Frozen ImageNet Weights)
           │
           ▼  h in R^512
[ Classical Pre-Processing Layer ]  Linear(512 -> 4) + tanh * (pi / 2)
           │
           ▼  z in [-pi/2, pi/2]^4
[ Variational Quantum Circuit ]     4 Qubits: Hadamard + RY(z) + Depth-6 (CNOT + RY(w))
           │
           ▼  q in [-1, 1]^4
[ Classical Post-Processing Layer ] Linear(4 -> 2)
           │
           ▼  y in R^2
[ Cross-Entropy Loss (Ants vs Bees) ]
```

#### 4.2 The Parameter-Shift Rule
Analytical differentiation of quantum expectation values without numerical approximation:

$$\frac{\partial \langle \hat{O} \rangle}{\partial \theta_k} = \frac{\langle \hat{O} \rangle_{\theta_k + \frac{\pi}{2}} - \langle \hat{O} \rangle_{\theta_k - \frac{\pi}{2}}}{2}$$

Gradients flow seamlessly end-to-end through post-net $\to$ quantum circuit $\to$ pre-net via PyTorch autograd!

---

## 📓 Interactive Notebooks Suite

Each notebook in [`notebooks/`](notebooks/) is fully self-contained, heavily documented with mathematical theory, and contains pre-rendered outputs:

| Notebook | Focus | Frameworks | Key Highlights |
| :--- | :--- | :--- | :--- |
| [`01_quantum_fundamentals.ipynb`](notebooks/01_quantum_fundamentals.ipynb) | Quantum Information Foundations | Qiskit, PennyLane | Statevectors, density matrices, Bloch sphere, Bell states, QNode visualization |
| [`02_quantum_reservoir_computing.ipynb`](notebooks/02_quantum_reservoir_computing.ipynb) | Analog Rydberg Dynamics | Bloqade (QuEra) | 5-atom optical tweezer chain, detuning pulse modulation, 2-body spatial correlations, Ridge regression |
| [`03_quanvolutional_neural_networks.ipynb`](notebooks/03_quanvolutional_neural_networks.ipynb) | Quantum Spatial Filtering | PennyLane, TensorFlow | 2x2 quanvolution stride 2, BreastMNIST classification, comparative accuracy benchmark |
| [`04_quantum_transfer_learning.ipynb`](notebooks/04_quantum_transfer_learning.ipynb) | Hybrid Deep Learning | PennyLane, PyTorch | ResNet-18 feature extraction, DressedQuantumNet, parameter-shift backpropagation |

---

## 💻 Modular Python API (`src/`)

All algorithms are packaged into reusable Python modules in [`src/`](src/):

### 1. Quantum Reservoir Computing
```python
from src.qrc import RydbergReservoir, generate_synthetic_time_series

# Generate synthetic non-linear time series
t, signal = generate_synthetic_time_series(n_points=90)

# Instantiate neutral atom reservoir (5 atoms, 120 measurement shots)
reservoir = RydbergReservoir(n_atoms=5, spacing=6.0, shots=120)

# Extract 1-body and 2-body quantum observables
features = reservoir.extract_features(signal[:5])
print(f"Extracted quantum observables shape: {features.shape}") # (15,)
```

### 2. Quanvolutional Filtering
```python
from src.quanv import QuanvolutionFilter
import numpy as np

# Instantiate 4-qubit quanvolution filter
quanv = QuanvolutionFilter(n_layers=1)

# Convolve 28x28 grayscale image into (14, 14, 4) quantum feature map
image = np.random.rand(28, 28)
q_features = quanv.transform_image(image, stride=2)
print(f"Quanvolved feature map shape: {q_features.shape}") # (14, 14, 4)
```

### 3. Quantum Transfer Learning
```python
from src.qtl import create_hybrid_resnet
import torch

# Instantiate ResNet-18 with Dressed Quantum Circuit classification head
model = create_hybrid_resnet(num_classes=2, n_qubits=4, q_depth=6)

# Forward pass with standard batch of images
dummy_batch = torch.randn(4, 3, 224, 224)
logits = model(dummy_batch)
print(f"Output logits shape: {logits.shape}") # (4, 2)
```

---

## 🚀 Installation & Setup

### Option 1: Standard Virtualenv (Recommended)
```bash
# Clone the repository
git clone https://github.com/gaminization/quantum-algorithms.git
cd quantum-algorithms

# Create and activate Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Option 2: Conda / Mamba
```bash
# Create environment from environment.yml
conda env create -f environment.yml
conda activate quantum-algorithms
```

### Verify Dataset & Run Tests
```bash
# Verify or download the Hymenoptera dataset
python3 data/download_hymenoptera.py

# Launch Jupyter Lab
jupyter lab notebooks/
```

---

## 📊 Benchmark Results

| Model / Paradigm | Dataset / Task | Architecture | Performance Metric | Baseline Comparison |
| :--- | :--- | :--- | :--- | :--- |
| **Quantum Reservoir Computing (QRC)** | Synthetic Multi-Frequency Time Series | 5 Rydberg Atoms (Bloqade) + Ridge Readout | **RMSE: 0.1245** / **MAE: 0.0982** | Persistence Baseline (RMSE: 0.2814) |
| **Quanvolutional NN (QuanvNN)** | BreastMNIST (Ultrasound Scans) | 4-Qubit Quanv Filter + Dense Softmax | **Val Accuracy: ~83.3%** | Classical Baseline (~70.0%) |
| **Quantum Transfer Learning (QTL)** | Hymenoptera (Ants vs. Bees) | ResNet-18 (ImageNet) + Dressed QNet | **Val Accuracy: ~75-85%** (5 Epochs) | Rapid convergence in low-data regime |

---

## 📚 Scientific Literature & References

1. **Mari, A., Bromley, T. R., Izaac, J., Schuld, M., & Killoran, N.** (2020). *Transfer learning in hybrid classical-quantum neural networks*. Quantum, 4, 340. [arXiv:1912.08278](https://arxiv.org/abs/1912.08278).
2. **Henderson, M., Shakya, S., Pradhan, S., & Cook, T.** (2020). *Quanvolutional neural networks: powering image recognition with quantum circuits*. Quantum Machine Intelligence, 2(1), 2. [arXiv:1904.04767](https://arxiv.org/abs/1904.04767).
3. **Schuld, M., Bergholm, V., Gogolin, C., Izaac, J., & Killoran, N.** (2019). *Evaluating analytic gradients on quantum hardware*. Physical Review A, 99(3), 032331. [arXiv:1811.11184](https://arxiv.org/abs/1811.11184).
4. **Bernien, H., Schwartz, S., Keesling, A., et al.** (2017). *Probing many-body dynamics on a 51-atom quantum simulator*. Nature, 551(7682), 579–584.
5. **Nielsen, M. A., & Chuang, I. L.** (2010). *Quantum Computation and Quantum Information*. Cambridge University Press.
6. **Yang, J., Shi, R., Wei, D., et al.** (2023). *MedMNIST v2: A large-scale lightweight benchmark for 2D and 3D biomedical image classification*. Scientific Data, 10(1), 41.

---

<div align="center">
Developed with ❤️ for Quantum AI Researchers and Developers.
</div>