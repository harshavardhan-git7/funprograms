from functools import reduce
#print(reduce(lambda a,b:a+b,range(1,6)))
n = 5
print(reduce(lambda a,b:a*b,range(1,n+1)))