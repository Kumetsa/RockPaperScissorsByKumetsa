import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()


while True:
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"

    player_move = input("Choose [r]ock, [p]aper or [s]cissors:")

    # Formatting player input
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Try again...")

    computer_random_number = random.randint(1, 3)

    # This generates random computer choice
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(f"The computer chose {computer_move}")

    # Logic to determine the winner
    if player_move == rock and computer_move == scissors or player_move == paper and computer_move == rock or player_move == scissors and computer_move == paper:
        print(f"{Fore.GREEN}You win!{Style.RESET_ALL}")
    elif player_move == computer_move:
        print(f"{Fore.YELLOW}Draw!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}You lose!{Style.RESET_ALL}")

    # Logic to restart the game
    while True:
        answer = str(input("Type [yes] to play again, or [no] to quit:"))
        if answer in ("yes", "no"):
            break
        print("Invalid input.")
    if answer == "yes":
        continue
    else:
        print("Goodbye!")
        break
