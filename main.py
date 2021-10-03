import random

moves = {
    "p": "r",
    "r": "s",
    "s": "p"
}

cpu = random.choice(list(moves.keys()))
player = input("r/p/s? ")

if player not in moves:
    print("Invalid move")
    exit()

print(f"Computer choose {cpu}")

if cpu == player:
    print("It's a tie")
elif moves[player] == cpu:
    print("You win")
else:
    print("You loose") 