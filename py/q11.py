q = int(input('Enter the choice triangle,rectangle,circle(1/2/3)'))
if(q== 1):
    a = int(input('Enter the height of triangle : '))
    b = int( input('Enter the base of triangle : '))
    c = int( input('Enter the side of triangle : '))
    area = a*b/2
    perimeter = a+b+c
    print('The area of triangle is',area,'and its perimeter is',perimeter)
elif(q== 2):
    l = int(input('Enter the length of rectangle : '))
    h = int(input('Enter the height of rectangle : '))
    ar = l*h
    pr = 2*(l+h)
    print('The area of rectangle is',ar,'and its perimeter is',pr)
else:
    r = int(input('Enter the radius of circle : '))
    are = 3.14 * r*r
    peri = 6.28*r
    print('The area of circle is',are,'and its perimeter is',peri)



