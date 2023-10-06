#!/usr/bin/env wolframscript
(* ::Package:: *)

ClearAll["Global`*"]

s = ParallelTable[ParallelTable[50^2 <= (x - xp) ^ 2 + (y - yp) ^ 2 +
     (z - zp) ^ 2 <= 60^2, {x, xp, 60 + xp, 2}, {y, yp, 60 + yp, 2}, {z, 
    zp, 60 + zp, 2}], {xp, 0, 2, 0.1}, {yp, 0, 2, 0.1}, {zp, 0, 2, 0.1}];

t = ParallelTable[Select[s[[i, j, k]] // Flatten, # == True&] // Length,
     {i, 1, 21}, {j, 1, 21}, {k, 1, 21}];

t // Flatten // Union
