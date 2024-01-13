myfile = open("fruits.txt")
content = myfile.read()
myfile.close()

with open("fruits.txt") as myfile:
    content = myfile.read()


print(content)

with open("vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCucumber\nOnion")
    myfile.write("\nGarlic")

def foo(character, filepath="fruits.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)


with open("fruits.txt", "a+") as myfile:
    myfile.write("\nOkra")
    myfile.seek(0)
    content = myfile.read()
    
print(content)
