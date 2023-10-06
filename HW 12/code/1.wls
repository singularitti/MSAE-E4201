#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"]

f[n_, {x_, y_, z_}] :=
    n x ((x + y) ^ (n - 1) + (x + z) ^ (n - 1)) - n x^n // Expand

f[2, {x, y, z}]

f[3, {x, y, z}]

f[4, {x, y, z}]

sum = Sum[f[n, {x, y, z}], {n, 0, Infinity}] // FullSimplify

xi = 1 / (1 - (x + y + z))

bar = sum / xi // FullSimplify

n0sum = Sum[f[n, {x, y, z}], {n, 0, Infinity}] // FullSimplify

n1sum = Sum[f[n, {y, x, z}], {n, 0, Infinity}] // FullSimplify

n2sum = Sum[f[n, {z, y, x}], {n, 0, Infinity}] // FullSimplify

(0 n0sum + 1 n1sum + 2 n2sum) / (n0sum + n1sum + n2sum) // FullSimplify
