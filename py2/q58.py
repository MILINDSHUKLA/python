#Write a program to store marks of “n” students in a class for “m” subjects using OOP.
class students:
    count = 0
    def __init__(self, name):
        self.name = name
        self.marks = []
        students.count = students.count + 1
        
    def enterMarks(self):
        for i in range(3):
            m = int(input("Enter the marks of %s in %d subject: "%(self.name, i+1)))
            self.marks.append(m)
            
    def display(self):
        print (self.name, "got ", self.marks)
             
name = input("Enter the name of Student:")
s1 = students(name)
s1.enterMarks()
s1.display()
print ("")
name = input("Enter the name of Student:")
s2 = students(name)
s2.enterMarks()
s2.display()

s2.displayCount()