def disarum(n,pow):
    if n == 0:
        return 0
    return (n % 10)**pow + disarum(n//10,pow-1)
n = 135
pow = len(str(n))
print('Disarum' if disarum(n,pow) == n else 'Not Disarum')