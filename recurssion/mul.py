'''def multi(n):
    if n == 0:
        return 1
    return (n % 10) * multi(n//10)
print(multi(1234))'''
def mult(n):
    return  1 if n == 0 else (n % 10) * mult(n//10)
print(mult(1234))