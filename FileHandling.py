file = open("student.txt", "w")
file.write("Hello Python\n")
file.write("Welcome to file handling")
file.close()
print("Data written successfully.")



file = open("student.txt", "r")
data = file.read()
print(data)
file.close()



file = open("student.txt", "r")
print(file.readline())
print(file.readline())
file.close()



file = open("student.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()



file = open("student.txt", "a")
file.write("\nPython File Handling")
file.close()
print("Data appended successfully.")



source = open("student.txt", "r")
destination = open("copy.txt", "w")
destination.write(source.read())
source.close()
destination.close()



file = open("student.txt", "r")
data = file.read()
print("characters =", len(data))
file.close()



file = open("student.txt", "r")
data = file.read()
words = data.split()
print("Words =", len(words))
file.close()



file = open("student.txt", "r")
data = file.read()
word = input("Enter word:")
if word in data:
    print("Word Found")
else:
    print("Word Not Found")



file = open("student.txt", "r")
data = file.read().lower()
count = 0
for ch in data:
    if ch in "aeiou":
        count += 1
print("Vowels =", count)
file.close()



file = open("student.txt", "r")
data = file.read()
upper = 0
lower = 0
for ch in data:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase =", upper)
print("Lowecase =", lower)



