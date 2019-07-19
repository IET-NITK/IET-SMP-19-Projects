sum=0
def fun(num):
    global sum
    sum+=num%10
    if num>0:
        fun(num//10)
    return sum

print(fun(12345))