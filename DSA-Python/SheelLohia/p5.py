# problem

def listing(*varlist):
    for i in varlist:
        a.append(i)

a=list()

listing(input("Enter the numbers "))
k=int(input("Enter k "))

print(a)

for u in range(1,k):
    s=min(a)
    b=a.count(s)
    for p in range(b):
        a.remove(s)
if(a==None):
    print("Does not exist ")
else:
    print(min(a))
