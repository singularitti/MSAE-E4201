#!/usr/bin/env wolframscript
(* ::Package:: *)

ClearAll["Global`*"]

f[{m_, n_}] :=
    Assuming[m > 0 && n > 0, Simplify[{n, Sqrt[n m]}]] (*m \:662f\:4e0a\:4e0a\:4e00\:6b65 final, n \:662f\:4e0a\:4e00\:6b65 final*)

finalT = NestList[f, {T3, (T1 T2) ^ (1/2)}, 25]

finalT[[All, 2]]

Cases[finalT, (T1 T2) ^ n_. :> n, -1]

Cases[Simplify[finalT[[All, 2]], Assumptions -> {T1 > 0, T2 > 0, T3 >
     0}], Power[Times[T1, T2], Rational[x_, y_]] -> {x / y}, {0, Infinity
    }] // Flatten
