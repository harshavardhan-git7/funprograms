'''def even(n):
    if n == -26:
        return 
    print(n)
    n -= 1
    even(n)
even(-10)'''
def sample(n):
    if n == 0:
        return 
    print(n)
    sample(n-1)
    print(n)
sample(5)