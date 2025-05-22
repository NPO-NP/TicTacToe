''' 
You can add your own functions and variables to this file.
You will have to implement the logic for the 3 game modes.
You will decide the input format and ignore data validation for now.
'''

import os

# --------- Function definitions ---------------
def displayMenu():
    os.system('cls')            # clear the screen
    print("1. Human vs Human")
    print("2. Human vs AI")
    print("3. Your AI vs friend's AI")
    print("4. Quit")
    print()
    choice = int(input("Your choice: ")) 
    return choice

def displayBoard( board, choice):
    os.system('cls')            # clear the screen
    if choice == H_vs_H:
        print("Human vs Human")
    elif choice == H_vs_AI:
        print("Human vs AI")
    else:
        print("AI vs AI")

    print("-------------")
    for row in board:
        print("| {} | {} | {} |".format(row[0], row[1], row[2]))
    print("-------------")

# ----------- variable and constant declarations -------------
# Playing board is represented by a list of 3 lists. Each sub-list is a row on the board
# Each column of each row is either Player 1 (O), Player 2 (X) or empty (-)
board = [ ['-','-','-'], \
          ['-','-','-'], \
          ['-','-','-']]     

H_vs_H = 1      # constant to represent human vs human  
H_vs_AI = 2     # constant to represent human vs AI
AI_vs_AI = 3    # constant to represent AI vs AI
QUIT = 4
PLAYER1 = 'O'   # player 1 token
PLAYER2 = 'X'   # player 2 token

# ----------- start of main logic ---------------
choice = displayMenu()  # 1:H vs H, 2:H vs AI, 3:AI vs AI

while not (choice == QUIT):
    displayBoard(board, choice)

    # Whichever choice you implement, need to check for win or draw. 
    # Display menu and break out of while loop if exit is chosen

    if choice == H_vs_H:
        print("Player 1")
        # implement logic for 2 human players

    elif choice == H_vs_AI:   # comment out if you are not ready to implement this
        print("Human's move")
        # implement logic for human vs AI, including the AI algorithm
    
    else:  # comment out if you are not ready to implement this
        print("My AI vs friend's AI")
        #implement logic to use your AI vs a friend's AI

    
    input()  # dummy input to pause the loop. Remove it when you are ready to implement any of the game modes


os.exit(0)

    