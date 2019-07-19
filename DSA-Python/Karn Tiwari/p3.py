# -*- coding: utf-8 -*-
# partially correct

"""
Created on Wed May 15 11:11:03 2019

@author: karn
"""
#Function to convert string into list
def convert(string):
    li=list(string.split(" "))
    return li

#taking input
print('Enter the string,N other words :',end='\n')
string=input()
n=int(input())
string1=input()

#string conversion
list1=convert(string)
list2=convert(string1)

n1=len(list2)

#Algorithm
for i in range(n1):
    if list2[i] in list1:
        y=list1.index(list2[i])
        x=len(list2[i])
        z=""
        for j in range(x):
            z=z+"*"
        list1[y]=z

#printing result
for i in list1:
    print(i,end=" ")
