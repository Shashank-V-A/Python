
print("--- Arithmetic Operators ---")
a = 15
b = 4

print(f"Addition (+):       {a} + {b} = {a + b}")
print(f"Subtraction (-):    {a} - {b} = {a - b}")
print(f"Multiplication (*): {a} * {b} = {a * b}")
print(f"Division (/):       {a} / {b} = {a / b}")      
print(f"Floor Division (//):{a} // {b} = {a // b}")   
print(f"Modulo (%):         {a} % {b} = {a % b}")      
print(f"Exponent (**):      {a} ** {b} = {a ** b}")   
print()

print("--- Comparison Operators ---")
x = 10
y = 20

print(f"Equal to (==):              {x} == {y} is {x == y}")
print(f"Not equal to (!=):          {x} != {y} is {x != y}")
print(f"Greater than (>):           {x} > {y} is {x > y}")
print(f"Less than (<):              {x} < {y} is {x < y}")
print(f"Greater than or equal (>=): {x} >= {y} is {x >= y}")
print(f"Less than or equal (<=):    {x} <= {y} is {x <= y}")
print()

print("--- Logical Operators ---")
p = True
q = False

print(f"Logical AND (and): {p} and {q} is {p and q}")  
print(f"Logical OR (or):   {p} or {q} is {p or q}")   
print(f"Logical NOT (not):  not {p} is {not p}")       

print("--- Bitwise Operators ---")
m = 5
n = 3

print(f"Bitwise AND (&): {m} & {n} = {m & n}")   
print(f"Bitwise OR (|):  {m} | {n} = {m | n}")  
print(f"Bitwise XOR (^): {m} ^ {n} = {m ^ n}")   
print(f"Bitwise NOT (~): ~{m} = {~m}")           
print(f"Left Shift (<<): {m} << 1 = {m << 1}")   
print(f"Right Shift (>>):{m} >> 1 = {m >> 1}")  
print()


print("--- Assignment Operators ---")
c = 10  
print(f"Assign (=):          c = {c}")

c += 5  
print(f"Add & Assign (+=):   c became {c}")

c *= 2  
print(f"Mult & Assign (*=):  c became {c}")
print()

print("--- Identity Operators ---")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list2:     {list1 is list2}")      
print(f"list1 is list3:     {list1 is list3}")     
print(f"list1 is not list2: {list1 is not list2}")  
print()



print("--- Membership Operators ---")
my_string = "Hello Python"
my_list = [10, 20, 30]
print(f"'Python' in string:   {'Python' in my_string}")
print(f"40 not in list:       {40 not in my_list}")
