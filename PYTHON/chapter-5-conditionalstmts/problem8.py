# find vowel and consonent
char = input("Enter a alphabet : ")

if (len(char)==1 and char.isalpha() ):
    if(char.lower() in 'aeiou' ):
        print(char,"is a Vowel Alphabet")
    else:
        print(char,"is a Consonent Alphabet")
else:
    print("----Invalid value entered----")