# Homework 3

[TOC]

## Problem 1

1. For
  $$
  S = N R \ln \Big( \frac{U V}{N^2 R \theta v_0} \Big), \label{eq:s}
  $$

  $$
  S(\lambda U, \lambda V, \lambda N) = \lambda N R \ln \Big( \frac{\lambda ^2 UV}{\lambda^2 N ^2 R \theta v_0} \Big) = \lambda S(U, V, N).
  $$
  And
  $$
  \Big( \frac{\partial S}{\partial U} \Big)_{V, N} = \frac{N R}{U} > 0 \; \text{ for any } U >0.
  $$
  Finally,
  $$
  \Big( \frac{\partial U}{\partial S} \Big)_{V, N} = \frac{U}{N R} = T,
  $$
  Substitue into $\eqref{eq:s}$ we derive
  $$
  S = \frac{U}{T} \ln \Big( \frac{T V}{N \theta v_0} \Big)
  $$
  When $\displaystyle \lim_{T \rightarrow 0} S = -\infty$ but not $0$. So it is not a valid fundamental equation.

2. If we substitute $S' = \lambda S$, $N' = \lambda N$, $U' = \lambda U$, $V' = \lambda V$, the equation should remain the same, let's check:

  $$
  \lambda U = \Big( \frac{v_0 \theta}{R} \Big) \frac{\lambda^2 S^2}{\lambda V} \exp \Big( \frac{\lambda S}{\lambda N R} \Big). \label{eq:1-b}
  $$

  It's obvious $\eqref{eq:1-b}$ reduces to
  $$
  U = \Big( \frac{v_0 \theta}{R} \Big) \frac{S^2}{V} \exp \Big( \frac{S}{N R} \Big),
  $$
  so criteria i holds.

  Since
  $$
    \Big( \frac{\partial U}{\partial S} \Big)_{V, N} = \Big( \frac{v_0 \theta}{R} \Big) \frac{S}{V} \exp\Big(\frac{S}{N R}\Big) \Big( 2 + \frac{S}{N R} \Big) > 0 \; \text{ for positive } S, V, N,
  $$

  so $\big( \frac{\partial S}{\partial U} \big)_{V, N}  > 0$ also.

  At $T = 0$, i.e.,
  $$
  \Big( \frac{\partial U}{\partial S} \Big)_{V, N} = \Big( \frac{v_0 \theta}{R} \Big) \frac{S}{V} \exp\Big(\frac{S}{N R}\Big) \Big( 2 + \frac{S}{N R} \Big) = 0, \label{eq:1-bus}
  $$
  $\eqref{eq:1-bus}$ only comes true when $S = 0$. So it is a valid fundamental equation.

3. Since

  $$
  S = \Big( \frac{R}{\theta^2} \Big)^{\frac{1}{3}} \Big( \frac{N U}{V} \Big)^{\frac{2}{3}},
  $$

  $$
  S(\lambda U, \lambda V, \lambda N) = \Big( \frac{R}{\theta^2} \Big)^{\frac{1}{3}} \lambda^{\frac{2}{3}} \Big( \frac{N U}{V} \Big)^{\frac{2}{3}},
  $$
  so it violates criteria i.

4. Since

  $$
  S = \Big( \frac{R^2 \theta}{v_0^3} \Big) \Big( \frac{V^3}{N U} \Big),
  $$

  $$
  S(\lambda U, \lambda V, \lambda N) = \lambda \Big( \frac{R^2 \theta}{v_0^3} \Big) \Big( \frac{V^3}{N U} \Big),
  $$


  criteria i holds.

$$
    \Big( \frac{\partial S}{\partial U} \Big)_{V, N} = - \Big( \frac{R^2 \theta}{v_0^3} \Big) \Big( \frac{V^3}{N U^2} \Big),
$$

  	it could not be positive because $V > 0$ and $U^2 > 0$. So it is not a valid fundamental equation.

## Problem 2

1. Max Planck first gave a value for $k_B$.
2. Jean Perrin came up with the number in 1909. American physicist Robert Millikan measured the electron charge in 1910. And we know Faraday constant, so divide it by elementary charge we derive Avogadro's number.

## Problem 3

1. At equilibrium state, $T_1 = T_2 = T$, where $T_1$ and $T_2$ are the temperature of monatomic gas and diatomic gas, respectively. So

  $$
  \begin{align}
  \frac{P_1 V_1}{N_1} &= \frac{P_2 V_2}{N_2},\\
  12000 &= 1.5 N_1 R T + 2.5 N_2 R T.
  \end{align}
  $$

  so $T = 262.427 \,\text{K}$, $P_1 = 218181.8\,\text{Pa}$, $P_2 = 109090.9\,\text{Pa}$.

2. As above.
3. $U_1 = 1.5 N_1 R T = 6545.455 \,\text{J}$, $U_2 = 12000\,\text{J} - U_1 = 5454.545 \,\text{J}$.
4. As above.

## Problem 4

1. See figure below.

  ![Noyan-4-a](http://i.imgur.com/938Iima.png)

2. $P_0 = 2\, \text{atm} = 202650\,\text{Pa}$, $V_0 = 0.001 \,\text{m}^3$, during process I, $PV = P_0 V_0 = N R T_1$, so $N = 0.06094 \,\text{mol}$.

3. See figure below.

  ![pro_4_c](http://i.imgur.com/8gUJVeC.png)

4. In process I, the equation of curve is

  $$
  P = \frac{202.65\,\text{J}}{V},
  $$

  where $V$ ranges from $0.001 \,\text{m}^3$ to $0.002\,\text{m}^3$.
  During process III, $P'V' = P_2 V_2 = N R T_3$, i.e.,
  $$
  P' = \frac{151.9875\,\text{J}}{V'},
  $$

  The work done is the purple area between process I and III, that is,
  $$
  \delta W = \int_{0.001}^{0.002}  \frac{202.65-151.9875}{V} \, d V = 35.117\,\text{J}.
  $$

5. In process I, $dU = 0$. So
  $$
  \delta Q = P \, dV,
  $$
  i.e.,
  $$
  Q = \int_{0.001}^{0.002} \frac{202.65}{V} \, dV = 140.466\,\text{J}.
  $$
  In process IV, $dV =0$,
  $$
  dU = \delta Q = 1.5 N R \Delta T = 75.99375\,\text{J}.
  $$
  So total heat transfer will be $216.460\,\text{J}$.
