#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:29:02 2019

@author: surag
"""
# not the fourth question

L=[]
def numbs(arg1):
    s=''
    global L
    for e in arg1:
        if e!=" ":
            s=s+e
        else:
            L.append(int(s))
            s=''
    L.sort()
    return L
sen=input()
num=int(input())
numbs(sen)
print(L[num+1])
