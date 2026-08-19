# search the word
with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes python is present in file at line: {lineno}")
        break
    lineno +=1
else:
    print("NO python is NOT present in file")