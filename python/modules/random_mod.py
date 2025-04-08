import random
import math
# print(random)


# __________MODULES_____

# 1.random()
# 2.randint()
# 3.randrange()
# 4.choice()
# 5.choices()


# random()
# ran=random.random()*10000
# num=math.floor(ran//1)
# print(num)


# randint()
# print(random.randint(1000,9999))

# randrange()
# print(random.randrange(100,999,10))



# choice()
# print(random.choice(["red","green","orange","blue","yellow","white"]))


# choices()
# print(random.choices([1,2,3,4,5,6,7,8,42,65,49,68,96,89,98,29],k=3))
# print(random.choices(["red","green","orange","blue","yellow","white"],k=2))



# GAME DEVELOPMENT

# 1."Write a Python program that selects a random number between 1 and 12. The user has three attempts "
# "to guess the correct number. After each incorrect guess, the program should prompt the user to try "
# "again. If the user runs out of attempts, the correct number should be displayed."


# num=random.randint(1,12)
# turns=3
# for i in range(1,4):
#     user_input=int(input("Enter the guess number: "))
#     if user_input==num:
#         print("Correct Guess!!!")
#         break
#     else:
#         print("Try Again!!!")
#         turns-=1


# if turns==0:
#     print(f"the correct number is the {num}")




# GAME-2

# 2."Write a Python program where two players roll a dice, and the game continues until one of the"
# " players reaches a target score of 25. Players must input their dice rolls manually, and "
# "the game checks if the input is valid."

target = 25
player1 = 0
player2 = 0

# Game continues until one of the players reaches the target
while player1 < target and player2 < target:
    # Roll the dice for player 1
    while True:
        try:
            user1 = int(input("Roll the dice, Player 1 (Enter a number between 1 and 6): "))
            if 1 <= user1 <= 6:
                player1 += user1
                print(f"Player 1 rolled {user1} and now has {player1} points.")
                break
            else:
                print("Invalid roll! Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 6.")
    
    # Check if Player 1 wins
    if player1 >= target:
        print("Player 1 is the winner!!!")
        break

    # Roll the dice for player 2
    while True:
        try:
            user2 = int(input("Roll the dice, Player 2 (Enter a number between 1 and 6): "))
            if 1 <= user2 <= 6:
                player2 += user2
                print(f"Player 2 rolled {user2} and now has {player2} points.")
                break
            else:
                print("Invalid roll! Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 6.")
    
    # Check if Player 2 wins
    if player2 >= target:
        print("Player 2 is the winner!!!")
        break
