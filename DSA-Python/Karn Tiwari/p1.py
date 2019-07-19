# -*- coding: utf-8 -*-
# correct

"""
Created on Wed May 15 11:53:39 2019

@author: karn
"""
#function declaration
def compare(string1,string2):
    arr=list(set(string1)&set(string2))
    y=""

    for i in range(len(arr)):
        y=y+arr[i]

    return y

#taking input
arr=[]
print('Enter N strings: ')
n=int(input())
for i in range(n):
    x=input()
    arr.append(x)

#comparison of strings of array
for i in range(n):
    if i==0:
        y=compare(arr[i],arr[i+1])
    else:
        y=compare(y,arr[i])

#printing of result
print(y)
