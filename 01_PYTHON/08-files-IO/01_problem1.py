# find a word in a file

f = open("poem.txt")
content = f.read()
if ("twinkle" in content):
    print("The word \"twinkle\" is present in the file")
else:
    print("The word \"twinkle\" is not present in the file")
f.close()