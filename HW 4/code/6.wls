#!/usr/bin/env wolframscript
(* ::Package:: *)

p = NN R T/(V -NN b)-NN^2 a/(T V^2);
D[p,V]//Simplify
D[p,V,V]
Solve[{-((6 a NN^2)/(T V^4))+(2 NN R T)/(-b NN+V)^3==0,(2 a NN^2)/(T V^3)-(NN R T)/(-b NN+V)^2==0}//Simplify,{V,T}]
(p/.{V->3 b NN,T->(2 Sqrt[2/3] Sqrt[a])/(3 Sqrt[b] Sqrt[R])})//Simplify
