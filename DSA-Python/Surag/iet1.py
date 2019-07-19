
# correct

def common(arg1,arg2):
    s=''
    for e in arg1:
        if e in arg2:
            s=s+e
    return s
num=int(input())
l=[]
if num>0:
    sen=input()
    if num==1:
        print (sen)
        pass
if num>1:
    sen1=input()
    sen=common(sen,sen1)
    if num==2:
        print(sen)
        pass
if num>2:
    for i in range(num-2):
        sen1=input()
        sen=common(sen,sen1)
    print(sen)
