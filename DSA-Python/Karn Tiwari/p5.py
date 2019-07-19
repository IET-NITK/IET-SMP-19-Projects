# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:26:46 2019

@author: karn
"""
#Function to convert string into list
def convert(string):
    li=list(string.split(" "))
    return li

#taking input
print('enter the input numbers separated by space and K',end='\n')
string=input()
k=int(input())

#function calling
arr=convert(string)
d=len(arr)
for i in range(d):
    arr[i]=float(arr[i])

#sorting of array element 
for i in range(d-1):
    for j in range(i+1,d):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
            
f_arr=[]

for num in arr:
    if num not in f_arr:
        f_arr.append(num)
        
d=len(f_arr)

#search for Kth element in the list        
if k<=d:
    print(f_arr[k-1])
        
else:
    print('Does not exist!')

