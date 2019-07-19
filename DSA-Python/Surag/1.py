def fun(L,num):
    if num%2==0:
        num-=1
    if num<=1:
        return L[0]
    elif True:
        return L[num-1]+fun(L,num-2)

L=[1,2,3,4,5,6,7,8,9]
print(fun(L,len(L)))
