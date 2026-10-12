<div align="center">

# ⚛️ Quantum Algorithms & Quantum Machine Learning (QML)

### A Unified Master Reference, Benchmark Suite, and Production-Grade Library Connecting Quantum Mathematics, Physical Hardware, and Differentiable Quantum Programming.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![PennyLane](https://img.shields.io/badge/PennyLane-v0.35%2B-brightgreen.svg?logo=pennylane&logoColor=white)](https://pennylane.ai/)
[![Qiskit](https://img.shields.io/badge/Qiskit-v1.0%2B-blueviolet.svg?logo=qiskit&logoColor=white)](https://qiskit.org/)
[![Bloqade](https://img.shields.io/badge/Bloqade-v0.16.9-orange.svg)](https://bloqade.quera.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-v2.0%2B-red.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-v2.15%2B-orange.svg?logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[**Architectural Guides**](docs/) • [**Interactive Notebooks**](notebooks/) • [**Python Library (`src/`)**](src/) • [**Datasets**](data/)

</div>

---

## 📑 Master Table of Contents
1. [The Three-Perspective Paradigm](#-the-three-perspective-paradigm)
2. [Complete Theoretical Documentation Matrix](#-complete-theoretical-documentation-matrix)
3. [Repository Directory Architecture](#-repository-directory-architecture)
4. [Fundamental Quantum Concepts: 12 Core Topics](#-fundamental-quantum-concepts-12-core-topics)
5. [Physical Quantum Hardware Comparison](#-physical-quantum-hardware-comparison)
6. [Quantum Software Ecosystem: Bloqade vs. PennyLane vs. Qiskit](#-quantum-software-ecosystem-bloqade-vs-pennylane-vs-qiskit)
7. [Global & Indian Quantum Technology Ecosystems](#-global--indian-quantum-technology-ecosystems)
8. [Quantum Fourier Transform (QFT) via Controlled Phase Shifts](#-quantum-fourier-transform-qft-via-controlled-phase-shifts)
9. [Classical ML vs. Quantum Machine Learning (QML)](#-classical-ml-vs-quantum-machine-learning-qml)
10. [Deep-Dive Implementations](#-deep-dive-implementations)
    - [Quantum Reservoir Computing (QRC) with Rydberg Atoms](#1-quantum-reservoir-computing-qrc-with-rydberg-atoms)
    - [Quanvolutional Neural Networks (QuanvNN) on BreastMNIST](#2-quanvolutional-neural-networks-quanvnn-on-breastmnist)
    - [Quantum Transfer Learning (QTL) with Dressed Quantum Nets](#3-quantum-transfer-learning-qtl-with-dressed-quantum-nets)
11. [Coherence Time, Decoherence & NV Centers in Diamond](#-coherence-time-decoherence--nv-centers-in-diamond)
12. [Complete Study Map & 6-Stage Learning Progression](#-complete-study-map--6-stage-learning-progression)
13. [Interactive Notebooks Suite](#-interactive-notebooks-suite)
14. [Modular Python Library (`src/`)](#-modular-python-library-src)
15. [Installation & Setup](#-installation--setup)
16. [Benchmark Results](#-benchmark-results)
17. [Academic Literature & References](#-academic-literature--references)

---

## 🏛️ The Three-Perspective Paradigm

Every quantum concept in this repository is articulated across three distinct, tightly connected layers:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   THE THREE PILLARS OF QUANTUM AI                      │
├────────────────────┬────────────────────┬──────────────────────────────┤
│ 1. MATHEMATICS     │ 2. PHYSICS         │ 3. PROGRAMMING               │
│ (Formal Theory)    │ (Physical Reality) │ (Executable Code)            │
├────────────────────┼────────────────────┼──────────────────────────────┤
│ Linear algebra,    │ Trapped ions,      │ Qiskit circuits,             │
│ complex amplitudes,│ superconducting    │ PennyLane QNodes,            │
│ Hilbert spaces,    │ circuits, neutral  │ Bloqade pulse schedules,     │
│ density matrices,  │ atoms, photonics,  │ autograd backpropagation,    │
│ Hamiltonians.      │ optical tweezers.  │ and classical PyTorch/TF ML. │
└────────────────────┴────────────────────┴──────────────────────────────┘
```

---

## 📚 Complete Theoretical Documentation Matrix

Detailed technical whitepapers for each paradigm are located in [`docs/`](docs/):

| Guide | Focus Areas | Key Formulations & Equations |
| :--- | :--- | :--- |
| [**01. Quantum Foundations**](docs/01_quantum_computing_basics.md) | Qubits, Superposition, Entanglement, States, Density Matrices | $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$, $\rho = \sum p_i |\psi_i\rangle\langle\psi_i|$, Bloch Sphere |
| [**02. Quantum Reservoir Computing**](docs/02_quantum_reservoir_computing.md) | Analog Rydberg Dynamics, van der Waals, Detuning Modulation | $\mathcal{H}(t) = \frac{\hbar\Omega}{2}\sum \sigma_i^x - \hbar\Delta\sum n_i + \sum \frac{C_6}{R^6}n_i n_j$ |
| [**03. Quanvolutional Networks**](docs/03_quanvolutional_networks.md) | Quantum Convolutions, 2D Filtering, BreastMNIST | Angle Embedding $R_Y(\pi p)$, `RandomLayers`, Pauli-$Z$ Observables |
| [**04. Quantum Transfer Learning**](docs/04_quantum_transfer_learning.md) | ResNet-18 Backbone, Dressed Quantum Circuits, Hybrid Autograd | Parameter-Shift Rule: $\partial_\theta \langle O \rangle = \frac{1}{2}[\langle O \rangle_{\theta+\pi/2} - \langle O \rangle_{\theta-\pi/2}]$ |
| [**05. Software & Organizations**](docs/05_quantum_software_ecosystems.md) | Bloqade vs. PennyLane vs. Qiskit; Global & Indian Ecosystems | Kirin IR, Lightning, Catalyst, NQM (₹6,003.65 Cr), IISc, TIFR |
| [**06. Quantum Fourier Transform**](docs/06_quantum_fourier_transform.md) | Discrete Fourier Transform, Controlled Phase Shifts, Circuits | $QFT|x\rangle = \frac{1}{\sqrt{N}}\sum e^{2\pi ixy/N}|y\rangle$, $\theta_k = \frac{2\pi}{2^{k+1}}$ |
| [**07. QML Paradigms & Mapping**](docs/07_quantum_machine_learning_paradigms.md) | 11 Classical ML $\to$ Quantum Counterparts, Decoherence | QSVM, QNN, QCNN, QLSTM, QGAN, QPCA, QPINN, Dephasing $T_2$ |

---

## 📂 Repository Directory Architecture

```
quantum-algorithms/
├── README.md                           # Master technical reference & educational framework
├── requirements.txt                    # Project dependencies (PennyLane, Qiskit, Bloqade, PyTorch, TF)
├── environment.yml                     # Conda/Mamba reproducible environment
├── .gitignore                          # Cleaned cache and intermediate tracking rules
│
├── 261012_demo.ipynb                   # Original workshop demo notebook (Qiskit & PennyLane)
├── QRC.ipynb                           # Original Quantum Reservoir Computing notebook (Bloqade)
├── qnn_medmnist.ipynb                  # Original Quanvolutional NN notebook (BreastMNIST)
├── qtl_colab.ipynb                     # Original Quantum Transfer Learning notebook (ResNet-18)
│
├── notebooks/                          # Production-ready Jupyter notebooks with rendered outputs
│   ├── 01_quantum_fundamentals.ipynb   # Qiskit & PennyLane foundations, Bloch sphere, states, density matrices
│   ├── 02_quantum_reservoir_computing.ipynb # Analog Rydberg atom reservoir computing with Bloqade
│   ├── 03_quanvolutional_neural_networks.ipynb # Quanvolution on BreastMNIST (PennyLane + TensorFlow)
│   └── 04_quantum_transfer_learning.ipynb # Hybrid classical-quantum transfer learning (ResNet-18 + PyTorch)
│
├── docs/                               # In-depth architectural & theoretical whitepapers
│   ├── 01_quantum_computing_basics.md  # 3-Perspective breakdown of 12 core concepts, study map
│   ├── 02_quantum_reservoir_computing.md # Rydberg Hamiltonian, blockade radius, detuning pulses
│   ├── 03_quanvolutional_networks.md   # Quantum convolutions, angle embedding, RandomLayers, BreastMNIST
│   └── 04_quantum_transfer_learning.md # 7-Stage QTL pipeline, parameter-shift rule, dataset bottlenecks
│   ├── 05_quantum_software_ecosystems.md # Bloqade, PennyLane, Qiskit, Global & Indian ecosystems
│   ├── 06_quantum_fourier_transform.md # QFT theory, controlled phase shifts, Qiskit & PennyLane code
│   └── 07_quantum_machine_learning_paradigms.md # Classical ML to QML mapping, noise & decoherence
│
├── data/                               # Dataset management & download utilities
│   ├── download_hymenoptera.py         # Automated dataset verification and download utility
│   └── hymenoptera_data/               # Ants & bees dataset (train & val splits)
│
├── src/                                # Reusable modular Python library
│   ├── __init__.py
│   ├── fundamentals/circuits.py        # Qiskit Bell state builder & PennyLane circuit primitives
│   ├── qrc/rydberg_reservoir.py        # Bloqade Rydberg analog reservoir simulation & Ridge readout
│   ├── quanv/quanvolution.py           # Quanvolutional 2D filter & batch feature transformation
│   └── qtl/dressed_quantum_net.py      # DressedQuantumNet PyTorch module & hybrid ResNet-18 builder
│
└── tools/
    └── generate_all_notebooks.py       # Notebook generation and verification pipeline
```

---

## 🔬 Fundamental Quantum Concepts: 12 Core Topics

See [**docs/01_quantum_computing_basics.md**](docs/01_quantum_computing_basics.md) for complete derivations:

1. **Superposition**: Linear combination $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ with $|\alpha|^2 + |\beta|^2 = 1$. Prepared via Hadamard gate $H|0\rangle = |+\rangle$.
2. **Entanglement**: Inseparable joint state $|\Psi\rangle \neq |\psi_1\rangle \otimes |\psi_2\rangle$. Demonstrated via Bell state $|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$.
3. **Interference**: Relative phase differences causing constructive and destructive probability cancellation: $H|\psi_+\rangle = |0\rangle$, $H|\psi_-\rangle = |1\rangle$.
4. **Qubit**: Basic two-level unit of quantum information residing in complex Hilbert space $\mathcal{H}_2 \cong \mathbb{C}^2$.
5. **Quantum States**: Mathematical specification determining probabilities for all physical observables.
6. **State Vector**: Complex amplitude column vector representing a pure quantum state ($2^n$ dimensions).
7. **Density Matrix**: General operator $\rho = \sum p_i |\psi_i\rangle\langle\psi_i|$ accommodating statistical mixtures and environmental decoherence.
8. **Superconducting Qubits**: Anharmonic LC circuits with Josephson junctions operating in dilution refrigerators (IBM, Google).
9. **Trapped-Ion Qubits**: Atomic ions trapped in RF electromagnetic fields driven by laser pulses (Quantinuum, IonQ).
10. **Photonic Qubits**: Qubits encoded in photon polarization or spatial modes (Xanadu, PsiQuantum).
11. **Neutral-Atom Qubits**: Neutral atoms suspended in optical tweezer arrays driven into Rydberg states (QuEra).
12. **Quantum Annealing**: Optimization via adiabatic Hamiltonian evolution $\mathcal{H}(t) = A(t)\mathcal{H}_{\text{init}} + B(t)\mathcal{H}_{\text{prob}}$ (D-Wave).

---

## ⚡ Physical Quantum Hardware Comparison

| Hardware Platform | Physical Realization | Control Mechanism | Operating Temp. | Advantages | Primary Challenges | Key Developers |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Superconducting** | Transmon circuits, Josephson junctions | Microwave pulses | $\sim 15\,\text{mK}$ | Fast gate speeds ($\sim 10-100\,\text{ns}$), lithographic fabrication | Short coherence times ($T_2 \sim 100\,\mu\text{s}$), crosstalk | IBM, Google, Rigetti |
| **Trapped Ions** | $^{171}\text{Yb}^+, \, ^{40}\text{Ca}^+$ in RF Paul traps | Focused UV/optical lasers | Room / Cryogenic | Long coherence times ($> 1\,\text{s}$), all-to-all connectivity | Slower gate speeds ($\sim 10-100\,\mu\text{s}$), complex optical routing | Quantinuum, IonQ |
| **Photonic** | Single photons in silica waveguides | Beam splitters, phase shifters | Room temperature (detectors mK) | Room temperature processor, low decoherence | Probabilistic entangling, photon absorption loss | Xanadu, PsiQuantum |
| **Neutral Atoms** | $^{87}\text{Rb}$ in optical tweezers | Laser pulses, Rydberg blockade | Ultra-cold vacuum ($\sim \mu\text{K}$) | Configurable arrays, native analog simulation, 256+ qubits | Slower reload times, atom loss | QuEra, Atom Computing |
| **Quantum Annealers**| Superconducting flux qubits | Inductive coupling loops | $\sim 15\,\text{mK}$ | 5,000+ qubits for QUBO optimization | Not universal gate-based quantum computers | D-Wave Systems |

---

## 💻 Quantum Software Ecosystem: Bloqade vs. PennyLane vs. Qiskit

See [**docs/05_quantum_software_ecosystems.md**](docs/05_quantum_software_ecosystems.md) for full analysis:

| Capability | Bloqade (QuEra) | PennyLane (Xanadu) | Qiskit (IBM) |
| :--- | :--- | :--- | :--- |
| **Primary Philosophy** | Analog Hamiltonian dynamics & neutral atom arrays | Differentiable quantum programming & hybrid QML | Gate-based circuits, pulse control, hardware compilation |
| **Central Abstraction** | Geometry layout + Laser detuning/Rabi waveforms | Quantum Nodes (`QNode`) + Autograd interfaces | `QuantumCircuit` + Unitary gate operations |
| **Gradient Engines** | Parameter sweeps / numerical differentiation | **Native Parameter-Shift Rule & adjoint differentiation** | Estimator / Sampler primitives |
| **Classical ML Bridge** | Python & Julia scientific workflows | **Native PyTorch, TensorFlow, JAX integrations** | Qiskit Machine Learning module |
| **Compiler & Acceleration**| Kirin Intermediate Representation | **Lightning (CPU/GPU) & Catalyst MLIR compiler** | Qiskit Transpiler & Qiskit Aer (C++) |

---

## 🌐 Global & Indian Quantum Technology Ecosystems

### International Leaders
- **IBM Quantum**: Industry standard for superconducting quantum processors and Qiskit.
- **Google Quantum AI**: Pioneering quantum supremacy, Sycamore processors, and surface-code error correction.
- **Rigetti Computing**: Superconducting quantum processors and hybrid cloud architectures.
- **IonQ & Quantinuum**: World-record quantum volume trapped-ion processors.
- **QuEra Computing**: 256-qubit analog neutral-atom processor Aquila and Bloqade SDK.
- **D-Wave Systems**: Commercial quantum annealing systems for combinatorial optimization.

### India's Quantum Ecosystem & National Quantum Mission (NQM)
- **National Quantum Mission (NQM)**: Approved with **₹6,003.65 crore** (2023–31) across quantum computing, communication, sensing, and materials.
- **Academic Research Hubs**:
  - **IISc Bengaluru**: Leads the *IISc Quantum Technology Initiative (IQTI)* across hardware, materials, and algorithms.
  - **TIFR Mumbai**: Fundamental quantum information theory, superconducting circuits, and condensed matter physics.
- **Domestic Quantum Industry**:
  - **Qbit Force**: Superconducting quantum hardware, cryogenic electronics, and fabrication.
  - **QNU Labs**: Quantum cybersecurity, Quantum Key Distribution (QKD), and Post-Quantum Cryptography (PQC).
  - **QpiAI**: Accelerating quantum computing and AI hardware integration.

---

## 📐 Quantum Fourier Transform (QFT) via Controlled Phase Shifts

See [**docs/06_quantum_fourier_transform.md**](docs/06_quantum_fourier_transform.md):

The Quantum Fourier Transform transforms quantum state amplitudes with exponential gate efficiency:

$$\boxed{\text{QFT}|x\rangle = \frac{1}{\sqrt{N}}\sum_{y=0}^{N-1} e^{2\pi ixy/N}|y\rangle, \quad N = 2^n}$$

### Circuit Synthesis via Controlled Phase Shifts $CP(\theta)$:
For an $n$-qubit register, the controlled phase angle depends on qubit distance $k$:
$$\theta_k = \frac{2\pi}{2^{k+1}} = \left\{ \frac{\pi}{2}, \frac{\pi}{4}, \frac{\pi}{8}, \dots \right\}$$

Two-qubit circuit sequence:
$$\boxed{H_0 \;\longrightarrow\; CP_{1, 0}\left(\frac{\pi}{2}\right) \;\longrightarrow\; H_1 \;\longrightarrow\; \text{SWAP}(0, 1)}$$

---

## 🤖 Classical ML vs. Quantum Machine Learning (QML)

See [**docs/07_quantum_machine_learning_paradigms.md**](docs/07_quantum_machine_learning_paradigms.md):

| Classical Machine Learning | Quantum Counterpart | Mathematical Mechanism | Primary Application |
| :--- | :--- | :--- | :--- |
| **Support Vector Machine (SVM)** | **QSVM** | Quantum Kernel $K(\mathbf{x}, \mathbf{z}) = \|\langle \phi(\mathbf{x}) \| \phi(\mathbf{z}) \rangle\|^2$ | Non-linear classification |
| **Neural Network (NN)** | **QNN** | Variational ansatz $f(\mathbf{x}) = \langle 0 \| U^\dagger \hat{O} U \| 0 \rangle$ | Expressive low-parameter modeling |
| **Convolutional Net (CNN)** | **QuanvNN / QCNN** | Quantum receptive fields & quantum pooling | Spatial image filtering (BreastMNIST) |
| **Recurrent Net (RNN)** | **Quantum Graph RNN** | Spatial graph + temporal recurrence | Complex spatio-temporal dynamics |
| **Long Short-Term Memory (LSTM)** | **QLSTM** | Parameterized circuits inside memory gates | Long-term sequential dependencies |
| **Generative Adversarial Net (GAN)**| **QGAN** | Parameterized quantum state distributions | Quantum state generation & sampling |
| **Principal Component Analysis** | **Quantum PCA** | Density matrix phase estimation | $O(\log N)$ spectral analysis on qRAM |
| **Transfer Learning** | **QTL** | Pre-trained CNN + Dressed Quantum Net | NISQ image classification (Ants vs. Bees)|
| **Reservoir Computing** | **QRC** | Neutral-atom analog Rydberg Hamiltonian | Zero-backprop time-series forecasting |
| **Physics-Informed NN (PINN)** | **QPINN** | Analytic parameter-shift loss residuals | Solving non-linear differential equations|

---

## 🛠️ Deep-Dive Implementations

### 1. Quantum Reservoir Computing (QRC) with Rydberg Atoms
- **Physical Model**: 5 $^{87}\text{Rb}$ atoms in 1D array ($6.0\,\mu\text{m}$ spacing).
- **Hamiltonian**: Constant Rabi drive $\Omega = 2.5\,\text{rad}/\mu\text{s}$, detuning $\Delta(t)$ modulated by sliding input windows.
- **Readout**: Ridge regression on 1-body occupations $\langle n_i \rangle$ and 2-body spatial correlations $\langle n_i n_j \rangle$.
- **Result**: Test **RMSE 0.1245** vs. Persistence Baseline 0.2814.
- **Notebook**: [`notebooks/02_quantum_reservoir_computing.ipynb`](notebooks/02_quantum_reservoir_computing.ipynb)

### 2. Quanvolutional Neural Networks (QuanvNN) on BreastMNIST
- **Quantum Kernel**: 4 qubits with angle embedding $R_Y(\pi p_j)$ and Haar-random entangling layers (`RandomLayers`).
- **Feature Map**: Downsamples $28 \times 28 \times 1$ ultrasound images to $14 \times 14 \times 4$ quantum feature representations.
- **Result**: Test validation accuracy **$\sim 83.3\%$** vs. classical linear model $\sim 70.0\%$.
- **Notebook**: [`notebooks/03_quanvolutional_neural_networks.ipynb`](notebooks/03_quanvolutional_neural_networks.ipynb)

### 3. Quantum Transfer Learning (QTL) with Dressed Quantum Nets
- **Architecture**: Frozen ResNet-18 (512 features) $\to$ Pre-Net (4 angles) $\to$ Depth-6 VQC $\to$ Post-Net (2 classes).
- **Optimization**: Analytic backpropagation via the **Parameter-Shift Rule**.
- **Result**: Validation accuracy **$> 75-85\%$ within 5 epochs** on Ants vs. Bees without overfitting.
- **Notebook**: [`notebooks/04_quantum_transfer_learning.ipynb`](notebooks/04_quantum_transfer_learning.ipynb)

---

## ⏱️ Coherence Time, Decoherence & NV Centers in Diamond

- **Decoherence**: Environmental interactions destroying off-diagonal quantum state coherences:
  $$\rho(t) = \frac{1}{2}\begin{bmatrix} 1 & e^{-t/T_2} \\ e^{-t/T_2} & 1 \end{bmatrix} \quad \xrightarrow{t \gg T_2} \quad \frac{1}{2}\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$
- **Coherence Times**:
  $$\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}$$
  $T_1$: Energy relaxation timescale. $T_2$: Dephasing timescale. $T_\phi$: Pure dephasing.
- **Nitrogen-Vacancy (NV) Centers in Diamond**:
  - Point defect in diamond lattice providing isolated electron spin qubits.
  - Achieves coherence times of **tens to hundreds of milliseconds (up to 800+ ms)** at room temperature with **Dynamical Decoupling** microwave pulse sequences.

---

## 🗺️ Complete Study Map & 6-Stage Learning Progression

```
┌────────────────────────────────────────────────────────────────────────┐
│                   RECOMMENDED LEARNING PROGRESSION                     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    Stage 1: Linear Algebra & Math Foundations (Vectors, Matrices, Complex Numbers)
                                    ▼
    Stage 2: Fundamental Quantum Concepts (Qubit, Superposition, Entanglement, Gates)
                                    ▼
    Stage 3: Quantum Programming (Qiskit & PennyLane Basics, Bell States, QNodes)
                                    ▼
    Stage 4: Quantum Noise & Open Systems (Density Matrices, Decoherence, T1 & T2)
                                    ▼
    Stage 5: Hardware Architectures (Superconducting, Trapped Ion, Neutral Atom, Annealing)
                                    ▼
    Stage 6: Quantum Algorithms & Advanced QML (QFT, VQE, QAOA, QRC, QuanvNN, QTL)
```

---

## 📓 Interactive Notebooks Suite

| Notebook | Focus Area | Frameworks | Key Highlights |
| :--- | :--- | :--- | :--- |
| [`01_quantum_fundamentals.ipynb`](notebooks/01_quantum_fundamentals.ipynb) | Foundations & State Algebra | Qiskit, PennyLane | Statevectors, density matrices, Bloch sphere, Bell states, QNode visualization |
| [`02_quantum_reservoir_computing.ipynb`](notebooks/02_quantum_reservoir_computing.ipynb) | Analog Rydberg Dynamics | Bloqade (QuEra) | 5-atom tweezer chain, detuning pulse modulation, 2-body spatial correlations, Ridge readout |
| [`03_quanvolutional_neural_networks.ipynb`](notebooks/03_quanvolutional_neural_networks.ipynb) | Quantum Spatial Filtering | PennyLane, TensorFlow | 2x2 quanvolution stride 2, BreastMNIST classification, comparative accuracy benchmark |
| [`04_quantum_transfer_learning.ipynb`](notebooks/04_quantum_transfer_learning.ipynb) | Hybrid Deep Learning | PennyLane, PyTorch | ResNet-18 feature extraction, DressedQuantumNet, parameter-shift backpropagation |

---

## 💻 Modular Python Library (`src/`)

### 1. Quantum Reservoir Computing
```python
from src.qrc import RydbergReservoir, generate_synthetic_time_series

t, signal = generate_synthetic_time_series(n_points=90)
reservoir = RydbergReservoir(n_atoms=5, spacing=6.0, shots=120)
features = reservoir.extract_features(signal[:5])
print("Extracted quantum observables shape:", features.shape) # (15,)
```

### 2. Quanvolutional Filtering
```python
from src.quanv import QuanvolutionFilter
import numpy as np

quanv = QuanvolutionFilter(n_layers=1)
image = np.random.rand(28, 28)
q_features = quanv.transform_image(image, stride=2)
print("Quanvolved feature map shape:", q_features.shape) # (14, 14, 4)
```

### 3. Quantum Transfer Learning
```python
from src.qtl import create_hybrid_resnet
import torch

model = create_hybrid_resnet(num_classes=2, n_qubits=4, q_depth=6)
dummy_batch = torch.randn(4, 3, 224, 224)
logits = model(dummy_batch)
print("Output logits shape:", logits.shape) # (4, 2)
```

---

## 🚀 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/gaminization/quantum-algorithms.git
cd quantum-algorithms

# Virtual Environment Setup
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verify dataset
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
| **Quantum Transfer Learning (QTL)** | Hymenoptera (Ants vs. Bees) | ResNet-18 (ImageNet) + Dressed QNet | **Val Accuracy: ~75-85%** (5 Epochs) | Rapid convergence without overfitting |

---

## 📚 Academic Literature & References

1. **Mari, A., et al.** (2020). *Transfer learning in hybrid classical-quantum neural networks*. Quantum, 4, 340. [arXiv:1912.08278](https://arxiv.org/abs/1912.08278).
2. **Henderson, M., et al.** (2020). *Quanvolutional neural networks: powering image recognition with quantum circuits*. Quantum Machine Intelligence, 2(1), 2. [arXiv:1904.04767](https://arxiv.org/abs/1904.04767).
3. **Schuld, M., et al.** (2019). *Evaluating analytic gradients on quantum hardware*. Phys. Rev. A, 99(3), 032331. [arXiv:1811.11184](https://arxiv.org/abs/1811.11184).
4. **Bernien, H., et al.** (2017). *Probing many-body dynamics on a 51-atom quantum simulator*. Nature, 551(7682), 579–584.
5. **Nielsen, M. A., & Chuang, I. L.** (2010). *Quantum Computation and Quantum Information*. Cambridge University Press.
6. **Yang, J., et al.** (2023). *MedMNIST v2: A large-scale lightweight benchmark for 2D and 3D biomedical image classification*. Scientific Data, 10(1), 41.

---

<div align="center">
Developed with ❤️ for Quantum AI Researchers and Developers.
</div>