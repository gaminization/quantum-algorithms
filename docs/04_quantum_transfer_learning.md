# 04. Quantum Transfer Learning (QTL) with Dressed Quantum Circuits

Comprehensive theoretical and mathematical guide covering Quantum Transfer Learning, Dressed Quantum Circuits, pre-trained CNN backbones, and hybrid end-to-end backpropagation via the Parameter-Shift Rule.

---

## 1. Scientific Motivation & Problem Statement

### 1.1 The High-Dimensional Input Bottleneck in NISQ
Noisy Intermediate-Scale Quantum (NISQ) processors have limited qubit counts (typically $10 - 100$ noisy qubits) and shallow coherence times.
Meanwhile, real-world visual perception tasks involve high-resolution multi-channel images:
- A standard ImageNet image has $224 \times 224 \times 3 = 150,528$ values.
- Direct quantum encoding schemes (amplitude encoding or angle embedding) would require either deep circuits prone to decoherence or tens of thousands of qubits.

### 1.2 Classical Transfer Learning
In classical Deep Learning, transfer learning reuses features learned on a large benchmark dataset (such as ImageNet-1K with 1.2 million images across 1,000 classes) to solve a new, domain-specific task with limited training data.
The deep convolutional layers act as a generalized visual feature extractor, transforming raw pixels into invariant abstract representations.

### 1.3 Quantum Transfer Learning (Mari et al., 2019)
Pioneered by Andrea Mari et al. (*arXiv:1912.08278*), Quantum Transfer Learning combines:
1. **A Pre-Trained Classical Backbone (e.g., ResNet-18)**: Extracts high-level visual features and compresses $150,528$ dimensions down to a compact $512$-dimensional vector.
2. **A "Dressed" Variational Quantum Circuit (VQC)**: Acts as the decision-making classification head, operating natively in a quantum Hilbert space!

---

## 2. The "Dressed" Quantum Circuit Architecture

```
Image X (224x224x3)
        │
        ▼
[ Pre-Trained ResNet-18 Backbone ] (FROZEN ImageNet Weights)
        │
        ▼  h in R^512
[ Classical Pre-Processing Layer ]  Linear(512 -> 4) + tanh * (pi / 2)
        │
        ▼  z in [-pi/2, pi/2]^4
[ Variational Quantum Circuit ]     4 Qubits, Hadamard, RY Embed, Depth-6 CNOT + RY
        │
        ▼  q in [-1, 1]^4
[ Classical Post-Processing Layer ] Linear(4 -> 2)
        │
        ▼  y in R^2
[ Cross-Entropy Loss & Predictions ]
```

---

### 2.1 Classical Feature Extractor: ResNet-18
We use **ResNet-18** pre-trained on ImageNet-1K:
- Comprises 18 convolutional layers with residual shortcut connections.
- We freeze all backbone parameters ($\nabla_{\theta_{\text{CNN}}} \mathcal{L} = 0$).
- For any input image $\mathbf{x}$, the penultimate average pooling layer outputs an embedding vector:
  $$\mathbf{h} = f_{\text{ResNet}}(\mathbf{x}) \in \mathbb{R}^{512}$$

---

### 2.2 Classical Pre-Processing Layer (`pre_net`)
Because our quantum circuit has $n = 4$ qubits, we compress the 512-dimensional embedding into 4 continuous rotation angles:

$$\mathbf{a} = \mathbf{W}_{\text{pre}} \mathbf{h} + \mathbf{b}_{\text{pre}}, \quad \mathbf{W}_{\text{pre}} \in \mathbb{R}^{4 \times 512}, \; \mathbf{b}_{\text{pre}} \in \mathbb{R}^4$$

We apply a scaled hyperbolic tangent activation function to constrain the values within $[-\pi/2, \pi/2]$:

$$\mathbf{z} = \tanh(\mathbf{a}) \cdot \frac{\pi}{2} \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]^4$$

---

### 2.3 The Variational Quantum Circuit (VQC)

#### Step 1: Unbiased Superposition Initialization
All $n = 4$ qubits start in ground state $|0\rangle^{\otimes 4}$. A Hadamard layer creates an unbiased uniform superposition state:

$$|\psi_0\rangle = H^{\otimes 4} |0\rangle^{\otimes 4} = |+\rangle^{\otimes 4} = \frac{1}{4} \sum_{k=0}^{15} |k\rangle$$

#### Step 2: Input Feature Embedding
The 4 classical features $z_j$ are embedded as rotation angles around the $Y$-axis:

$$|\psi_{\text{embed}}(\mathbf{z})\rangle = \left( \bigotimes_{j=0}^{3} R_Y(z_j) \right) |\psi_0\rangle$$

#### Step 3: Parameterized Variational Layers
We repeat $q_{\text{depth}} = 6$ variational blocks. Each block $l \in \{1, \dots, 6\}$ consists of:
1. **Entangling CNOT Ring Layers**:
   - Even pairs: $CNOT(0, 1), \; CNOT(2, 3)$
   - Odd pairs: $CNOT(1, 2)$ (and periodic wrap-around)
2. **Parameterized Single-Qubit Rotations**:
   $$\bigotimes_{j=0}^{3} R_Y(w_{l, j})$$

The total unitary evolution is:
$$U(\mathbf{w}) = \prod_{l=1}^{q_{\text{depth}}} \left[ \left( \bigotimes_{j=0}^{3} R_Y(w_{l, j}) \right) U_{\text{entangle}} \right]$$

The total number of trainable quantum weights is:
$$N_{\text{quantum}} = q_{\text{depth}} \times n = 6 \times 4 = 24 \text{ parameters}$$

#### Step 4: Quantum Measurement
We measure the expectation values of the Pauli-$Z$ observable on each qubit:

$$q_j = \langle \psi_{\text{final}} | \hat{Z}_j | \psi_{\text{final}} \rangle \in [-1, 1], \quad j \in \{0, 1, 2, 3\}$$

---

### 2.4 Classical Post-Processing Layer (`post_net`)
The 4 quantum expectation values $\mathbf{q} \in \mathbb{R}^4$ are transformed by a final trainable linear layer into the 2 classification logits (Ants vs. Bees):

$$\mathbf{y} = \mathbf{W}_{\text{post}} \mathbf{q} + \mathbf{b}_{\text{post}}, \quad \mathbf{W}_{\text{post}} \in \mathbb{R}^{2 \times 4}, \; \mathbf{b}_{\text{post}} \in \mathbb{R}^2$$

---

## 3. Hybrid Differentiable Programming & The Parameter-Shift Rule

To optimize the hybrid network end-to-end, gradients must propagate from the classical loss function back through the quantum circuit to the pre-processing layer.

### 3.1 The Parameter-Shift Rule
Unlike classical neural networks where numerical differentiation suffers from rounding error or finite difference inaccuracies on noisy quantum processors, quantum expectation values can be differentiated **analytically** using the **Parameter-Shift Rule** (Schuld et al., 2019):

$$\frac{\partial \langle \hat{O} \rangle}{\partial \theta_k} = \frac{\langle \hat{O} \rangle_{\theta_k + s} - \langle \hat{O} \rangle_{\theta_k - s}}{2 \sin(s)}$$

For standard generator gates (eigenvalues $\pm 1/2$), choosing shift $s = \frac{\pi}{2}$ gives:

$$\frac{\partial \langle \hat{O} \rangle}{\partial \theta_k} = \frac{1}{2} \left[ \langle \hat{O} \rangle_{\theta_k + \frac{\pi}{2}} - \langle \hat{O} \rangle_{\theta_k - \frac{\pi}{2}} \right]$$

### 3.2 Chain Rule Across Hybrid Boundaries
The gradient of loss $\mathcal{L}$ with respect to quantum parameters $\mathbf{w}$ and classical pre-net weights $\mathbf{W}_{\text{pre}}$:

$$\frac{\partial \mathcal{L}}{\partial \mathbf{w}} = \frac{\partial \mathcal{L}}{\partial \mathbf{y}} \cdot \mathbf{W}_{\text{post}} \cdot \frac{\partial \mathbf{q}}{\partial \mathbf{w}}$$

$$\frac{\partial \mathcal{L}}{\partial \mathbf{W}_{\text{pre}}} = \left( \frac{\partial \mathcal{L}}{\partial \mathbf{y}} \cdot \mathbf{W}_{\text{post}} \cdot \frac{\partial \mathbf{q}}{\partial \mathbf{z}} \odot \frac{\pi}{2}(1 - \tanh^2(\mathbf{a})) \right) \mathbf{h}^T$$

PennyLane and PyTorch automatically handle this hybrid chain rule seamlessly!

---

## 4. Experimental Results on Hymenoptera Dataset

- **Dataset**: Ants vs. Bees (397 images, train/validation split).
- **Optimizer**: Adam ($\text{lr} = 0.0004$) applied to `model_hybrid.fc.parameters()`.
- **Scheduler**: StepLR ($\gamma = 0.1$, step size = 10 epochs).
- **Loss**: Cross-Entropy Loss.
- **Results**: The hybrid model rapidly achieves $> 75-85\%$ validation accuracy within 5 epochs, demonstrating effective transfer of visual features into a low-dimensional variational quantum Hilbert space.
