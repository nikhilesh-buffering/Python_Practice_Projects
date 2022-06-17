import random
i=0
score=0
cscore=0
opt=[1,2,3]
print("Welcome to Snake Water Gun game!\n")
while(i<10):
    inp=int(input(f"{10-i} plays remaining.Press 1 for snake, 2 for water, 3 for gun\n"))
    cinp=random.choice(opt)
    if inp==cinp:
        cscore=cscore+0
        score=score+0
        print(f"No Result.Your score is {score} and computer score is {cscore}\n")
    elif (inp==1 and cinp==2) or (inp==3 and cinp==1) or (inp==2 and cinp==3):
        cscore=cscore+0
        score=score+1
        print(f"You won! Your score is {score} and computer score is {cscore}\n")
    elif (inp==2 and cinp==1) or (inp==1 and cinp==3) or (inp==3 and cinp==2):
        cscore=cscore+1
        score=score+0
        print(f"You lost. Your score is {score} and computer score is {cscore}\n")
    i+=1
if cscore>score:
    print("Computer won the game. Better luck next time!")
elif score>cscore:
    print("You won!Congratulations!")
else:
    print("The match is Tied!")
