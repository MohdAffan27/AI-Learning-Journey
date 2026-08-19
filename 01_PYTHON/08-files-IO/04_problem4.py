# replace the word from the file
word = "affan"

with open("file.txt","r") as f:
    content = f.read()
contentnew = content.replace(word,"sumair")

with open("file.txt", "w") as f:
    f.write(contentnew)
