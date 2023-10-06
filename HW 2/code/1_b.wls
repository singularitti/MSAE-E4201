#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear["Global`*"]

a = (3 9 10^-6) ^ (1/3); b = (2 4 10^-6) ^ (1/3);

S = a UA ^ (1/3) + b (80 - UA) ^ (1/3)

Solve[\!\(
\*SubscriptBox[\(\[PartialD]\), \(UA\)]S\) == 0, UA]
