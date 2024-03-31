from tkinter import *
import string    
import random    
import pyperclip #for copying the password


##############################Functions###################################
#Generate Function
def Generate() :
    #Use characters functions of "string" library
    letters = string.ascii_letters
    numbers = string.digits
    specials= string.punctuation
    password_length = int(inputLenght.get())
    
    #Combine all characters
    characters = letters + numbers + specials

    #Show randomly the password in the output box by using sample method from "random" library
    
    if choice.get()==1:   #weak password contains letters only
        Password.insert(0, random.sample(letters, password_length))
    
    if choice.get()==2:   #medium password contains letters & numbers
        Password.insert(0, random.sample(letters+numbers, password_length))

    if choice.get()==3:    #strong password contains all characters
        Password.insert(0, random.sample(letters+numbers+specials, password_length))

#Copy function
def Copy() :
    pyperclip.copy(Password.get())

#Erase function
def Erase() :
    Password.delete(0, END)

##############################Main Interface###################################
#Call Tkinter
root = Tk()

#Some variables for styling
color_label1 = 'azure'
color_bg = 'sky blue'
choice= IntVar()  #type of the value button
label_txt = ('times new roman', 20, 'bold')
radio_txt = ('Arial',13,'bold')
input_txt = ('Cambria',10)

#Title
root.title("Password Generator")

#Favicon
root.iconbitmap(r'key.ico')

#Interface's Dimension
root.geometry('250x400')

#Interface's Background
root.config(background= color_bg)

#First Label
Label1 = Label(root, text='Password Generator', background= color_bg, #font='times new roman'
               font=label_txt, fg= color_label1)
Label1.grid()

#First Level Button
weakRadioButton = Radiobutton(root,text='Weak',value=1,variable=choice, font=radio_txt, bg='RoyalBlue1')
weakRadioButton.grid(pady=5)
#Second Level Button
mediumRadioButton = Radiobutton(root,text='Medium',value=2,variable=choice, font=radio_txt, bg='RoyalBlue2')
mediumRadioButton.grid(pady=5)
#Third Level Button
strongRadioButton = Radiobutton(root,text='Strong',value=3,variable=choice, font=radio_txt, bg='RoyalBlue3')
strongRadioButton.grid(pady=5)

#Second Label
Label2 = Label(root, text='Password Lenght', background= color_bg, #font='times new roman'
               font=label_txt, fg= color_label1)
Label2.grid()

#Input the Length
inputLenght = Spinbox(root, from_=5, to_=20, width=5, font=input_txt)
inputLenght.grid(pady=5)

#Generate Button
generateButton = Button(root, text='Generate' , font=radio_txt, command= Generate)
generateButton.grid(pady=5)

#Output the Password
Password = Entry(root, width=25, bd=2)
Password.grid()

#Copy Button
copyButton = Button(root, text='Copy' , font=radio_txt, command= Copy)
copyButton.grid(pady=5)

#Erase Button
eraseButton = Button(root, text='Erase' , font=radio_txt, command= Erase)
eraseButton.grid(pady=5)



#Display the window
root.mainloop()

