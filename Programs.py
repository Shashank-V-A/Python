#Program for sqaure of numbers uisng List
num = [10, 20, 30, 40, 50]
square = [x*x for x in num]
print(square)

#Program for even numbers
even = [x for x in range(1,21) if x%2==0]
print(even)

#Program to find length of each word
names = ["Java", "Python", "ReactJS", "SpringBoot"]
length = [len(x) for x in names]
print(length)

#Program for dictionary comprehension
square = {x:x*x for x in range(1, 6)}
print(square)

#Program for dictionary with even numbers
even = {x:x*x for x in range(1, 11) if x%2==0}
print(even)

#Set Comprehension
square = {x*x for x in range(1, 11)}
print(square)


#Nested List Comprehension
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8 , 9]]
flat = [num for row in matrix for num in row]
print(flat)

#Multiplication table using list comprehension
num = 69
table = [num * i for i in range(1, 11)]
print(table)