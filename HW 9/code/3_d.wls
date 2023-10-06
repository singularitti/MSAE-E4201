#!/usr/bin/env wolframscript
(* ::Package:: *)

Series[Log[x], {x, x0, 1}]

1/2 / L (2 Nr^2 / NN - 3 Nr + NN) /. {Nr -> NN / 2 + L / 2 / l}

Simplify[(-3 (L / (2 l) + NN / 2) + (2 (L / (2 l) + NN / 2) ^ 2) / NN
     + NN) / (2 L)]
