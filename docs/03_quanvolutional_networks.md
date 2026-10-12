# 03. Quanvolutional Neural Networks (QuanvNN) for Medical Imaging

Comprehensive guide covering the theory of Quanvolutional Neural Networks, spatial quantum transformations, angle embedding, random circuit entanglers, and benchmark classification on BreastMNIST.

---

## 1. Classical Convolutions vs. Quantum Convolutions

### 1.1 The Classical Convolutional Layer
In classical Deep Learning, a 2D convolutional layer computes local spatial dot products between an input image feature map $\mathbf{X}$ and a learnable linear kernel filter $\mathbf{W} \in \mathbb{R}^{K \times K}$:

$$y(j, k) = \sigma\left( \sum_{m=0}^{K-1} \sum_{n=0}^{K-1} W(m, n) X(j \cdot s + m, \; k \cdot s + n) + b \right)$$

where $s$ is the spatial stride and $\sigma$ is an activation function (e.g., ReLU).
While highly expressive when stacked into deep hierarchies, each classical layer is fundamentally a linear affine transformation followed by a point-wise scalar non-linearity.

---

### 1.2 The Quanvolutional Layer (Henderson et al., 2020)
**Quanvolution** replaces the classical linear filter dot product with a **parameterized or random quantum circuit** acting on local spatial pixel patches:

```
[ Input Image Patch (2x2) ]
     [ p0, p1 ]
     [ p2, p3 ]
         │
         ▼
[ Angle Embedding: RY(pi * pj) on 4 Qubits ]
         │
         ▼
[ Random Quantum Entangling Circuit (RandomLayers) ]
         │
         ▼
[ Measure Pauli-Z Expectation Values <Z_0>, <Z_1>, <Z_2>, <Z_3> ]
         │
         ▼
[ 4-Channel Output at Spatial Coordinate (j/2, k/2) ]
```

### Why Quanvolution?
1. **Exponential Hilbert Space Projection**: A $2 \times 2$ pixel patch ($4$ numbers) is mapped into a $2^4 = 16$-dimensional complex Hilbert space.
2. **Non-linear Kernel Trick**: Quantum entanglement and unitary rotations induce non-linear feature representations that cannot be factored into independent pixel non-linearities.
3. **Hardware Accessibility in the NISQ Era**: Instead of needing hundreds of error-corrected qubits to load an entire $28 \times 28$ or $224 \times 224$ image at once, Quanvolution only requires **4 physical qubits** evaluated repeatedly across local patches!

---

## 2. Mathematical Formulation of the Quanvolution Circuit

### 2.1 Receptive Field Extraction & Normalization
Given an image $\mathbf{I} \in [0, 1]^{H \times W \times 1}$, we slide a $2 \times 2$ window with stride $s = 2$.
At each window location $(j, k)$, we extract 4 pixel values:

$$\mathbf{p} = [p_0, p_1, p_2, p_3]^T = [I_{j, k}, \; I_{j, k+1}, \; I_{j+1, k}, \; I_{j+1, k+1}]^T$$

---

### 2.2 Quantum State Preparation (Angle Embedding)
Each qubit $j \in \{0, 1, 2, 3\}$ is initialized in the computational ground state $|0\rangle$.
We apply a rotation around the $Y$-axis proportional to the normalized pixel intensity $p_j$:

$$|\psi_{\text{in}}(\mathbf{p})\rangle = \bigotimes_{j=0}^{3} R_Y(\pi p_j) |0\rangle$$

where:
$$R_Y(\pi p_j) = \begin{pmatrix} \cos\left(\frac{\pi p_j}{2}\right) & -\sin\left(\frac{\pi p_j}{2}\right) \\ \sin\left(\frac{\pi p_j}{2}\right) & \cos\left(\frac{\pi p_j}{2}\right) \end{pmatrix}$$

- If $p_j = 0$ (black pixel): $R_Y(0)|0\rangle = |0\rangle$ (state points North).
- If $p_j = 1$ (white pixel): $R_Y(\pi)|0\rangle = |1\rangle$ (state points South).
- Intermediate values map smoothly along the meridian of the Bloch sphere.

---

### 2.3 Unitary Entangling Layers (`RandomLayers`)
To mix the spatial information across all 4 pixels in the receptive field, we apply a parameterized multi-qubit unitary operator $U(\vec{\theta})$:

$$|\psi_{\text{out}}\rangle = U(\vec{\theta}) |\psi_{\text{in}}(\mathbf{p})\rangle$$

The `RandomLayers` template applies alternating single-qubit rotations and entangling two-qubit gates (such as $CNOT$):
$$U(\vec{\theta}) = \prod_{l=1}^{L} \left( \prod_{(a, b) \in \text{pairs}} CNOT_{a, b} \right) \left( \bigotimes_{q=0}^{3} R(\vec{\theta}_{l, q}) \right)$$

---

### 2.4 Observable Measurement & Feature Mapping
We perform projective measurements of the Pauli-$Z$ operator on each of the 4 qubits:

$$q_c(j/2, k/2) = \langle \psi_{\text{out}} | \hat{Z}_c | \psi_{\text{out}} \rangle \in [-1, 1], \quad c \in \{0, 1, 2, 3\}$$

Because the stride is $s=2$:
- Input spatial dimensions: $H = 28, \; W = 28$
- Output spatial dimensions: $H' = 28/2 = 14, \; W' = 28/2 = 14$
- Output channels: $C' = 4$
- Resulting feature tensor shape: $(14, 14, 4)$

---

## 3. Medical Dataset: BreastMNIST

The **BreastMNIST** dataset is part of the standardized MedMNIST biomedical benchmark:
- **Modality**: 2D Breast Ultrasound images.
- **Task**: Binary classification (0: Benign / Normal, 1: Malignant).
- **Resolution**: $28 \times 28$ pixels, grayscale.
- **Clinical Significance**: Early detection of malignant lesions in ultrasound imaging with low computational overhead.

---

## 4. Hybrid Classifier Architecture & Comparative Analysis

```
Quanvolved Features (14x14x4 = 784) ───> [ Flatten Layer ] ───> [ Dense Softmax Layer (num_classes) ] ───> Predictions
```

### 4.1 Downstream Model Architecture
Both models share the exact same downstream classical architecture:
1. `Flatten()`: Unrolls input tensors into 1D vectors.
2. `Dense(num_classes, activation="softmax")`: Linear classification head.
3. Loss function: Sparse Categorical Cross-Entropy:
   $$\mathcal{L} = -\sum_{i=1}^M \log P(y_i | \mathbf{x}_i)$$

### 4.2 Benchmark Comparison
1. **Model With Quantum Preprocessing**:
   Trained on the 4-channel quanvolved representations $(14, 14, 4)$.
2. **Model Without Quantum Preprocessing**:
   Trained directly on the raw normalized pixel inputs $(28, 28, 1)$.

### Empirical Findings:
- The non-linear feature maps generated by the quantum circuit preserve key structural edge and contrast boundaries while compressing spatial resolution.
- The quantum layer provides enhanced initial separability, enabling competitive or superior validation trajectories with minimal classical trainable parameters.
