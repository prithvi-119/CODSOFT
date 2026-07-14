import random

choices = ["rock", "paper", "scissors"]

wins = 0
losses = 0
draws = 0

while True:

    computer = random.choice(choices)

    player = input("\nEnter rock, paper, or scissors: ").lower()

    if player not in choices:
        print("Invalid Choice!")
        continue

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("Draw!")
        draws += 1

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You Win!")
        wins += 1

    else:
        print("Computer Wins!")
        losses += 1

    print("\n------ Score ------")
    print("Wins   :", wins)
    print("Losses :", losses)
    print("Draws  :", draws)

    again = input("\nPlay again? (yes/no): ").lower()

    if again != "yes":
        print("\nFinal Score")
        print("Wins   :", wins)
        print("Losses :", losses)
        print("Draws  :", draws)
        print("Thanks for playing!")
        break