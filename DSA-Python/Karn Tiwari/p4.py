# -*- coding: utf-8 -*-

# correct

"""
Created on Wed May 15 09:33:39 2019

@author: karn
"""
#taking input
x=[ 0 for i in range(3)]
y=[ 0 for i in range(3)]

print('enter the three coordinate of a triangle:',end='\n')

for i in range(3):
    x[i],y[i]=input().split(" ")

#converting string to float
for i in range(3):
    x[i]=float(x[i])
    y[i]=float(y[i])

#calculating sides of triangle
a=((x[0]-x[1])**2 +(y[0]-y[1])**2)**0.5
b=((x[1]-x[2])**2 +(y[1]-y[2])**2)**0.5
c=((x[2]-x[0])**2 +(y[2]-y[0])**2)**0.5
s=(a+b+c)/2

#calculating area and printing the result
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)
