'''def composite(n):
    if n > 1:
        for x in range(2,n//2+1):
            if n % x == 0:
                return 'Composite'
        return 'Not Composite'
    return 'Not Composite'
n = 10
print(composite(n))'''
def composite(n):
    count = 0
    for x in range(1,n+1):
        if n % x == 0:
            count += 1
            
    if count > 2:
        return 'Composite'
    return 'Not Composite'
n = 10
print(composite(n))
