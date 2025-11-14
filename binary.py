def binary(n,pos):
    total = 0
    while n > 0:
        rem = n % 2 
        total += rem * pos
        pos *= 10
        n//=2
    return total
n = 12
pos = 1
print(binary(n,pos))