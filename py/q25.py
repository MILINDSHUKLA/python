#Write a program to print the following pattern.
'''*
**
***
**
*'''
for i in range(1,5):
    for j in range(1,i):
          print('*',end = '')  
    print('\n')
for i in range(4,0,-1):
     for j in range(1,i):
         print('*',end='')
     print('\n')