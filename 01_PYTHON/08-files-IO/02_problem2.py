# save the high score of the game 
import random

def game():
    print("you are playing a game...")
    score = random.randint(1,69)

    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print("your score:",score)
    if(score>hiscore):
        with open("hiscore.txt" , "w") as f:
            f.write(str(score))
    return score
game()