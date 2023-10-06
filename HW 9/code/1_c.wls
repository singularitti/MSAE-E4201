#!/usr/bin/env wolframscript
(* ::Package:: *)

w=w0-A Log[V/V0];
gamma=A/w;
T=1/(kB/h/w*Log[1+3NN h w/U])
dtv=D[T,V]//FullSimplify
1/V*1/dtv*V/(gamma*Cv)//FullSimplify
