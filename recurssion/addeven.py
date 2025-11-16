def evenodd(n):
    return 0 if n == 0 else (n % 10 if n % 2 == 0 else 0) + evenodd(n//10)
print(evenodd(12345678))