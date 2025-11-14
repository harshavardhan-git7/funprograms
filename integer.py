def integer(n,pos):
    total = 0
    while n > 0:
        rem = n % 10
        total += rem *(2 **pos)
        pos += 1
        n//=10
    return total
n = 1100
pos = 0
print(integer(n,pos))