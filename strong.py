def fact(n):
    fact = 1
    for x in range(1,n+1):
        fact *= x
    return fact
def strong(n):
    total = 0
    while n > 0:
        rem = n % 10
        total += fact(rem)
        n//=10
    return total
n = 145
print('Strong' if  n == strong(n) else 'Not Strong')