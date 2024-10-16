import sys
import random
from enum import Enum

def rps(name='Player One'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
            
        playerchoice = input(f"\n{name}, please enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoise = random.choice("123")

        computer = int(computerchoise)

        print(
            f"\n{name}, you chose {str(RPS(player)).replace("RPS.", "").title()}."
        )
        print(
            f"\nPython chose {str(RPS(computer)).replace("RPS.", "").title()}.\n" 
        )

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if playerchoice == 1 and computerchoise == 3:
                player_wins += 1
                return f"🎉 {name} wins!"
            elif playerchoice == 2 and computerchoise == 1:
                player_wins += 1
                return f"🎉 {name} wins!"
            elif playerchoice == 3 and computerchoise == 2:
                player_wins += 1
                return f"🎉 {name} wins!"
            elif player == computer :
                return "😲 Tie game."
            else:
                python_wins += 1
                return f"😈 Python wins! \nSorry {name}."
        
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {game_count}")
        print(f"\n{name}'s Count: {player_wins}")
        print(f"\nGame Count: {python_wins}")

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
            sys.exit(f"Bye {name}! 👋")       
    
    return play_rps



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game esperance."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()