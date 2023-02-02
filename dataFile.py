with open("testFile.txt","r") as file:
    content = file.read()
print(content)
with open("testFile.txt","w") as file:
    file.write("This is python dataFile")
with open("testFile.txt","a") as file:
    file.write("This is appended file")