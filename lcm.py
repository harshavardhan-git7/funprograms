def lcm(n1,n2):
    if n1 > n2:
        lcm = n1
    else:
        lcm = n2
    while True:
        if lcm % n1 == 0 and lcm % n2 == 0:
            return lcm
        lcm += 1

print(lcm(6,3))