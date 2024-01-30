import random
import re

pattern = re.compile(r"\b(rock|paper|scissors)\b", re.IGNORECASE)

user_input = input("Enter your rock, paper, scissor choice: ")
match_input = pattern.search(user_input)

while not match_input:
    user_input = input("Enter your rock, paper, scissor choice: ")
    match_input = pattern.search(user_input)

player_choice = match_input.group().lower()

rps_random_seed = random.randint(0, 2)
match rps_random_seed:
    case 0:
        rps_bot_choice = "rock"
    case 1:
        rps_bot_choice = "paper"
    case 2:
        rps_bot_choice = "scissor"
print(f"RPS bot chooses {rps_bot_choice}")

if player_choice == rps_bot_choice:
    print("TIE")
elif player_choice == "rock":
    if rps_bot_choice == "paper":
        print("RPS Bot WINS")
    else:
        print("Player WINS")
elif player_choice == "paper":
    if rps_bot_choice == "scissor":
        print("RPS Bot WINS")
    else:
        print("Player WINS")
elif player_choice == "scissor":
    if rps_bot_choice == "rock":
        print("RPS Bot WINS")
    else:
        print("Player WINS")



    