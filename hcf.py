'''def hcf(n1,n2):
    if n1 > n2:
        hcf = n2
    else:
        hcf = n1
    while True:
        if n1 % hcf == 0 and n2 % hcf == 0:
            return hcf
        hcf -= 1
print(hcf(5,6))'''
def hcf(n1,n2):
    if n1 > n2:
        hcf = n2
    else:
        hcf = n1
    for val in range(hcf,0,-1):
        if n1 % val == 0 and n2 % val == 0:
            return val
print(hcf(5,6))