#print(list(filter(lambda num:num % 2 == 0,[1,2,3,4,5,6])))
# positive numbers
#print(list(filter(lambda x : x > 0,[1,-2,5,3,-6,-8])))
'''def string(st):
    if type(st) == str and st.startswith('A'):
        return st
print(list(filter(string,['Apple','abc',7.8,'xyz'])))'''
'''def prime(n):
    if n > 1:
        for x in range(2,n//2+1):
            if n % x == 0:
                return False
        return True
    return False
print(list(filter(prime,range(10,41))))'''
#print(tuple(filter(len,['abcd','123','','12abc'])))
#print(list(filter(int,input('Enter Elements').split())))
print(list(map(lambda n1,n2:n1 + n2,list(map(int,input('Enter Elements').split())),list(map(int,input('Enter elements').split())))))
