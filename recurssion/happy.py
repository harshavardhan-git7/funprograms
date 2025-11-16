def square(n):
    if n == 0:
        return 0
    return (n % 10) **2 + square(n//10)
def happy(n):
    if n > 9:
        return happy(square(n))
    return n == 1 or n == 7
print('Happy' if happy(19) else 'Not Happy')