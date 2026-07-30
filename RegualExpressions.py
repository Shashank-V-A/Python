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