'''
Tic-Tac-Toe
Author: Craig Conover
'''

from tkinter import *
import random

# Next turn, determines when to switch players turns.
def next_turn(row, column):
    
    global player

    # Evaluates 
    if buttons[row][column]['text'] == "" and check_winner() is False:
        
        # If first player, check winner and announce winner or switch player
        if player == players[0]:

            buttons[row][column]['text'] = player

            # No winner yet, switch player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            # Player one wins the game
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            # Game is a tie
            elif check_winner() == 'Tie':
                label.config(text=(" Tie"))

        # If second player, check winner and announce winner or switch player
        else:

            buttons[row][column]['text'] = player

            # No winner yet, switch player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            # Player two wins the game
            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            # Game is a tie
            elif check_winner() == 'Tie':
                label.config(text=(" Tie"))

# Check if there is a winner and if so display the winner
def check_winner():
    
    # Check rows for a winner
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg='green')
            buttons[row][1].config(bg='green')
            buttons[row][2].config(bg='green')
            return True

    # Check columns for a winner
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg='green')
            buttons[1][column].config(bg='green')
            buttons[2][column].config(bg='green')
            return True

    # Check diagnally from top left to bottom right for a winner
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True

    # Check diagnally from top right to bottom left for a winner
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True

    # Check for a tie by having no winner no spaces left
    elif empty_spaces() is False:

        # How to style and display a tie
        for row in range(3):
            for column in range(3):
               buttons[row][column].config(bg='yellow') 
        return "Tie"

    else:
        return False

# Check for empty spaces
def empty_spaces():
    
    spaces = 9
    # If empty spaces exist return True otherwise return False
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -=1

    if spaces == 0:
        return False
    else:
        return True

# Starting a new game
def new_game():

    global player

    # Randomly select player to start
    player = random.choice(players)

    label.config(text=player+' turn')

    # Clear board, remove all x's, o's, and reset board colors
    for row in range(3):
         for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

# Set the board using tkinter
window = Tk()
window.title('Tic-Tac-Toe')
players = ['x','o']
player = random.choice(players)
buttons = [[0,0,0],
            [0,0,0],
            [0,0,0]]

# Display the Player that will go first
label = Label(text= player + ' turn', font=('consolas',40))
label.pack(side='top')

# New Game button configuration
reset_button = Button(text='restart', font=('consolas',20),  command=new_game)

reset_button.pack(side='top')

frame = Frame(window)
frame.pack()

# Game board configuration
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2, command= lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row,column=column)
    

window.mainloop()