# 01. Quantum Computing Foundations & Information Theory

Comprehensive guide covering the theoretical, mathematical, and algorithmic principles of quantum information processing, quantum circuits, and simulation frameworks.

---

## 1. Classical vs. Quantum Information

### 1.1 The Classical Bit
A classical bit is the fundamental unit of classical digital information, constrained deterministically to one of two discrete states in Boolean algebra:

$$b \in \{0, 1\}$$

In classical digital computers, bits are realized physically through microscopic transistor voltages (e.g., $0\,\text{V}$ for low / 0 and $+3.3\,\text{V}$ for high / 1). At any instantaneous moment, a classical system of $n$ bits occupies exactly one out of $2^n$ configurations.

---

### 1.2 The Qubit (Quantum Bit)
A qubit is the basic unit of quantum information. Rather than being confined to discrete binary values, a qubit is a two-level physical quantum system residing in a 2-dimensional complex Hilbert space $\mathcal{H}_2 \cong \mathbb{C}^2$.

By the principle of **quantum superposition**, a qubit state $|\psi\rangle$ can exist as an arbitrary linear combination of the orthonormal computational basis states $|0\rangle$ and $|1\rangle$:

$$|\psi\rangle = \alpha |0\rangle + \beta |1\rangle = \alpha \begin{pmatrix} 1 \\ 0 \end{pmatrix} + \beta \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$$

where $\alpha, \beta \in \mathbb{C}$ are complex probability amplitudes satisfying the normalization constraint:

$$\langle \psi | \psi \rangle = |\alpha|^2 + |\beta|^2 = 1$$

---

### 1.3 Quantum Measurement Postulate & Born's Rule
When a qubit state $|\psi\rangle = \alpha |0\rangle + \beta |1\rangle$ is observed with respect to the computational basis $\{|0\rangle, |1\rangle\}$:
1. The measurement outcome is **inherently probabilistic**.
2. Outcome $0$ is obtained with probability:
   $$P(0) = |\langle 0 | \psi \rangle|^2 = |\alpha|^2$$
3. Outcome $1$ is obtained with probability:
   $$P(1) = |\langle 1 | \psi \rangle|^2 = |\beta|^2$$
4. **State Wavefunction Collapse**: Upon measurement, the state irreversibly collapses into the measured eigenstate ($|0\rangle$ or $|1\rangle$), erasing the prior superposition information.

---

## 2. Geometric Representation: The Bloch Sphere

Because global phase factors $e^{i\gamma}$ carry no observable physical consequence ($|\psi'\rangle = e^{i\gamma}|\psi\rangle \implies |\langle \phi | \psi' \rangle|^2 = |\langle \phi | \psi \rangle|^2$), any normalized single-qubit state can be parameterized by two real angles $\theta \in [0, \pi]$ and $\phi \in [0, 2\pi)$:

$$|\psi\rangle = \cos\left(\frac{\theta}{2}\right) |0\rangle + e^{i\phi} \sin\left(\frac{\theta}{2}\right) |1\rangle$$

```
                   |+z> = |0> (North Pole)
                      |
                      |   / |psi>
                      |  /  theta
                      | /
           -----------+----------- +y
                     /|
                    / |
                  phi |
                 /    |
              +x      |-z> = |1> (South Pole)
```

### Cartesian Bloch Vector Coordinates
Mapping the angles $(\theta, \phi)$ to 3D Euclidean space:

$$\vec{r} = (x, y, z) = \left(\sin\theta \cos\phi, \; \sin\theta \sin\phi, \; \cos\theta\right)$$

Key landmarks on the Bloch Sphere:
- **North Pole** $(0, 0, 1)$: $|0\rangle$ ($\theta = 0$)
- **South Pole** $(0, 0, -1)$: $|1\rangle$ ($\theta = \pi$)
- **Positive X-axis** $(1, 0, 0)$: $|+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}$ ($\theta = \pi/2, \phi = 0$)
- **Negative X-axis** $(-1, 0, 0)$: $|-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}$ ($\theta = \pi/2, \phi = \pi$)
- **Positive Y-axis** $(0, 1, 0)$: $|+i\rangle = \frac{|0\rangle + i|1\rangle}{\sqrt{2}}$ ($\theta = \pi/2, \phi = \pi/2$)
- **Negative Y-axis** $(0, -1, 0)$: $|-i\rangle = \frac{|0\rangle - i|1\rangle}{\sqrt{2}}$ ($\theta = \pi/2, \phi = 3\pi/2$)

---

## 3. Pure States vs. Mixed States & Density Matrices

### 3.1 Statevector Formulation (Pure States)
A quantum state is **pure** if it can be represented by a single ket vector $|\psi\rangle$. A pure state corresponds to a point strictly on the **surface** of the Bloch sphere ($|\vec{r}| = 1$).

---

### 3.2 Density Operator Formulation (Mixed States)
In realistic quantum computing (finite temperature, environmental decoherence, or statistical ensembles), a system may exist in state $|\psi_i\rangle$ with classical probability $p_i$. Such a state is described by the **density matrix** $\rho$:

$$\rho = \sum_{i} p_i |\psi_i\rangle \langle \psi_i|, \quad p_i \ge 0, \quad \sum_i p_i = 1$$

Fundamental properties of valid density matrices:
1. **Hermiticity**: $\rho = \rho^\dagger$
2. **Unit Trace**: $\text{Tr}(\rho) = 1$
3. **Positive Semi-definiteness**: $\langle \phi | \rho | \phi \rangle \ge 0$ for all $|\phi\rangle$

### Purity Criterion
The purity $\gamma$ of a state is defined as:

$$\gamma = \text{Tr}(\rho^2)$$

- If $\gamma = 1$: The state is **pure** (lies on the Bloch sphere surface).
- If $\gamma < 1$: The state is **mixed** (lies in the interior of the Bloch sphere, $|\vec{r}| < 1$).
- Maximally mixed state: $\rho = \frac{1}{2} I = \begin{pmatrix} 0.5 & 0 \\ 0 & 0.5 \end{pmatrix}$, located at the center of the sphere $(0, 0, 0)$ with $\gamma = 0.5$.

### Density Matrix in Bloch Coordinates
$$\rho = \frac{1}{2} \left( I + \vec{r} \cdot \vec{\sigma} \right) = \frac{1}{2} \begin{pmatrix} 1 + z & x - iy \\ x + iy & 1 - z \end{pmatrix}$$

---

## 4. Multi-Qubit Systems & Entanglement

### 4.1 Composite Hilbert Space & Tensor Products
For $n$ qubits, the combined state space is formed by the tensor product:

$$\mathcal{H} = \mathcal{H}_1 \otimes \mathcal{H}_2 \otimes \dots \otimes \mathcal{H}_n \cong \mathbb{C}^{2^n}$$

A general state of $n$ qubits requires $2^n$ complex amplitudes:

$$|\Psi\rangle = \sum_{j=0}^{2^n - 1} c_j |j\rangle, \quad \sum_{j=0}^{2^n - 1} |c_j|^2 = 1$$

This exponential growth ($\dim(\mathcal{H}) = 2^n$) is the core source of quantum computational capacity:
- $n = 10 \implies 1,024$ amplitudes
- $n = 50 \implies \approx 1.12 \times 10^{15}$ amplitudes (exceeding petabyte classical RAM limits)
- $n = 300 \implies$ more dimensions than atoms in the observable universe.

---

### 4.2 Quantum Entanglement & Bell States
A multi-qubit state $|\Psi\rangle$ is **separable** if it can be written as a product of individual subsystem states:

$$|\Psi_{\text{sep}}\rangle = |\psi_1\rangle \otimes |\psi_2\rangle$$

If a state cannot be factored into product states, it is **entangled**:
$$\exists \text{ no } |\psi_1\rangle, |\psi_2\rangle \quad \text{such that} \quad |\Psi\rangle = |\psi_1\rangle \otimes |\psi_2\rangle$$

#### The Four Maximally Entangled Bell States
Constructed using a Hadamard gate $H$ followed by a Controlled-NOT ($CNOT$) gate:

$$|\Phi^+\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}, \qquad |\Phi^-\rangle = \frac{|00\rangle - |11\rangle}{\sqrt{2}}$$
$$|\Psi^+\rangle = \frac{|01\rangle + |10\rangle}{\sqrt{2}}, \qquad |\Psi^-\rangle = \frac{|01\rangle - |10\rangle}{\sqrt{2}}$$

---

## 5. Quantum Logic Gates & Unitaries

All quantum operations on closed quantum systems are linear, reversible transformations represented by **Unitary operators** $U$:

$$U U^\dagger = U^\dagger U = I$$

### 5.1 Single-Qubit Gates

| Gate Name | Symbol | Matrix Representation | Action on Basis States |
| :--- | :---: | :---: | :--- |
| **Pauli-X** (NOT) | $X$ or $\sigma_x$ | $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | $X\|0\rangle = \|1\rangle, \; X\|1\rangle = \|0\rangle$ |
| **Pauli-Y** | $Y$ or $\sigma_y$ | $\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$ | $Y\|0\rangle = i\|1\rangle, \; Y\|1\rangle = -i\|0\rangle$ |
| **Pauli-Z** (Phase Flip) | $Z$ or $\sigma_z$ | $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ | $Z\|0\rangle = \|0\rangle, \; Z\|1\rangle = -\|1\rangle$ |
| **Hadamard** | $H$ | $\frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ | $H\|0\rangle = \|+\rangle, \; H\|1\rangle = \|-\rangle$ |
| **Phase Gate** | $S$ | $\begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$ | $S\|0\rangle = \|0\rangle, \; S\|1\rangle = i\|1\rangle$ |
| **$\pi/8$ Gate** | $T$ | $\begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$ | $T\|0\rangle = \|0\rangle, \; T\|1\rangle = e^{i\pi/4}\|1\rangle$ |

### 5.2 Parameterized Rotation Gates
Continuous rotations around the Cartesian axes of the Bloch Sphere:

$$R_X(\theta) = \exp\left(-i \frac{\theta}{2} X\right) = \begin{pmatrix} \cos(\theta/2) & -i\sin(\theta/2) \\ -i\sin(\theta/2) & \cos(\theta/2) \end{pmatrix}$$

$$R_Y(\theta) = \exp\left(-i \frac{\theta}{2} Y\right) = \begin{pmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{pmatrix}$$

$$R_Z(\theta) = \exp\left(-i \frac{\theta}{2} Z\right) = \begin{pmatrix} e^{-i\theta/2} & 0 \\ 0 & e^{i\theta/2} \end{pmatrix}$$

---

### 5.3 Multi-Qubit Entangling Gates

#### Controlled-NOT Gate ($CNOT$ / $CX$)
Flips target qubit $q_1$ if and only if control qubit $q_0$ is in state $|1\rangle$:

$$CNOT = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

Circuit Diagram:
```
q_0: ──■──
       │
q_1: ──■──
```

---

## 6. Quantum Complexity Classes & Computational Advantages

```
              ┌───────────────────────────────┐
              │           PSPACE              │
              │  ┌─────────────────────────┐  │
              │  │           NP            │  │
              │  │   ┌─────────────────┐   │  │
              │  │   │  BQP (Quantum)  │   │  │
              │  │   │   ┌─────────┐   │   │  │
              │  │   │   │ P / BPP │   │   │  │
              │  │   │   └─────────┘   │   │  │
              │  │   └─────────────────┘   │  │
              │  └─────────────────────────┘  │
              └───────────────────────────────┘
```

- **P**: Problems solvable by a deterministic classical Turing machine in polynomial time $O(n^k)$.
- **BPP**: Problems solvable by a probabilistic classical computer with bounded error probability ($\le 1/3$) in polynomial time.
- **BQP (Bounded-error Quantum Polynomial-Time)**: Problems solvable by a polynomial-size quantum circuit with error probability at most $1/3$.
- **NP**: Decision problems whose positive solutions can be verified in polynomial time.

### Canonical Quantum Speedups
1. **Deutsch-Jozsa Algorithm**: Determines if a function $f: \{0, 1\}^n \to \{0, 1\}$ is constant or balanced in **$1$ query** (exponentially faster than classical worst-case $2^{n-1} + 1$).
2. **Bernstein-Vazirani Algorithm**: Recovers an $n$-bit secret string $s$ from an oracle $f(x) = s \cdot x \pmod 2$ in **$1$ query** (classical requires $n$ queries).
3. **Simon's Algorithm**: Discovers hidden period $s$ for function $f(x) = f(x \oplus s)$ in $O(n)$ queries (exponential speedup over classical $O(2^{n/2})$).
4. **Grover's Search Algorithm**: Searches an unstructured database of $N$ items in $O(\sqrt{N})$ queries (quadratic speedup over classical $O(N)$).
5. **Shor's Factoring Algorithm**: Factors an $n$-bit integer in $O(n^3)$ polynomial time using Quantum Phase Estimation / QFT (exponential speedup over best classical General Number Field Sieve).

---

## 7. Quantum Software Ecosystems

### 7.1 Qiskit (IBM)
- **Primary Focus**: Gate-level circuit compilation, pulse-level control, OpenQASM specification, noise modeling, and IBM Quantum hardware execution.
- **Key Modules**: `qiskit.circuit`, `qiskit.quantum_info`, `qiskit_aer` (high-performance C++ simulator).

### 7.2 PennyLane (Xanadu)
- **Primary Focus**: Quantum Differentiable Programming, hybrid Quantum-Classical Machine Learning (QML), hardware-agnostic execution.
- **Integration**: Seamless autograd with PyTorch, TensorFlow, and JAX.
- **Gradient Engines**: Parameter-Shift Rule, Finite Differences, Adjoint Differentiation.

### 7.3 Bloqade (QuEra Computing)
- **Primary Focus**: Neutral atom analog quantum simulation and Aquila QPU cloud execution.
- **Paradigm**: Continuous Hamiltonian evolution with optical tweezers and laser pulse schedules.
