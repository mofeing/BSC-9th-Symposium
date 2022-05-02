---
marp: true
paginate: true
theme: default
math: true
---
<style>
#title {
  text-align: center;
}
</style>

<h1 id="title">
rosnet
</div>

#### A Block Tensor Algebra Library for Out-of-Core Quantum Computing Simulation
<center>
Sergio Sánchez Ramírez

sergio.sanchez.ramirez@bsc.es

BSC - QUANTIC
</center>

---

# Bit

- System of 2 states
- Discrete

![bg right](media/videos/animations/1080p30/BitDistribution_ManimCE_v0.15.2.gif)

---

# Pbit

- _Probabilistic bit_
- 2 possible events: $\mathfrak{0}$ and $\mathfrak{1}$

$$ \Pr(\mathfrak{0}) = \alpha ~~~~~~ \Pr(\mathfrak{1}) = \beta $$

$$ \alpha + \beta = 1 $$

![bg left](media/videos/animations/1080p30/PbitDistribution_ManimCE_v0.15.2.gif)

---

# Qubit

![bg right](media/videos/animations/1080p30/BlochSphereXRotation_ManimCE_v0.15.2.gif)

$$ \vec{\psi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \alpha \vec{\mathfrak{0}} + \beta \vec{\mathfrak{1}} ~~ \textsf{where} ~~ \alpha, \beta \in \Complex$$

$$ \vec{\mathfrak{0}} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} ~~~~ \vec{\mathfrak{1}} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$


_Born's rule_
 $$
 \Pr(\vec{\mathfrak{0}} \mid \vec{\psi}) = \lVert \vec{\mathfrak{0}} \cdot \vec{\psi} \rVert^2 = \lVert\alpha\rVert^2 \\
 \Pr(\vec{\mathfrak{1}} \mid \vec{\psi}) = \lVert\beta\rVert^2
 $$

---

$$ \vec{+} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \end{pmatrix} ~~~~ \vec{-} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -1 \end{pmatrix} $$

$$ \vec{⇑} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ i \end{pmatrix} ~~~~ \vec{⇓} = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -i \end{pmatrix} $$

---

$$ X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} $$

![bg left](media/videos/animations/1080p30/BlochSphereXRotation_ManimCE_v0.15.2.gif)

---

$$ Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} $$

---

# Composite systems
### What if we have 2 qubits?

Possible measurements are
$$ (\mathfrak{\vec{0}, \vec{0}}),~ (\mathfrak{\vec{0}, \vec{1}}),~ (\mathfrak{\vec{1}, \vec{0}}) ~\text{or}~ (\mathfrak{\vec{1}, \vec{1}}) $$

And so we can represent the quantum state that represents the probability distribution of each possible outcome,
$$ \vec{\psi} = \begin{pmatrix}
  \alpha_{00} \\
  \alpha_{01} \\
  \alpha_{10} \\
  \alpha_{11}
\end{pmatrix} ~~\mapsto~~ \Pr\left(i,j \mid \vec{\psi}\right) = \lVert\alpha_{i,j}\rVert^2 $$

---

# 2-qubit gates

$$ CNOT = CX = \left(\begin{array}{cc|cc}
  1 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 \\ \hline
  0 & 0 & 0 & 1 \\
  0 & 0 & 1 & 0
\end{array}\right)
$$

---

If both qubits/systems are **independent**, then
$$
\vec{\psi} = \vec{a} \otimes \vec{b} = \begin{pmatrix}
  a_0 b_0 \\
  a_0 b_1 \\ \hline
  a_1 b_0 \\
  a_1 b_1
\end{pmatrix} \begin{cases}
  \vec{a} = \begin{pmatrix} a_0 \\ a_1 \end{pmatrix} \\
  \\
  \vec{b} = \begin{pmatrix} b_0 \\ b_1 \end{pmatrix}
\end{cases}
$$

---

If both qubit/systems are **correlated**, then
$$
\vec{\psi} = \sum_{i,j} \lambda_{i,j} ~ \left( \vec{\mathfrak{i}} \otimes \vec{\mathfrak{j}} \right)
$$

---

$$ \mathcal{O}(2^n) $$

| \# qubits | size        |
| --------- | ----------- |
| 10        | 8 KiB       |
| 20        | 8 MiB       |
| 30        | 8 GiB       |
| 40        | 8 TiB       |
| **45**    | **256 TiB** |

---

# Tensors

- Generalization of linear objects into higher "dimensions" <small>(_order_ is a better term)</small>
  - _n_-dimensional arrays
- Graphical notation

---

<style>
</style>

![width:80%](static/tensor-notation-1.jpg)

<footer>
Source: Tai-Danae Bradley (math3ma.com/blog/matrices-as-tensor-network-diagrams)
</footer>

---

![width:80%](static/tensor-notation-2.jpg)

<footer>
Source: Tai-Danae Bradley (math3ma.com/blog/matrices-as-tensor-network-diagrams)
</footer>

---

![width:80%](static/tensor-notation-3.jpg)

<footer>
Source: Tai-Danae Bradley (math3ma.com/blog/matrices-as-tensor-network-diagrams)
</footer>

---

![width:80%](static/tensor-notation-4.jpg)

<footer>
Source: Tai-Danae Bradley (math3ma.com/blog/matrices-as-tensor-network-diagrams)
</footer>

---

# Tensor Networks

- Graph of tensors