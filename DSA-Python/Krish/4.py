
# correct
x1,y1=float(input('enter x1')),float(input ('enter y1'))
x2,y2=float(input('enter x2')),float(input ('enter y2'))
x3,y3=float(input('enter x3')),float(input ('enter y3'))
a=(((x2-x1)**2)+((y2-y1)**2))**0.5
b=(((x2-x3)**2)+((y2-y3)**2))**0.5
c=(((x3-x1)**2)+((y3-y1)**2))**0.5
s=(a+b+c)/2
d=(s*(s-a)*(s-b)*(s-c))**0.5
print(float(d))
