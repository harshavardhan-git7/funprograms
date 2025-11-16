def reverse(n,pos):
    if n == 0:
        return 0
    return (n % 10)*pos + reverse(n//10,pos//10)
n = 1234
pos = 10 ** (len(str(n))-1)
print(reverse(n,pos))