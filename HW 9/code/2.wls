#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"]

s = kB Simplify[nn Log[nn / (nn / 2 + U / (2 mu H))] + (nn / 2 - U / 
    (2 mu H)) Log[(nn / 2 + U / (2 mu H)) / (nn / 2 - U / (2 mu H))]]

T = 1 / D[s, U] // Simplify

D[(Exp[-2 mu H / kB / t] - 1) / (Exp[-2 mu H / kB / t] + 1) nn mu H, 
    t] // Simplify

D[s, H] T // FullSimplify
