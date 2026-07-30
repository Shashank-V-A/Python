def outer():
    def inner():
        print("Inner Function")
    print("Outer Function")
    inner()
outer()

def calculator():
    def add(a, b):
        return a + b
    print(add(10, 20))
calculator()