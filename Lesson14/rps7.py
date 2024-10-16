import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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

        print(
            f"\nYou chose {str(RPS(player)).replace("RPS.", "").title()}."
        )
        print(
            f"\nPython chose {str(RPS(computer)).replace("RPS.", "").title()}.\n" 
        )

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if playerchoice == 1 and computerchoise == 3:
                player_wins += 1
                return "🎉 You win!"
            elif playerchoice == 2 and computerchoise == 1:
                player_wins += 1
                return "🎉 You win!"
            elif playerchoice == 3 and computerchoise == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer :
                return "😲 Tie game."
            else:
                python_wins += 1
                return "😈 Python wins!"
        
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {str(game_count)}")
        print(f"\nGame Count: {str(player_wins)}")
        print(f"\nGame Count: {str(python_wins)}")

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
    
    return play_rps

rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()