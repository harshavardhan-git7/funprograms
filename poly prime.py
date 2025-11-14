def prime(n):
    if n > 1:
        for x in range(2,n//2+1):
            if n % x == 0:
                return False
        return True
    return False
def palindrome(n):
    total = 0
    while n > 0:
        rem = n % 10
        total = total * 10 + rem
        n//= 10
    return total
n = 11
if prime(n) and palindrome(n) == n:
    print('poly prime')
else:
    print('Not poly prime')
