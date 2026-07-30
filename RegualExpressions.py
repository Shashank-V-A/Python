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


#RE to extract email
text = "Contact: shashankva05@gmail.com"
email = re.findall(r"\S+@\S+", text)
print("Email Found:", email)


#RE for checking valid number
mobile = "7022742719"
if re.fullmatch(r"\d{10}", mobile):
    print("Valid mobile number.")



#RE to print all words
text = "Python Java C++"
words = re.findall(r"\w+", text)
print("All words found:", words)



#RE to check valid date format
date = "18/07/2005"
if re.fullmatch(r"\d{2}/\d{2}/\d{4}", date):
    print("Valid date format.")