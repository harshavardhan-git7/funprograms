def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)
def strong(n):
    if n == 0:
        return 0
    return fact(n % 10) + strong(n//10)
n = 145
print('Strong' if strong(n) == n else 'Not Strong')