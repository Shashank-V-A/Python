s = "Python"
print(s)
print(type(s))

s = "Python"
print(s[0])
print(s[1])
print(s[-1])

s = "Programming"
print(s[0:6])
print(s[3:8])
print(s[::-1])

first = "Hello"
second = "World"
print(first + " " + second)


a = "apple"
b = "banana"
print(a == b)
print(a < b)

s = "Shashank Is The Best"
for ch in s:
    print(ch)

s = input("Enter string: ")
print(s.replace(" ", ""))

s = input("Enter string: ")
if len(s) > 1:
    S = s[-1] + s[1:-1] + s[0]
print(s)


s = "Python"
print(s.isalpha())

s = "12345"
print(s.isdigit())

s = input("Enter string: ")
upper = 0
lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1


s1 = input("First string: ")
s2 = input("Second string: ")
if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
