class Student:
    name = "Shashank VA"
    age = 21
s = Student()
print("Name:", s.name)
print("Age:", s.age)



class Student:
    def display(self):
        print("This is a student class")
s = Student()
s.display()