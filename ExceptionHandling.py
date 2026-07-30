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
if age < 18:
    raise Exception("Not eligible")
print("Eligible")




correct_password = "Pythin123"
try:
    password = input("Enter password: ")
    if password != correct_password:
        raise ValueError("Wrong Password")
    print("Login Successful")
except ValueError as e:
    print(e)



balance = 5000
try:
    amount = int(input("Enter amount:"))
    if amount > balance:
        raise ValueError("Insufficient Balance")
    balance -= amount
    print("remaining balance =", balance)
except ValueError as e:
    print(e)



try:
    marks = int(input("Enter Marks:"))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")
    print("Valid Marks")
except ValueError as e:
    print(e)



try:
    a = int(input())
    try:
        b = int(input())
        print(a / b)
    except ZeroDivisionError:
        print("Division by zero")
except ValueError:
    print("Invalid Input")



try:
    a = int(input())
    b = int(input())
    print(a / b)
except Exception as e:
    print("Error:", e)


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")
    choice = int(input("Choice: "))
    if choice == 1:
        print(a + b)
    elif choice == 2:
        print(a - b)
    elif choice == 3:
        print(a * b)
    elif choice == 4:
        print(a / b)
    else:
        print("Invalid Choice")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid Input")