from ast import Lambda
import random
from tkinter import *

#Var && Dictionaries
comp_score = 0
player_score = 0

#Logic
def outcome_handler(user_choice):
    global comp_score
    global player_score
    outcomes = ["rock","paper","scissors"]
    random_number = random.randint(0,2)
    computer_choice = outcomes[random_number]
    print(outcomes[random_number])

# Screen
master = Tk()
master.title("RPS")

#Labels
Label(master,text="Rock - Paper - Scissors",font=("Calibri",14)).grid(row=0,sticky=N,pady=10,padx=200)
Label(master,text="Select an Option",font=("Calibri",12)).grid(row=1,sticky=N)
player_score_label = Label(master,text="Player : 0",font=("Calibri",12))
player_score_label.grid(row=2,sticky=W)
computer_score_label = Label(master,text="Computer : 0",font=("Calibri",12))
computer_score_label.grid(row=2,sticky=E)
player_choice_label = Label(master,font=("Calibri",12))
player_choice_label.grid(row=3,sticky=W)
computer_choice_label = Label(master,font=("Calibri",12))
computer_choice_label.grid(row=3,sticky=E)
outcome_label = Label(master,font=("Calibri",12))
outcome_label.grid(row=3,sticky=N)

#Buttons
Button(master,text="Rock",command=lambda:outcome_handler("rock")).grid(row=4,sticky=W,padx=5,pady=5)
Button(master,text="Paper",command=lambda:outcome_handler("paper")).grid(row=4,sticky=N,padx=5,pady=5)
Button(master,text="Scissors",command=lambda:outcome_handler("scissors")).grid(row=4,sticky=E,padx=5,pady=5)
master.mainloop()

Label(master).grid(row=5) #Dummy Label