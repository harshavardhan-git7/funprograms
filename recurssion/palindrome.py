def palindrome(n,pos):
    if n == 0:
        return 0
    return (n % 10)*pos + palindrome(n//10,pos//10)
n = 121
pos = 10 **(len(str(n))-1)
print('Palindrome' if palindrome(n,pos)==n else 'Not Palindrome')