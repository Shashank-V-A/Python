try:
    a = 10
    b = 0
    res = a / b
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid Input")



try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter only integers.")


try:
    a = int(input())
    b = int(input())
    print(a / b)
except(ValueError, ZeroDivisionError):
    print("Something went wrong")



try:
    a = int(input())
    b = int(input())
    res = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Answer =", res)



try:
    file = open("demo.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Program Finished")



try:
    num = int(input())
except ValueError:
    print("Invalid Number.")
else:
    print("Square =", num * num)
finally:
    print("Thank you")


try:
    f = open("student.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File does not exist")



numbers = [10, 20, 30]
try:
    print(numbers[5])
except IndexError:
    print("Index out of range")


student = {"name" : "Shashank"}
try:
    print(student["age"])
except KeyError:
    print("Key not found")



try:
    print(10 + "20")
except TypeError:
    print("Cannot add int and string")



age = int(input("Enter Age:"))
