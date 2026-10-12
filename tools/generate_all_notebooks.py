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
    orig = load_nb("261012_demo.ipynb")
    cells = []

    cells.append(md_cell("""# 01. Quantum Fundamentals, Statevectors, and Variational Circuits
### Foundations of Quantum Information Science with Qiskit and PennyLane

---

## Overview & Learning Objectives
This notebook provides a hands-on exploration of the foundational building blocks of quantum computing:
1. **Classical vs. Quantum Bits**: Mathematical representation in Hilbert space, Dirac bra-ket notation, and state superposition.
2. **Statevectors & Density Matrices**: Distinguishing pure quantum states from statistical mixtures; density operator algebra.
3. **Quantum Gates & Unitary Transformations**: Single-qubit rotations ($X, Y, Z, H, R_Y, R_Z$) and 2-qubit entangling gates ($CNOT$).
4. **Geometric State Representation**: The Bloch Sphere and Cartesian coordinate parameterization.
5. **Differentiable Quantum Programming**: Parameterized variational circuits, Quantum Nodes (`QNode`), and expectation value measurements in PennyLane.

---

## 1. Mathematical Framework

### 1.1 The Qubit State Space
Unlike a classical bit which is strictly constrained to $0$ or $1$, a qubit lives in a two-dimensional complex Hilbert space $\\mathcal{H}_2$. A state $|\\psi\\rangle$ is defined as:

$$|\\psi\\rangle = \\alpha |0\\rangle + \\beta |1\\rangle = \\alpha \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix} + \\beta \\begin{pmatrix} 0 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} \\alpha \\\\ \\beta \\end{pmatrix}$$

where $\\alpha, \\beta \\in \\mathbb{C}$, satisfying the normalization constraint:
$$|\\alpha|^2 + |\\beta|^2 = 1$$

According to the **Born Rule**, measurement in the computational basis $\{|0\\rangle, |1\\rangle\}$ yields:
- Probability of measuring state $0$: $P(0) = |\\langle 0 | \\psi \\rangle|^2 = |\\alpha|^2$
- Probability of measuring state $1$: $P(1) = |\\langle 1 | \\psi \\rangle|^2 = |\\beta|^2$

### 1.2 Multi-Qubit Registers and Tensor Products
For an $n$-qubit system, the composite state space is the tensor product of individual qubit spaces:
$$\\mathcal{H} = \\mathcal{H}_1 \\otimes \\mathcal{H}_2 \\otimes \\dots \\otimes \\mathcal{H}_n \\cong \\mathbb{C}^{2^n}$$

For a 2-qubit system initialized in ground state:
$$|00\\rangle = |0\\rangle \\otimes |0\\rangle = \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix} \\otimes \\begin{pmatrix} 1 \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \\end{pmatrix}$$

Applying the Hadamard gate $H = \\frac{1}{\\sqrt{2}}\\begin{pmatrix} 1 & 1 \\\\ 1 & -1 \\end{pmatrix}$ to both qubits produces the uniform superposition:
$$|++\\rangle = (H|0\\rangle) \\otimes (H|0\\rangle) = \\frac{1}{2}(|00\\rangle + |01\\rangle + |10\\rangle + |11\\rangle) = \\frac{1}{2}\\begin{pmatrix} 1 \\\\ 1 \\\\ 1 \\\\ 1 \\end{pmatrix}$$

### 1.3 Density Matrices: Pure vs. Mixed States
For an ensemble of quantum states $\{|\\psi_i\\rangle\}$ with probabilities $\{p_i\}$, the state is described by the density operator:
$$\\rho = \\sum_{i} p_i |\\psi_i\\rangle \\langle\\psi_i|, \\quad \\text{Tr}(\\rho) = 1, \\quad \\rho = \\rho^\\dagger, \\quad \\rho \\ge 0$$
- **Pure state**: $\\text{Tr}(\\rho^2) = 1$
- **Mixed state**: $\\text{Tr}(\\rho^2) < 1$

### 1.4 Bloch Sphere Parameterization
Any single-qubit pure state can be written up to a global phase as:
$$|\\psi\\rangle = \\cos\\left(\\frac{\\theta}{2}\\right)|0\\rangle + e^{i\\phi}\\sin\\left(\\frac{\\theta}{2}\\right)|1\\rangle$$
where $\\theta \\in [0, \\pi]$ is the polar angle and $\\phi \\in [0, 2\\pi)$ is the azimuthal angle.
The corresponding coordinates on the unit sphere are:
$$\\vec{r} = (x, y, z) = (\\sin\\theta\\cos\\phi, \\; \\sin\\theta\\sin\\phi, \\; \\cos\\theta)$$"""))

    cells.append(orig["cells"][0])  # pip install
    cells.append(md_cell("""## 2. Circuit Construction, Superposition, and State Analysis in Qiskit
We define a 2-qubit register, create superposition using Hadamard gates, and compare the mathematical representations before and after gate execution."""))
    cells.append(orig["cells"][1])  # imports
    cells.append(orig["cells"][2])  # circuit & statevector/density matrix computation
    cells.append(md_cell("""### 2.1 Statevectors
Notice the transition from deterministic state $|00\\rangle$ to equal-superposition $|++\\rangle$:"""))
    cells.append(orig["cells"][3])  # sv1
    cells.append(orig["cells"][4])  # sv2
    cells.append(md_cell("""### 2.2 Density Matrices
Comparing the outer product $\\rho_1 = |00\\rangle\\langle 00|$ with $\\rho_2 = |++\\rangle\\langle ++|$:"""))
    cells.append(orig["cells"][5])  # dm1
    cells.append(orig["cells"][6])  # dm2
    cells.append(md_cell("""---
## 3. Geometric Visualization: The Bloch Sphere
Visualizing the single-qubit statevector on the Bloch Sphere. The state $|0\\rangle$ corresponds to $\\theta = 0$, pointing straight up along the $+Z$ axis."""))
    cells.append(orig["cells"][7])  # bloch vector import
    cells.append(orig["cells"][8])  # plot_bloch_multivector
    cells.append(md_cell("""---
## 4. Parameterized Variational Quantum Circuits in PennyLane
PennyLane allows defining quantum circuits as differentiable nodes (**QNodes**).
Here we construct a 2-qubit circuit with:
- Parameterized rotation $R_Z(x)$ on qubit 0
- Entangling $CNOT$ gate between qubits 0 and 1
- Parameterized rotation $R_Y(y)$ on qubit 1
- Measurement of the expectation value $\\langle \\hat{Z}_1 \\rangle$"""))
    cells.append(orig["cells"][9])   # pip install pennylane
    cells.append(orig["cells"][10])  # import pennylane
    cells.append(orig["cells"][11])  # quantum function
    cells.append(orig["cells"][12])  # device
    cells.append(orig["cells"][13])  # numpy import
    cells.append(orig["cells"][14])  # QNode definition
    cells.append(md_cell("""### 4.1 Circuit Rendering & Visual Verification"""))
    cells.append(orig["cells"][15])  # text draw
    cells.append(orig["cells"][16])  # matplotlib import
    cells.append(orig["cells"][17])  # draw_mpl

    orig["cells"] = cells
    out_path = NOTEBOOKS_DIR / "01_quantum_fundamentals.ipynb"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(orig, f, indent=1)
    print(f"Created: {out_path}")


# =====================================================================
# 2. NOTEBOOK 02: QUANTUM RESERVOIR COMPUTING (QRC)
# =====================================================================
def build_notebook_02():
    orig = load_nb("QRC.ipynb")
    cells = []

    cells.append(md_cell("""# 02. Quantum Reservoir Computing (QRC) on Neutral Atom Arrays
### Analog Quantum Simulation, Rydberg Blockade Physics, and Time-Series Forecasting with Bloqade

---

## Overview & Key Concepts
**Quantum Reservoir Computing (QRC)** is a computational paradigm that exploits the natural, non-linear, high-dimensional dynamics of quantum many-body systems to process temporal data.
Instead of training all variational parameters inside deep quantum circuits (which suffer from barren plateaus and high optimization overhead), QRC uses:
1. **A Fixed Quantum Reservoir**: An analog physical quantum system driven by input signals.
2. **A Linear Readout Layer**: Simple classical regression or classification trained on extracted quantum observables.

### Key Strengths of QRC:
- **No Quantum Backpropagation**: Zero need to differentiate through the quantum reservoir or update quantum gates during training.
- **Hardware-Efficient**: Ideal for analog quantum processors (neutral atoms, superconducting annealers) without error correction.
- **Fading Memory & Non-Linear Mapping**: Naturally satisfies the *Echo State Property* required for non-linear temporal tasks.

---

## 1. Physical Model: Neutral Rydberg Atom Arrays

### 1.1 The Neutral Atom Hamiltonian
Neutral alkali atoms (e.g., $^{87}\\text{Rb}$) trapped in optical tweezer arrays are excited from their ground state $|g\\rangle$ to high-lying Rydberg states $|r\\rangle$ with principal quantum number $n \\gg 1$.
The time-dependent many-body Hamiltonian governing the system in the rotating frame is:

$$\\mathcal{H}(t) = \\frac{\\hbar \\Omega(t)}{2} \\sum_{i=1}^{N} \\sigma_i^x - \\hbar \\Delta(t) \\sum_{i=1}^{N} n_i + \\sum_{i < j} \\frac{C_6}{|\\mathbf{r}_i - \\mathbf{r}_j|^6} n_i n_j$$

Where:
- $\\Omega(t)$ is the **Rabi frequency** driving coherent oscillations between $|g\\rangle$ and $|r\\rangle$.
- $\\sigma_i^x = |g_i\\rangle\\langle r_i| + |r_i\\rangle\\langle g_i|$ is the Pauli-$X$ transition operator.
- $\\Delta(t) = \\omega_L - \\omega_0$ is the **laser detuning** from atomic resonance.
- $n_i = |r_i\\rangle\\langle r_i| = \\frac{1 + \\sigma_i^z}{2}$ is the Rydberg state projector (occupation number).
- $C_6$ is the van der Waals interaction coefficient ($C_6 \\propto n^{11}$).
- $|\\mathbf{r}_i - \\mathbf{r}_j|$ is the spatial distance between atoms $i$ and $j$.

### 1.2 The Rydberg Blockade Effect
When two atoms are closer than the **blockade radius** $R_b = (C_6 / \\hbar \\Omega)^{1/6}$, the repulsive energy shift $V_{ij} = C_6 / R^6$ prevents simultaneous excitation of both atoms to the Rydberg state. This produces strong, non-local quantum correlations across the array without explicit 2-qubit gate compilation.

### 1.3 Reservoir Observable Extraction
From projective measurements across $S$ measurement shots:
1. **Single-atom Rydberg occupations**: $\\langle n_i \\rangle = \\frac{1}{S} \\sum_{s=1}^S (1 - b_{i, s})$
2. **Two-body spatial density correlations**: $\\langle n_i n_j \\rangle = \\frac{1}{S} \\sum_{s=1}^S (1 - b_{i, s})(1 - b_{j, s})$ for $i < j$

For $N=5$ atoms, this produces $5 + \\binom{5}{2} = 5 + 10 = 15$ feature observables per input window."""))

    cells.append(orig["cells"][0])  # pip install
    cells.append(md_cell("""## 2. Synthetic Non-linear Time Series Problem
We generate a complex time series consisting of two non-harmonic sinusoids plus Gaussian noise:
$$s(t) = 0.65 \\sin\\left(\\frac{2\\pi t}{18}\\right) + 0.25 \\sin\\left(\\frac{2\\pi t}{7}\\right) + \\epsilon(t)$$
We slice the series into sliding windows of length $W=5$ to forecast the next time step $s(t+1)$."""))
    cells.append(orig["cells"][1])  # imports
    cells.append(orig["cells"][2])  # data generation & plotting
    cells.append(md_cell("""## 3. Physical Atom Geometry & Control Pulse Parameters
We place $N=5$ atoms along a 1D chain with uniform spacing $d = 6.0\\,\\mu\\text{m}$.
The input values within each temporal window are encoded into the laser **detuning** $\\Delta(t)$ as piecewise-constant segments of duration $\\tau = 0.20\\,\\mu\\text{s}$ under constant Rabi driving $\\Omega = 2.5\\,\\text{rad}/\\mu\\text{s}$."""))
    cells.append(orig["cells"][3])  # atom setup
    cells.append(orig["cells"][4])  # build_reservoir_program
    cells.append(md_cell("""## 4. Analog Simulation & Quantum Feature Extraction
For each input window, Bloqade simulates the analog Hamiltonian dynamics and collects measurement bitstrings.
We calculate both 1-body expectations $\\langle n_i \\rangle$ and 2-body spatial correlations $\\langle n_i n_j \\rangle$."""))
    cells.append(orig["cells"][5])  # extract_features
    cells.append(orig["cells"][6])  # make_feature_matrix
    cells.append(md_cell("""## 5. Classical Readout Training: Ridge Regression
We feed the extracted quantum feature matrix into a standardized **Ridge Regression** model:
$$\\min_{\\mathbf{w}} \\| \\mathbf{X}_q \\mathbf{w} - \\mathbf{y} \\|_2^2 + \\alpha \\| \\mathbf{w} \\|_2^2$$"""))
    cells.append(orig["cells"][7])  # readout model
    cells.append(orig["cells"][8])  # plot predictions
    cells.append(md_cell("""## 6. Benchmark: Comparison with Persistence Baseline
A standard benchmark for time-series forecasting is the classical **Persistence Model** (naive prediction: $\\hat{y}_{t+1} = y_t$). We compare Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE)."""))
    cells.append(orig["cells"][9])  # persistence comparison

    orig["cells"] = cells
    out_path = NOTEBOOKS_DIR / "02_quantum_reservoir_computing.ipynb"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(orig, f, indent=1)
    print(f"Created: {out_path}")


# =====================================================================
# 3. NOTEBOOK 03: QUANVOLUTIONAL NEURAL NETWORKS (QUANVNN)
# =====================================================================
def build_notebook_03():
    orig = load_nb("qnn_medmnist.ipynb")
    cells = []

    cells.append(md_cell("""# 03. Quanvolutional Neural Networks (QuanvNN) for Medical Imaging
### Quantum Image Filtering with Random Entangling Circuits on BreastMNIST

---

## Overview & Scientific Background
**Quanvolutional Neural Networks (QuanvNN)**, introduced by Henderson et al. (2020), extend classical Convolutional Neural Networks (CNNs) by replacing classical linear kernel filters with **local parameterized quantum circuits**.

### Why Quanvolution?
- **High-Dimensional Hilbert Space Mapping**: A small $2 \\times 2$ pixel patch is transformed into the $2^4 = 16$-dimensional state space of 4 entangled qubits.
- **Non-Linear Quantum Kernel Representation**: Quantum gates induce complex non-linear correlations that classical single-layer convolutions cannot natively compute.
- **Scalability for NISQ Devices**: Instead of loading the entire image into a massive quantum register (which requires hundreds of error-corrected qubits), quanvolution operates locally on small patches using only 4 qubits!

---

## 1. Architectural Pipeline

### 1.1 Local Receptive Field & Angle Encoding
For each $2 \\times 2$ spatial receptive field $[x_{0,0}, x_{0,1}, x_{1,0}, x_{1,1}]$ with stride $s=2$:
1. **Angle Embedding**: Each normalized pixel intensity $p_j \\in [0, 1]$ is encoded into the rotation angle of an $R_Y$ gate:
   $$|\\psi_{\\text{in}}\\rangle = \\bigotimes_{j=0}^{3} R_Y(\\pi p_j) |0\\rangle$$
2. **Entangling Unitary Transformation (`RandomLayers`)**:
   A parameterized unitary transformation $U(\\vec{\\theta})$ comprising random single-qubit rotations and entangling gates (e.g. CNOTs) mixes the spatial information:
   $$|\\psi_{\\text{out}}\\rangle = U(\\vec{\\theta}) |\\psi_{\\text{in}}\\rangle$$
3. **Quantum Measurement Observables**:
   Expectation values of the Pauli-$Z$ operator on each of the 4 qubits are extracted:
   $$f_c = \\langle \\psi_{\\text{out}} | \\hat{Z}_c | \\psi_{\\text{out}} \\rangle \\in [-1, 1], \\quad c \\in \\{0, 1, 2, 3\\}$$
4. **Spatial Downsampling**:
   An input image of shape $(28, 28, 1)$ is transformed into a rich 4-channel quantum feature map of shape $(14, 14, 4)$.

### 1.2 Downstream Classification
The extracted quantum feature map is flattened and passed to a Dense classification layer in Keras/TensorFlow for binary medical diagnosis on **BreastMNIST** (benign vs. malignant ultrasound scans)."""))

    cells.append(orig["cells"][0])  # pip install
    cells.append(orig["cells"][1])  # imports
    cells.append(orig["cells"][2])  # hyperparameters
    cells.append(md_cell("""## 2. Medical Dataset: BreastMNIST
The **BreastMNIST** dataset from the MedMNIST benchmark comprises 2D ultrasound breast cancer images classified as benign (class 0) or malignant (class 1)."""))
    cells.append(orig["cells"][3])  # dataset download & load
    cells.append(orig["cells"][4])  # normalization & channel expansion
    cells.append(md_cell("""## 3. Quantum Convolution Circuit Definition
We configure a 4-qubit PennyLane circuit initialized with $R_Y(\\pi \\cdot x)$ angle embedding, followed by a random entangling layer (`RandomLayers`) and Pauli-$Z$ expectation measurements."""))
    cells.append(orig["cells"][5])  # circuit definition
    cells.append(orig["cells"][6])  # quanv function
    cells.append(md_cell("""## 4. Quantum Preprocessing & Feature Extraction
We slide the 4-qubit quanvolutional kernel across all images in the training and testing sets, saving the resulting feature tensors."""))
    cells.append(orig["cells"][7])  # preprocessing loop
    cells.append(md_cell("""## 5. Visualizing Extracted Quantum Feature Channels
Here we compare the raw grayscale input images with the 4 extracted quantum channel representations."""))
    cells.append(orig["cells"][8])  # visualization plot
    cells.append(md_cell("""## 6. Downstream Model & Comparative Benchmark
We define a classification network in Keras and train two models:
1. **With Quantum Layer**: Trained on the $(14, 14, 4)$ quanvolved feature representations.
2. **Without Quantum Layer**: Trained directly on the raw image pixels as a classical baseline."""))
    cells.append(orig["cells"][9])   # MyModel definition
    cells.append(orig["cells"][10])  # q_model training
    cells.append(orig["cells"][11])  # c_model training
    cells.append(md_cell("""## 7. Performance Comparison & Validation Trajectories
Visualizing the validation accuracy curves of both architectures across optimization epochs."""))
    cells.append(orig["cells"][12])  # comparison plot

    orig["cells"] = cells
    out_path = NOTEBOOKS_DIR / "03_quanvolutional_neural_networks.ipynb"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(orig, f, indent=1)
    print(f"Created: {out_path}")


# =====================================================================
# 4. NOTEBOOK 04: QUANTUM TRANSFER LEARNING (QTL)
# =====================================================================
def build_notebook_04():
    orig = load_nb("qtl_colab.ipynb")
    cells = []

    cells.append(md_cell("""# 04. Quantum Transfer Learning (QTL) with Dressed Quantum Circuits
### Hybrid Classical-Quantum Deep Learning with Pre-Trained ResNet-18 & PennyLane

---

## Overview & Scientific Foundation
**Quantum Transfer Learning (QTL)**, pioneered by Mari et al. (2019) (*"Transfer learning in hybrid classical-quantum neural networks"*, arXiv:1912.08278), addresses the input bottleneck of NISQ devices:
- High-resolution real-world images (e.g. $224 \\times 224 \\times 3$) have tens of thousands of degrees of freedom. Directly encoding them into quantum states would require prohibitive quantum depth and hundreds of qubits.
- In QTL, a powerful classical deep neural network pre-trained on ImageNet (such as **ResNet-18**) serves as a **feature extractor**, compressing complex visual patterns into a compact 512-dimensional latent vector.
- A **Dressed Quantum Circuit** replaces the final classification head, processing the high-level features in a low-dimensional variational quantum Hilbert space!

---

## 1. The Dressed Quantum Circuit Architecture

### 1.1 Architecture & Information Flow
$$\\mathbf{x} \\xrightarrow{\\text{ResNet-18 (frozen)}} \\mathbf{h} \\in \\mathbb{R}^{512} \\xrightarrow{\\text{Pre-Net}} \\mathbf{z} \\in \\left[-\\frac{\\pi}{2}, \\frac{\\pi}{2}\\right]^4 \\xrightarrow{\\text{VQC}} \\mathbf{q} \\in [-1, 1]^4 \\xrightarrow{\\text{Post-Net}} \\mathbf{y} \\in \\mathbb{R}^2$$

1. **Feature Extractor**: Pre-trained ResNet-18 outputs a 512-dimensional embedding $\\mathbf{h}$. Its convolutional weights are frozen.
2. **Classical Pre-processing (`pre_net`)**:
   A trainable linear layer reduces dimension from 512 to 4, followed by non-linear scaling:
   $$z_j = \\tanh(W_{\\text{pre}} \\mathbf{h} + b_{\\text{pre}})_j \\cdot \\frac{\\pi}{2}$$
3. **Variational Quantum Circuit (VQC)**:
   - **Superposition initialization**: $|\\psi_0\\rangle = H^{\\otimes 4} |0\\rangle^{\\otimes 4} = |+\\rangle^{\\otimes 4}$
   - **Feature encoding**: Single-qubit rotations $R_Y(z_j)$ embed inputs into qubit amplitudes.
   - **Trainable Variational Layers**: Alternating layers of CNOT ring entanglers and parameterized $R_Y(w_{l, j})$ rotations across depth $d=6$.
   - **Quantum Measurement**: Pauli-$Z$ expectation values on all 4 qubits: $q_j = \\langle \\psi | \\hat{Z}_j | \\psi \\rangle$.
4. **Classical Post-processing (`post_net`)**:
   Linear readout layer mapping the 4 quantum expectation values to 2 class logits (Ants vs. Bees).

### 1.2 End-to-End Hybrid Optimization
Gradients flow seamlessly from the cross-entropy loss through the classical post-net, through the variational quantum circuit via the **parameter-shift rule**:
$$\\frac{\\partial \\langle \\hat{O} \\rangle}{\\partial \\theta_k} = \\frac{\\langle \\hat{O} \\rangle_{\\theta_k + \\frac{\\pi}{2}} - \\langle \\hat{O} \\rangle_{\\theta_k - \\frac{\\pi}{2}}}{2}$$
and into the pre-processing linear layer using standard PyTorch autograd!"""))

    cells.append(orig["cells"][0])  # %matplotlib inline
    cells.append(orig["cells"][1])  # pip install
    cells.append(orig["cells"][2])  # imports & seeds
    cells.append(orig["cells"][3])  # hyperparameters
    cells.append(md_cell("""## 2. PennyLane Device & Hardware Acceleration Setup
We initialize a PennyLane `default.qubit` device with $N=4$ wires and configure PyTorch GPU/CPU acceleration."""))
    cells.append(orig["cells"][5])  # dev
    cells.append(orig["cells"][6])  # device
    cells.append(orig["cells"][7])  # device print

    # Replace cell 8 with robust path resolution
    robust_cell_8 = dict(orig["cells"][8])
    robust_cell_8["source"] = [
        "import os\n",
        "from pathlib import Path\n",
        "\n",
        "# Robust dataset path resolution (supports local clone, notebooks dir, Colab Drive, and auto-download)\n",
        "candidate_paths = [\n",
        "    Path('../data/hymenoptera_data'),\n",
        "    Path('data/hymenoptera_data'),\n",
        "    Path('/content/quantum-algorithms/data/hymenoptera_data'),\n",
        "    Path('/content/drive/MyDrive/Dayanand Sagar FDP/hymenoptera_data')\n",
        "]\n",
        "\n",
        "data_dir = None\n",
        "for cp in candidate_paths:\n",
        "    if cp.exists() and (cp / 'train').exists():\n",
        "        data_dir = str(cp)\n",
        "        print(f'Found dataset at: {data_dir}')\n",
        "        break\n",
        "\n",
        "if data_dir is None:\n",
        "    try:\n",
        "        from google.colab import drive\n",
        "        drive.mount('/content/drive')\n",
        "        data_dir = '/content/drive/MyDrive/Dayanand Sagar FDP/hymenoptera_data'\n",
        "    except Exception:\n",
        "        import urllib.request, zipfile\n",
        "        print('Downloading Hymenoptera dataset...')\n",
        "        url = 'https://download.pytorch.org/tutorial/hymenoptera_data.zip'\n",
        "        urllib.request.urlretrieve(url, 'hymenoptera_data.zip')\n",
        "        with zipfile.ZipFile('hymenoptera_data.zip', 'r') as zf:\n",
        "            zf.extractall('data')\n",
        "        data_dir = 'data/hymenoptera_data'\n",
        "\n",
        "data_transforms = {\n",
        "    'train': transforms.Compose([\n",
        "        transforms.Resize(256),\n",
        "        transforms.CenterCrop(224),\n",
        "        transforms.ToTensor(),\n",
        "        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),\n",
        "    ]),\n",
        "    'val': transforms.Compose([\n",
        "        transforms.Resize(256),\n",
        "        transforms.CenterCrop(224),\n",
        "        transforms.ToTensor(),\n",
        "        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),\n",
        "    ]),\n",
        "}\n",
        "\n",
        "image_datasets = {\n",
        "    x if x == 'train' else 'validation': datasets.ImageFolder(\n",
        "        os.path.join(data_dir, x), data_transforms[x]\n",
        "    )\n",
        "    for x in ['train', 'val']\n",
        "}\n",
        "dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'validation']}\n",
        "class_names = image_datasets['train'].classes\n",
        "\n",
        "dataloaders = {\n",
        "    x: torch.utils.data.DataLoader(image_datasets[x], batch_size=batch_size, shuffle=True)\n",
        "    for x in ['train', 'validation']\n",
        "}\n",
        "\n",
        "def imshow(inp, title=None):\n",
        "    inp = inp.numpy().transpose((1, 2, 0))\n",
        "    mean = np.array([0.485, 0.456, 0.406])\n",
        "    std = np.array([0.229, 0.224, 0.225])\n",
        "    inp = std * inp + mean\n",
        "    inp = np.clip(inp, 0, 1)\n",
        "    plt.imshow(inp)\n",
        "    if title is not None:\n",
        "        plt.title(title)\n"
    ]

    cells.append(md_cell("""## 3. Dataset Loading: Hymenoptera (Ants vs. Bees)
Loading images, applying ImageNet standard normalization, and inspecting a validation batch."""))
    cells.append(robust_cell_8)
    cells.append(orig["cells"][10])  # imshow

    cells.append(md_cell("""## 4. Variational Quantum Circuit Definition
We implement Hadamard state initialization, parameterized $R_Y$ feature embedding, and a sequence of entangling CNOT layers alternating with trainable $R_Y$ rotations."""))
    cells.append(orig["cells"][11])  # H_layer, RY_layer, entangling_layer
    cells.append(orig["cells"][12])  # quantum_net QNode
    cells.append(orig["cells"][13])  # DressedQuantumNet class

    cells.append(md_cell("""## 5. Constructing the Hybrid ResNet-18 Model
We instantiate ResNet-18 with pre-trained ImageNet weights, freeze all convolutional backbone parameters, and replace the final fully-connected layer with `DressedQuantumNet`."""))
    cells.append(orig["cells"][14])  # model_hybrid
    cells.append(orig["cells"][15])  # criterion
    cells.append(orig["cells"][16])  # optimizer
    cells.append(orig["cells"][17])  # scheduler

    cells.append(md_cell("""## 6. Training & Evaluation Loop
Executing hybrid training across epochs, computing validation accuracy, and tracking optimal model weights."""))
    cells.append(orig["cells"][18])  # train_model function
    cells.append(orig["cells"][20])  # model_hybrid training execution

    cells.append(md_cell("""## 7. Model Predictions & Visual Inspection
Visualizing sample predictions on validation images with predicted class labels."""))
    cells.append(orig["cells"][21])  # visualize_model function
    cells.append(orig["cells"][22])  # visualize_model call
    cells.append(orig["cells"][23])  # references

    orig["cells"] = cells
    out_path = NOTEBOOKS_DIR / "04_quantum_transfer_learning.ipynb"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(orig, f, indent=1)
    print(f"Created: {out_path}")


if __name__ == "__main__":
    build_notebook_01()
    build_notebook_02()
    build_notebook_03()
    build_notebook_04()
    print("All notebooks built successfully!")
