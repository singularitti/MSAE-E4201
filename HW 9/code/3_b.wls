#!/usr/bin/env wolframscript
(* ::Package:: *)

(* Mathematica Source File  *)
(* Created by Mathematica Plugin for IntelliJ IDEA *)
(* :Author: Qi *)
(* :Date: 2017-04-03 *)

S = kB (NN Log[NN / (NN - Nr)] - Nr Log[Nr / (NN - Nr)]);
D[S, Nr] // Simplify
