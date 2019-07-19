#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 22:35:31 2019

@author: surag
"""
# correct

def spil(arg1):
    K=[]
    s=''
    for e in arg1:
        if e==arg1[-1]:
            s=s+e
            K.append(s)
        elif e ==" ":
             K.append(s)
             s=''

        else:
            s=s+e
    return K

sen=input()
num=int(input())
words=input()
ori_words=(spil(sen))
censor=(spil(words))
print(ori_words,censor)
s=""
for i in range(len(ori_words)):
    if ori_words[i] in censor:
        s=s+"*"*len(ori_words[i])+" "
    else:
        s=s+ori_words[i]+' '
print(s)
