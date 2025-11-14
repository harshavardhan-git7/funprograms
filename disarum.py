def disarum(n,pos):
    total = 0
    temp = n
    while n > 0:
        rem = n % 10 
        total += rem **pos
        pos -= 1
        n //=10
    return total
n = 135
pos=len(str(n))
print('Disarum' if  n == disarum(n,pos) else 'Not Diarum')
    