def integer(n,pos):
    if n == 0:
        return 0
    return (n % 10) * (2 ** pos) + integer(n//10,pos+1)
n = 1100
pos = 0
print(integer(n,pos))