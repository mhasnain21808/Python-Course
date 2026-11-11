#String Method (Very Important)

text1 = "      Hello python learners   "

#Remove spaces

print("Remove spaces :",text1.strip())

#Convert to upper case

print("Capital letters:",text1.upper().strip())

#Convert to proper text

print("proper letters:",text1.title().strip())


#Convert to lowercase

print("Lower letters:",text1.lower().strip())

#Replace text

print("Replace tecxt:",text1.replace("python","SQL"))

#Cout occurence of letter of word

print("Count of o:",text1.count("o"))

#Check if text is start with something

print("Start with hello?",text1.strip().startswith("Hello"))

#Check if only numbers are present in data 

mobile = "03"
print(mobile.isnumeric())


msg = "Welcome to python course"
words=msg.split()
print("Word list:",words)

#Jpoin back with hyphen

joined_words=" ".join(words)
print(joined_words)



#Find position of letter
print(text1.strip().find("p"))


#Extract Domain
Email = "name123@gmail.com"
Domain = Email[Email.find("@")+1:5]
print(Domain)