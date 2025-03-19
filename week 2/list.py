numbers= [2,5,9]
#print(numbers)

languages= ["python", "html", "css", "java"]
#print(languages[3])
#print(languages[-2])
#print(languages[1:3])
#print(languages[1:])
languages.append("react")
languages.extend(numbers)

print(languages)
print(languages.count("html"))
print(languages.index("react"))
