# Write a program to check whether a given year is leap year or not.
year = int(input('Enter the year '))
x = year%100
r = x%4
if(r==0):
    print('It is a leap year')
else:
    print('It is not a leap year')
