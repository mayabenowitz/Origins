# The Quantum Origins of the Universe
[![status: active](https://github.com/GIScience/badges/raw/master/status/active.svg)](https://github.com/GIScience/badges#active)
![materials: public](https://img.shields.io/badge/Materials-Public-green.svg)
![GitHub issues open](https://img.shields.io/github/issues/mayabenowitz/Origins)
![GitHub issues closed](https://img.shields.io/github/issues-closed/mayabenowitz/Origins)
![Contributors](https://img.shields.io/github/contributors/mayabenowitz/Origins?logoColor=green&style=social)
![Twitter](https://img.shields.io/twitter/follow/cosmicfibretion?style=social)


 Is quantum mechanics universal? Is the entire universe a unified quantum object? Everett's work on the foundations of quantum theory, *The Theory of the Universal Wavefunction*, has been described by Max Jammer, a philosopher of science, as "**one of the most daring and most ambitious theories ever constructed in the history of science**." The goal of this research program is to take Everett's principle of quantum universality to heart and make the audacious leap from quantum mechanics in the laboratory frame to the universe as a whole to understand its origins. The dream is bigger still. For if we truly understood our cosmic origins---the separation between science and spirituality would collapse---and humanity would finally be able to *define* God (or Source). Perhaps then humanity could finally heal and give birth to a New Earth. 

~~Paper 1: [On the Origins of the Universe and the Nature of the Cosmological Singularity](https://github.com/mayabenowitz/Origins/blob/main/manuscript/foundations_of_quantum_universality_Final_v1_0%20(1).pdf)~~

~~Paper 2: [The Everettian Conformal Bootstrap](https://github.com/mayabenowitz/Origins/blob/main/manuscript/everettian_conformal_bootstrap_PRL.pdf)~~

Paper 3 (Final): [The Theory of the Initial Conditions](https://github.com/mayabenowitz/Origins/blob/main/manuscript/the_theory_of_the_initial_conditions_07042026.pdf)

## Abstract

We revisit old ideas with a modern perspective and approach quantum cosmology from a quantum information-theoretic starting point. Our view is that the leap from quantum mechanics in the laboratory frame to the universe as a whole is key to understanding its origins. The problem of the external observer and the conflict of principle between unitarity, causality, and diffeomorphism invariance are explored in bubble nucleation theories. We argue causality is fundamentally incompatible with the assumption that the universe has no external observer. A unique closed-form cosmological wavefunction describing the probability amplitude of the initial state of bubble/antibubble nucleation events is derived. The wavefunction vanishes at the initial singular state, yielding numerous observable consequences. We propose a CMB double-slit experiment to test the theory.
 
## Key Result: Quantum Cosmology from the Top Down

1. There is no external observer who prepared the initial state of the cosmos.
2. The *form* of the laws of physics does not change with scale.
3. The universal wavefunction $\Psi$ exists and contains all physical information of the universe.
4. $\Psi$ obeys the timeless Schrödinger equation,

   
   $\hat{H}\Psi = 0$
   

   on all scales. Nature has no fundamental scale: $\Psi$ is scale-invariant. Only dimensionless quantities are fundamental.
5. The universal wavefunction is a 2-spinor $\Psi$ that lives in the Hilbert space of states
   $L^2[\mathbb{C}P^1(2,2,2)] \otimes \mathbb{C}^2$, where
   $\mathbb{C}P^1(2,2,2)$ is the **surface of the initial data** with $\Psi$ assigning a non-zero probability amplitude to every possible initial nucleated state of a bubble and antibubble.

### Solution

```math
\hat{H} = -\partial_a^2 I + \frac{\phi}{\pi a^2}\left(\frac{\phi}{\pi}I + \sigma_3\right) \qquad\qquad \Psi(a,\phi) = \begin{pmatrix} (1 + e^{-i\phi})a^{-\phi/\pi} \\ (1 + e^{i\phi})a^{\phi/\pi} \end{pmatrix}
```

Here $a$ is the cosmological scale factor, $I$ is the 2x2 identity matrix, $\sigma_3$ is a Pauli matrix, and $\beta = \cot({\phi/2}) = 1/T$ is the inverse temperature of the initial nucleated state. At the initial singularity where $\beta = 0$, we have $\phi = \pi$ with $\Psi = 0$. *It is of profound mathematical beauty that $\Psi = 0$ uniquely at the initial singularity $\phi = \pi$ by Euler's identity.*

The **surface of the initial data** or **vacuum orbifold** is defined as

$$ \mathbb{C}P^1(2, 2, 2) := {(e^{i\theta}, e^{i\phi}) \mid 0 \leq \theta < 2\pi, \ 0 \leq \phi < 2\pi } \cong (S_a^1 \times S_\beta^1) \dslash_{\text{ref}} \ \mathbb{Z}_2 \in \mathbb{C}^2$$

with the conformally flat metric

$$ ds^2 = d\theta^2 + d\phi^2 $$

where all the curvature concentrates and diverges at the following fixed points from the $\mathbb{Z}_2$ quotient,

$$ (\theta, \phi) = (\pi, \pi), \ \ (\pi, 0), \ \ (0, 0). $$

Modulo the $\mathbb{Z}_2$, the surface of the initial data is a conformal Clifford torus. With the reflective $\mathbb{Z}_2$, the topology is a flat sphere with the above order-2 conical singularities. Specifically, $\mathbb{C}P^1(2,2,2)$ is a flat Riemann sphere with a reflective $\mathbb{Z}_2$ quotient.