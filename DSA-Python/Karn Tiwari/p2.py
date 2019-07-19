# -*- coding: utf-8 -*-

# correct

"""
Spyder Editor

This is a temporary script file.
"""
#import math library
import math
#Enter the input string
string=input()
x=len(string)

#finding the perfect string
for k in range(x):
    if (k*k)>=x:
        x=k
        break

#variable declaration and initialize
n=len(string)
count=0
s=""

for i in range(x*x):
    if count<n:
        s=s+string[i]
        count+=1
    else:
        s=s+"*"

count=0

#formation of square matrix
a=[['*' for i in range(x)] for j in range(x) ]
for i in range(x):
    for j in range(0,i+1):
        a[i-j][j]=s[count]
        count+=1

y=1
count=x*x-1

for i in range(x-1,0,-1):
    z=0
    for j in range(x-1,x-1-y,-1):
        a[i+z][j]=s[count]
        count-=1
        z+=1
    y+=1

#printing the matrix
print(a)
