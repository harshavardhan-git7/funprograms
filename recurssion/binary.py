def binary(n,pos):
    if n == 0:
        return 0
    return (n % 2)*pos + binary(n//2,pos*10)
n = 12
pos = 1
print(binary(n,pos))