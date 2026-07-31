#Program 1
class Student:
    name = "Shashank VA"
    age = 21
s = Student()
print("Name:", s.name)
print("Age:", s.age)


#Program 2
class Student:
    def display(self):
        print("This is a student class")
s = Student()
s.display()


#Program 3
class Student:
    college = "MVJ College Of Engineering" #Class Variable
    def __init__(self,name):
        self.name = name   #Instance Variable
        
#Parameterised Constructor
s1 = Student("Swarup")
s2 = Student("Rahul")
print(s1.name)
print(s2.name)
print(s1.college)
print(s2.college)

Student.college = "IISC"
print(s1.college)
print(s2.college)