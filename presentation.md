---
marp: true
paginate: true
theme: default
math: true
---

# `rosnet`
#### A Block Tensor Algebra Library for Out-of-Core Quantum Computing Simulation
<center>
Sergio Sánchez Ramírez

sergio.sanchez.ramirez@bsc.es

BSC - QUANTIC
</center>

---

# Bit

- 2 states
- discrete

![bg right](media/videos/animations/1080p30/BitDistribution_ManimCE_v0.15.2.gif)

---

# Pbit

- _probabilistic bit_
  <!-- - pr. distribution over a _bit_ -->
- 2 probable events: $0$ and $1$

$$ \Pr(0) = \alpha ~~~~~~ \Pr(1) = \beta $$

$$ \alpha + \beta = 1 $$

![bg left](media/videos/animations/1080p30/PbitDistribution_ManimCE_v0.15.2.gif)

---

# Qubit

![bg right](media/videos/animations/1080p30/BlochSphereXRotation_ManimCE_v0.15.2.gif)

$$ \vec{\psi} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix} = \alpha \vec{\mathfrak{0}} + \beta \vec{\mathfrak{1}} ~~ \textsf{where} ~~ \alpha, \beta \in \Complex$$

$$ \vec{\mathfrak{0}} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} ~~~~ \vec{\mathfrak{1}} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$


_Born's rule_
 $$
 \Pr(\vec{\mathfrak{0}} \mid \vec{\psi}) = \lVert\alpha\rVert^2 \\
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

# Quantum state

-