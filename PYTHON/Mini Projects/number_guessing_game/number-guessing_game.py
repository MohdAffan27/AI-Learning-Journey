import random
secret_number = random.randint(1,20)
max_attemp = 5
print("welcome to the number Guessing Game...")
print("\n-----lets start-----")
print("You have only 5 chances to guess it!")
print("Guess the number between (1-20) in",max_attemp,"tries\n")

# loop a specific number of times
for attempts in range(1,max_attemp+1):
    print("Attempt",attempts,"/",max_attemp , end="")
    guess= int(input(" - Enter your Guess: "))
    if guess < secret_number:
        print("Too Low!..")
    elif guess > secret_number:
        print("Too High...")
    else:
        print("Correct! Took",attempts,"tries to guess.")
        break
else:
    print("Game over! you ran out of attempts. the number was",secret_number)