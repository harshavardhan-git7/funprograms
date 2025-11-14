def prime(n):
    if n > 1:
        for x in range(2,n//2+1):
            if n % x == 0:
                return False
        return True
    return False
def reverse(n):
    temp = n
    total = 0
    while n > 0:
        rem = n % 10
        total = total * 10 + rem
        n//=10
    return total
n = 13
var = reverse(n)
print('Emirp' if prime(n) and var != n and prime(var) else 'Not Emirp')
        