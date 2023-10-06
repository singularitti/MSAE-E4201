# Homework 1

[TOC]

## Problem 1

### First assumption

Build $2$ Cartesian coordinate systems $\Gamma$ and $\Gamma'$ for cubic lattice and $2$
cocentric spheres, respectively. The assumption here is the origin $O'$ of the $2$ cocentric
spheres is coincided with the origin $O$ of the simple cubic lattice. Then we need to solve
$$
50^2 \leq (x - 0)^2 + (y-0)^2+(z-0)^2 \leq 60^2, \text{where } x, y, z \text{ are even numbers,}
$$
here $(x, y, z)$ is one vertex of the lattice, under either $\Gamma$ and $\Gamma'$ (because
they are same, since $O = O'$).

Also, we need $O$ is exactly located at one vertex of the lattice. Up till now, we assume
all the atoms are point particles.

```c++
#include <iostream>
#include <cmath>

int main() {
    double x, y, z, v, l_square, i = 0;
  
    for (x = -60; x <= 60; x += 2) {
        for (y = -60; y <= 60; y += 2) {
            for (z = -60; z <= 60; z += 2) {
                l_square = pow(x, 2.0) + pow(y, 2.0) + pow(z, 2.0);
                if (2500 <= l_square && l_square <= 3600) i += 1;
            }
        }
    }
    printf("%f", i);
}
```

The result is $47964$.

If the assumption is not true, then we have to consider the lattice origin is not
$(0, 0, 0)$ under $\Gamma'$, but $(x_c, y_c, z_c)$. Still, $O$ is exact located at one
vertex of the lattice (to make life simpler). So we have to build a linear map
$\mathcal{T}$ s.t.
$$
\begin{align}
\mathcal{T} &\colon \Gamma \rightarrow \Gamma' \\
\mathcal{T} &\colon (x, y, z) \mapsto (x - x_c, y - y_c, z- z_c),
\end{align}
$$
as you see, $\mathcal{T}$ translates a coordinate $(x, y, z)$ under $\Gamma$ to $\Gamma'$,
like $\mathcal{T}(x_c, y_c, z_c) = (0, 0, 0)$. So the problem becomes
$$
50^2 \leq (x - x_c)^2 + (y-y_c)^2+(z-z_c)^2 \leq 60^2,
$$
where $x_c \in [0, 2)$, $y_c \in [0, 2)$, $z_c \in [0, 2)$. I tried to write code like this

```c++
#include <iostream>
#include <cmath>

int main() {
    double x, y, z, v, l_square, i = 0;
    double xp, yp, zp;
    for (xp = 0; xp < 2; xp += 0.01) {
        for (yp = 0; yp < 2; yp += 0.01) {
            for (zp = 0; zp < 2; zp += 0.01) {
                for (x = -60 + xp; x <= 60 + xp; x += 2) {
                    for (y = -60 + yp; y <= 60 + yp; y += 2) {
                        for (z = -60 + zp; z <= 60 + zp; z += 2) {
                            l_square = pow(x - xp, 2.0) + pow(y - yp, 2.0) + pow(z - zp, 2.0);
                            if (2500 <= l_square && l_square <= 3600) i += 1;
                        }
                    }
                }
            }
        }
    }
    printf("%f", i);
}
```

But it took too long time to solve, and theoretically, $0.01$ for one step is still coarse.

### Second assumption

We can make further assumptions that atoms are not particles, with average volume $2^3$, the
volume of the interspace of $2$ spheres is
$$
V = \frac{4}{3}\pi (60^3 - 50^3),
$$
so it can contain almost $ \frac{ 4\pi }{ 3 }\times (60^3-50^3)/2^3 \approx 47647$ atoms.

## Problem 2

For an adiabatic process,
$$
dU = \delta Q - pdV = -pdV.
$$
Since
$$
U = A p^2 V,
$$
then
$$
dU = -pdV = Ap^2dV +  2p A Vdp.
$$
Then

$$
\begin{align}
-(A p^2 +p) dV &= 2 A V p dp,\\
-\frac{1}{2AV} dV &= \frac{p}{Ap^2 + p} dp,\\
\Rightarrow V &= \frac{C}{(1+Ap)^{2}},
\end{align}
$$
Where $C$ is a constant.
