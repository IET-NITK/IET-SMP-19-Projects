L=[1,5,2]
def fun(n):
    global L
    if n<=len(L)-1:
        return L[n]
    else:
        L.append(3*fun(n-3)-5*fun(n-1))
        return L[n]
print(fun(10),L)