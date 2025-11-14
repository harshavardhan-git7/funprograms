def factorial(n):
    fact = 1
    for x in range(1,n+1):
        fact *= x
    return fact
n = 5
print(factorial(n))