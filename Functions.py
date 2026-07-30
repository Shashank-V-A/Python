def greet():
    print("Welcome to Python")
greet()

def add(a, b):
    print("Sum =", a + b)
add(10, 20)

def square(n):
    return n * n
res = square(5)
print(res)

def evenOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"