import random

'''1 for snake
-1 for water
0 for gun'''

# Correct the random.choice syntax
computer = random.choice([1, -1, 0])

youstr = input("Enter your choice (s for snake, w for water, g for gun): ").strip().lower()
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

# Ensure the input is valid
if youstr not in youDict:
    print("Invalid choice. Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw")
    elif (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
        print("You win!")
    elif (computer == 1 and you == -1) or (computer == -1 and you == 0) or (computer == 0 and you == 1):
        print("You lose!")
    else:
        print("Something went wrong")
