def prime(n,val):
    if val == n+1:
        return 0
    if n % val == 0:
        return 1 + prime(n,val+1)
    else:
        return 0 + prime(n,val+1)
n = 11
val = 1
print(' prime ' if prime(n,val) == 2 else 'Not Prime')