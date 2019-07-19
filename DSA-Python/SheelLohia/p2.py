# problem
from array import *
y=input("Enter a string ")
from math import sqrt,ceil
m=0
j=0
x=ceil(sqrt(len(y)))
a=[["*" for i in range(x)]for j in range(x)]
while(m<x):
    i=0
    while((i<=m) and (j<len(y))):
        a[m-i][i]=y[j]
        print(a[i][m-i])
        j+=1
        i+=1
    m+=1
m-=1
while(m>=0):
    i=x-m
    while((i<=m) and (j<len(y))):
        a[x+m-2-i][i]=y[j]
        j+=1
        i+=1
    m-=1
for b in range(x):
    print(a[b])
