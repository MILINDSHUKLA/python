# Write a program to check whether a given number is armstrong or not.
n = int(input('Enter a number : '))
t = n
r = 0
while(n>0):
    d = n%10
    r = r*10+d
    n=n//10
if(t==r):
    print('Yes,it is a Palindrome Number')
else:
    print('No it is not a Palindrome Number')