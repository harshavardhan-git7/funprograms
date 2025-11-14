'''def prime(n):
    if n > 1:
        for x in range(2,n//2+1):
            if n % x == 0:
                return 'Not Prime'
        return 'Prime'
    return 'Not Prime'
n = 11
print(prime(n))'''
def prime(n):
    count = 0
    for x in range(1,n+1):
        if n % x == 0:
            count += 1
    if count == 2:
        return 'Prime'
    return 'Not Prime'
n = 11
print(prime(n))