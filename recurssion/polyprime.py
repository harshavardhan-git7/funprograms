def prime(n,val):
    if val == n+1:
        return 0
    if n % val == 0:
        return 1 + prime(n,val+1)
    else:
        return 0 + prime(n,val+1)
def polyprime(n,pos):
    if n == 0:
        return 0
    return (n % 10)*pos + polyprime(n//10,pos//10)
n = 11
pos = 10 **(len(str(n))-1)
val = 1
if polyprime(n,pos) == n and prime(n,val) == 2:
    print('Polyprime')
else:
    print('Not Prime')
    