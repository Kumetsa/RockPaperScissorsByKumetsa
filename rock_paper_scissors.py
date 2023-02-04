import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

player_name = input("Enter Player Name:") or "Unknown player"

player_score = 0
computer_score = 0
points_to_win = int(input("Choose number of games to win (min.1,max.10):"))
if points_to_win not in range(1, 11):
    print("Invalid input.")
    points_to_win = int(input("Choose number of games to win (min.1,max.10, default is 3) :")) or 3


while True:
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"

    player_move = input("Choose [r]ock, [p]aper or [s]cissors:")

    # Validating & Formatting player input
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("Invalid input. Try again...")
        continue

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

    # Logic to determine the winner and count score
    if player_move == rock and computer_move == scissors or player_move == paper and computer_move == rock or player_move == scissors and computer_move == paper:
        player_score += 1
        print(f"{Fore.GREEN}You win!{Style.RESET_ALL}")
    elif player_move == computer_move:
        print(f"{Fore.YELLOW}Draw!{Style.RESET_ALL}")
    else:
        computer_score += 1
        print(f"{Fore.RED}You lose!{Style.RESET_ALL}")

    print(f"Score: {player_name}:[{player_score}] | Computer:[{computer_score}]")
    # Logic to restart the game
    if player_score == points_to_win:
        print(f"Final score: {player_name}:[{player_score}] | Computer:[{computer_score}] ")
        print(f"{Fore.GREEN}{player_name} won !{Style.RESET_ALL}")
        player_score = 0
        computer_score = 0
        while True:
            answer = input("Type [yes] to play again or [no] to quit:")
            if answer in ("yes", "no"):
                break
        answer = input("Type [yes] to play again or [no] to quit:")
        if answer == "yes":
            continue
        if answer == "no":
            print("Goodbye!")
            break
    elif computer_score == points_to_win:
        print(f"Final score: {player_name}:[{player_score}] | Computer:[{computer_score}] ")
        print(f"{Fore.GREEN}Computer won !{Style.RESET_ALL}")
        player_score = 0
        computer_score = 0
        while True:
            answer = input("Type [yes] to play again or [no] to quit:")
            if answer in ("yes", "no"):
                break
        if answer == "yes":
            continue
        if answer == "no":
            print(f"{Fore.RED}Goodbye!{Style.RESET_ALL}")
            break
