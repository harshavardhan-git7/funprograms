def amstrong(n,pow):
    if n == 0:
        return 0
    return (n % 10)**pow + amstrong(n//10,pow)
n = 153
pow = len(str(n))
print('Amst' if amstrong(n,pow)== n else 'Not Amst')