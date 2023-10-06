#!/usr/bin/env wolframscript
(* ::Package:: *)

Z = Exp[\[Beta] \[Mu] H] + Exp[-\[Beta] \[Mu] H]

u = -1 / V \[Mu] H (Exp[\[Beta] \[Mu] H] - Exp[-\[Beta] \[Mu] H]) / (
    Exp[\[Beta] \[Mu] H] + Exp[-\[Beta] \[Mu] H]) // Simplify

D[u /. {\[Beta] -> 1 / (kB T)}, T] // Simplify

-D[u /. {\[Beta] -> 1 / (kB T)}, H] // Simplify
