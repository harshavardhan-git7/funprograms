'''def add(n):
    if n == 0:
        return 0
    return (n % 10) + add(n//10)
print(add(1234))'''
def adddigit(n):
    return 0 if n == 0 else (n% 10) + adddigit(n//10) 
print(adddigit(1234))