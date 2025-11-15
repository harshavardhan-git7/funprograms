'''def Sum(n):
    total = 0
    while n > 0:
        rem = n % 10
        total += rem
        n//=10
    return total
mapobj = map(Sum,[1234,456,798])
for x in mapobj:
    print(x,end=' ')'''
'''def prime(n):
    if n > 1:
        for x in range(2,n//2+1):
            if n % x == 0:
                return 'NOt Prime'
        return 'Prime'
    return 'Not Prime'
mapobj = map(prime,range(1,11))
for x in mapobj:
    print(x)'''
'''def even(n):
    if n % 2 == 0:
        return 'Even'
    return 'Odd'
mapobj = map(even,range(1,11))
for x in mapobj:
    print(x)'''
'''def Amstrong(n):
    pow = len(str(n))
    total = 0
    temp = n
    while n > 0:
        rem = n % 10
        total += rem ** pow
        n//=10
    if total == temp:
        return f'{temp} is Amstrong'
    return f'{temp} is Not Amstrong'
mapobj = map(Amstrong,range(1,21))
for x in mapobj:
    print(x)'''
'''def binary(n):
    total = 0
    pos = 1
    while n > 0:
        rem = n % 2
        total += rem * pos
        pos *= 10
        n//=2
    return total
mapobj = map(binary,range(50,100))
for x in mapobj:
    print(x)'''
#print(list(map(lambda x : x + 5,range(20,30))))
'''def add(n1,n2):
    return n1 + n2
print(list(map(add,[10,20,30],[50,60,70])))'''
#print('\n'.join(list(map(lambda st : '* '*3,range(1,4)))))
#print('\n'.join(list(map(lambda st : '* '*st,range(1,4)))))
#print('\n'.join(list(map(lambda st : '* '*st,range(3,0,-1)))))
#print('\n'.join(list(map(lambda sp,st:'  '*sp+'* '*st,range(3,-1,-1),range(1,5)))))
#print('\n'.join(list(map(lambda sp,st:'  '*sp + '* '*st,range(0,4),range(4,0,-1)))))

    