#var = lambda a,b:a+b
#print(var(3,6))
'''l = [7,0,5,4]
for ind in range(len(l)):
    l[ind] = ((lambda a:a*2)(l[ind]))
print(l)'''
n = 5
for x in range(1,n+1):
    print((lambda st : '* '*st)(x))