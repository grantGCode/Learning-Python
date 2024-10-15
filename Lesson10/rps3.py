import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
        
    playerchoice = input("\nEnter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    player = int(playerchoice)

    computerchoise = random.choice("123")

    computer = int(computerchoise)

    print("\nYou chose "+ str(RPS(player)).replace("RPS.", "") + "." )
    print("Python chose "+ str(RPS(computer)).replace("RPS.", "") + ".\n" )

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

    while True:
        playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")       


play_rps()