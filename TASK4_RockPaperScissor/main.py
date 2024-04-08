from tkinter import *
from random import randint   #INTEGER RANDOM NUMBERS
from PIL import Image, ImageTk   #DISPLAY IMAGES BY PILLOW LIBRARY

##Tkinter Tools##
root = Tk()
root.title("RockPaperScissor")
bg_color = "navajo white"
root.configure(background=bg_color)
root.iconbitmap(r'images/rpsgame.ico') #icon


########################Functions########################

#List of Choices
choice = ["rock", "paper", "scissor"]

#Rock Button Click Function
def rock():
    user = choice[0]  
    computer = choice[randint(0, 2)]
    user_label.config(image=rock_pic)
    auto(computer) 
    result(user, computer)
#Paper Button Click Function
def paper():
    user = choice[1]
    computer = choice[randint(0, 2)]
    user_label.config(image=paper_pic)
    auto(computer)
    result(user, computer)
#Scissor Button Click Function
def scissor():
    user = choice[2]
    computer = choice[randint(0, 2)]
    user_label.config(image=scissor_pic)
    auto(computer)
    result(user, computer)

#Computer Choice Function
def auto(computer):
    if computer == "rock":
        computer_label.config(image=rock_pic)
    elif computer == "paper":
        computer_label.config(image=paper_pic)
    else:
        computer_label.config(image=scissor_pic)

#Check Result by message and updating score
def result(user, computer):
    global user_score, computer_score
    if user == computer:
        mssg.config(text="It's a tie this time!", fg="orange", font=('Arial', 20 , 'bold'))
    elif (user == "rock" and computer == "paper") or (user == "paper" and computer == "scissor") or (user == "scissor" and computer == "rock"):
        #the computer win
        Cscore = int(computer_score['text'])
        Cscore += 1
        computer_score.config(text=str(Cscore))
        mssg.config(text="You lost this time" , fg="red2", font=('Arial', 20 , 'bold'))
    else:
        #the user win
        Uscore = int(user_score['text'])
        Uscore += 1
        user_score.config(text=str(Uscore))
        mssg.config(text="You won this time" , fg="green3", font=('Arial', 20 , 'bold'))

#Buttons
radbutton= IntVar() #Variable of buttons to make only one choice
rock_button = Radiobutton(root, text="Rock", value=1, variable=radbutton , 
                          command=rock, bg="turquoise", width=20)
paper_button = Radiobutton(root, text="Paper", value=2, variable=radbutton , 
                           command=paper, bg="orange red", width=20)
scissor_button = Radiobutton(root, text="Scissor", value=3, variable=radbutton , 
                             command=scissor, bg="yellow green", width=20)

#Choose Click Button
def choose() :
    txt_label = Label(root, bg=bg_color, text="Choose", font=('time new roman', 13), 
                      width= 20, height=2).grid(row=0, column=2, pady=4, padx=4)
    rock_button.grid(row=1, column=1)
    paper_button.grid(row=1, column=2)
    scissor_button.grid(row=1, column=3)

#Start New Game; when clicking it, user can "choose" a button
def new() :
    #hide buttons
    rock_button.grid_forget()
    paper_button.grid_forget()
    scissor_button.grid_forget()
    #initialize scores, message and pictures
    mssg.config(text="") 
    computer_score.config(text=0)
    user_score.config(text=0)
    computer_label.config(image=computer_pic)
    user_label.config(image=user_pic)
    #show the button of the ready to display the 3 buttons (rock, paper, scissor)
    ready = Button(root, text="Ready.....  Start!", command=choose, width=15, 
                   fg="snow" , bg="chocolate", font=('arial', 10), 
                   pady=4, padx=4).grid(row=0 , column=2)
    



########################Interface GUI########################

#pictures
rock_pic = ImageTk.PhotoImage(Image.open("images/rock.png"))
paper_pic = ImageTk.PhotoImage(Image.open("images/paper.png"))
scissor_pic = ImageTk.PhotoImage(Image.open("images/scissor.png"))
computer_pic = ImageTk.PhotoImage(Image.open("images/computer.png"))
user_pic = ImageTk.PhotoImage(Image.open("images/player.png"))


###User_part
#Picture
user_label = Label(root, image=user_pic, background=bg_color, width=300, height=300)
user_label.grid(row=2, column=0)
#Score
user_score = Label(root, bg=bg_color, text=0 , font=('Arial', 20 , 'bold'))
user_score.grid(row=2, column=1)
#Title
user_title = Label(root, bg=bg_color, text="YOU", font=('cambria', 15, 'bold'))
user_title.grid(row=3, column=0)

###Computer_part
#Picture
computer_label = Label(root, image=computer_pic, background=bg_color, width= 300, height=300)
computer_label.grid(row=2, column=4)
#Score
computer_score = Label(root, bg=bg_color, text=0, font=('Arial', 20 , 'bold'))
computer_score.grid(row=2, column=3)
#Title
computer_title = Label(root, bg=bg_color, text="COMPUTER", font=('cambria', 15, 'bold'))
computer_title.grid(row=3, column=4)

#Message; it will be appeared at least the player play the first time 
mssg = Label(root, text="", bg=bg_color)
mssg.grid(row=4, column=2)

#New Game
newGame = Button(root, text="New Game", command=new, bg="gold", width=15, 
                 font=('time new roman', 15)).grid(row=5, column=2, padx=4, pady=4)

#Display the window
root.mainloop()
