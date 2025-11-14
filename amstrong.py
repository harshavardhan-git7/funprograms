def amstrong(n,pow):
    total = 0
    temp = n
    while n > 0:
        rem = n % 10
        total += rem ** pow
        n //=10
    if total == temp:
        return 'Amstrong'
    return 'Not Amstrong'
    
n = 153
pow = len(str(n))
print(amstrong(n,pow))

    

    