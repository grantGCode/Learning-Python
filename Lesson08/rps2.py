import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    print("")
    playerchoice = input("Enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computerchoise = random.choice("123")

    computer = int(computerchoise)

    print("")
    print("You chose "+ str(RPS(player)).replace("RPS.", "") + "." )
    print("Python chose "+ str(RPS(computer)).replace("RPS.", "") + "." )
    print("")


    if playerchoice == 1 and computerchoise == 3:
        print("🎉 You win!")
    elif playerchoice == 2 and computerchoise == 1:
        print("🎉 You win!")
    elif playerchoice == 3 and computerchoise == 2:
        print("🎉 You win!")
    elif player == computer :
        print("😲 Tie game.")
    else:
        print("😈 Python wins!")
    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        break
        # or I could also use: playagain = False