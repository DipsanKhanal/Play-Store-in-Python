import tkinter as tk
import random

win = tk.Tk()
win.geometry("1500x1500")
win.title("Rock-Paper-Scissors Game")
win.config(bg="#33FF57")

Rimg=tk.PhotoImage(file = "RPS\\rock.png")
Pimg=tk.PhotoImage(file = "RPS\\paper.png")
Simg = tk.PhotoImage(file = "RPS\\scissor.png")

# Variables to keep track of the scores
user_score = 0
computer_score = 0

# Define the function to handle the button clicks
def play_game(choice):
    global user_score
    global computer_score

    # Generate the computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Determine the winner
    result = None
    if choice == computer_choice:
        result = "tie"
    elif (choice == "rock" and computer_choice == "scissors") or \
         (choice == "paper" and computer_choice == "rock") or \
         (choice == "scissors" and computer_choice == "paper"):
        result = "you win"
        user_score += 1
    else:
        result = "you lose"
        computer_score += 1
    resultlabel.config(text=f"Result:\n\nYour Score: {user_score}\nComputer Score: {computer_score}")

    # Display the result
    result_label.config(text=f"Result: {result}\nYou chose {choice}\nComputer chose {computer_choice}\n\nYour Score: {user_score}\nComputer Score: {computer_score}")

# Create the buttons
rock_button = tk.Button(win, height = 110,width = 200, image=Rimg, command=lambda: play_game("rock"))
paper_button = tk.Button(win, height = 110,width = 200, image=Pimg, command=lambda: play_game("paper"))
scissors_button = tk.Button(win, height = 110,width = 200, image=Simg, command=lambda: play_game("scissors"))

# Place the buttons
rock_button.place(x =70 , y= 70)
paper_button.place(x =1200 , y=70)
scissors_button.place(x =700 , y=500)

# Create the result label
result_label = tk.Label(win, text="",bg= "red", font = ("Helvetica",20))
result_label.place(x = 650, y= 700)
resultlabel = tk.Label(win, text="",bg = "yellow", font = ("Helvetica",20))
resultlabel.place(x = 650, y= 150)
# Create the reset button
reset_button = tk.Button(win, text="Reset Scores",bg = "cyan", font = ("Helvetica",16), command=lambda: reset_scores())
reset_button.place(x = 690, y= 80)

# Define the reset scores function
def reset_scores():
    global user_score
    global computer_score
    user_score = 0
    computer_score = 0
    resultlabel.config(text=f"Result:\n\nYour Score: {user_score}\nComputer Score: {computer_score}")

win.mainloop()
