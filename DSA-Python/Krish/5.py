
# wrong
a = input('enter a list of numbers')
list=a.split()
list.sort()
k=int(input('enter an integer value for k'))
if k<len(list):
     print(list[k-1])
else:
     print('does not exist')
