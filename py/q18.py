# Write a program to check whether a given number is armstrong or not.
n = int(input('Enter the number : '))
l = n
s = 0
while(n>0):
    d = n%10
    n = n/10
    s = s+d*d*d
if(s==l):
    print('It is an armstrong number')
else:
    print('It is not an armstrong number')