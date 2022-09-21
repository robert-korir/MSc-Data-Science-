"""
2.PythonSubmission_Rock_Paper_Scissors

Create a Rock, Paper, Scissors game!

Simple UI with TKInter
Three buttons, for "Rock", "Paper" and "Scissors", each containing an image
After pressing one, the computer picks a random number between 1 and 3 and according to that number, chooses it's guess
If the player wins, display a string "YOU WIN!"
If the computer wins, display a string "YOU LOSE!"
If it's a tie, display a string "TIE!"
Write the points continuously in the results.txt file
How to get a random number: https://www.programiz.com/python-programming/examples/random-number

How to display an image on a button: https://www.geeksforgeeks.org/python-add-image-on-a-tkinter-button/
"""
import random
from random import randint
from tkinter import * 
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# here, image option is used to
# set image on button

player_choice = 0
computer_choice = 0
  
#Define a function for opening the Dialog box
def open_prompt(choice):
    print('choice', choice)

#implement user selection
def get_random_pick():
    choice = random.randint(1,3)
    return choice

def get_random_choice():
    print("In production")
    
# Creating a photoimage object to use image
rock = PhotoImage(file = r"C:\Users\ROBERT-KORIR\Documents\ObudaRevisions\rock.png")
scissors = PhotoImage(file = r"C:\Users\ROBERT-KORIR\Documents\ObudaRevisions\scissors.png")
paper = PhotoImage(file = r"C:\Users\ROBERT-KORIR\Documents\ObudaRevisions\paper.png")
Button(root, text = 'ROCK', image = rock, command=open_prompt(1)).pack(side = LEFT)
Button(root, text = 'SCISSORS', image = scissors, command=open_prompt(2)).pack(side = BOTTOM)
Button(root, text = 'PAPER !', image = paper, command=open_prompt(3)).pack(side = RIGHT)


root.mainloop()


    

