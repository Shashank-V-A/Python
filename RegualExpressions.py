#RE Search
import re
string = "The rain in Spain"
res = re.search("The", string)
if res:
    print("Sikthu Guru")
else:
    print("Manege hogi malko.")


#RE Search 2
text= "The rain in Spain"
if re.match("The", text):
    print("Match found")
else:
    print("No match found")

#RE Match gives all specific pattern in list
data = "cat bat rat mat"
res = re.findall("at", data)
print("All occurances of 'at': ", res)

#RE Substituiton
text = "I like python programming"
res = re.sub("python", "Java", text)
print("After Substitution:", res)


#RE Split
data = "I am Shashank from MVJCE:Currently in my 7th sem"
res = re.split("[:,]", data)
print("After Splitting:", res)


#RE Digit Pattern
text = "My roll number is 45 and my age is 21"
res = re.findall(r"\d+", text)
print("All numbers found:", res)

text = "Contact: shashankva05@gmail.com"
email = re.findall(r"\S+@\S+", text)
print("Email Found:", email)