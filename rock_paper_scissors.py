import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

# Score counter
player_score = 0
computer_score = 0
draws = 0

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

    # Logic to determine the winner and count score
    if player_move == rock and computer_move == scissors or player_move == paper and computer_move == rock or player_move == scissors and computer_move == paper:
        player_score += 1
        print(f"{Fore.GREEN}You win!{Style.RESET_ALL}")
    elif player_move == computer_move:
        draws += 1
        print(f"{Fore.YELLOW}Draw!{Style.RESET_ALL}")
    else:
        computer_score += 1
        print(f"{Fore.RED}You lose!{Style.RESET_ALL}")

    print(f"Current score: Player:[{player_score}] | Draws:[{draws}] | Computer:[{computer_score}]")
    # Logic to restart the game
    while True:
        answer = str(input("Type [yes] to play again, or [no] to quit:"))
        if answer in ("yes", "no"):
            break
        print("Invalid input.")
    if answer == "yes":
        continue
    else:
        print(f"Final score: Player:[{player_score}] | Draws:[{draws}] | Computer:[{computer_score}] ")
        print("Goodbye!")
        break
