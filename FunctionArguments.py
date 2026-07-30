def student(name, age):
    print(name, age)
student("Shashank", 21)

def student(name, age):
    print(name, age)
student(age=21, name="Shashank")

def employee(name, salary=30000):
    print(name, salary)
employee("Shashank")
employee("Karthik", 50000)

def total(*numbers):
    print(sum(numbers))
total(10, 20)
total(10, 20, 30, 40)

def details(**student):
    print(student)
details(name="Shashank", age=21, city="Bangalore")
