from cgitb import text
import random
import string
import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.geometry("600x400")
window.title("Raad het woord")

##############
# Variabels
##############

label1 = tkinter.Label(window , text="Vul een word in" , font=("arial" , 40) )
entry = tkinter.Entry(window , width=40 )
label2 = tkinter.Label(window , text="4 tot 7 letters" , font=("arial" , 10) )


label1 = tkinter.Label(window , text="Vul een word in" , font=("arial" , 40) )

btn2 = tkinter.Button(window , text=" ")


points = 0
word = "a"
spin1 = "b"
lists = [[] for i in range(7)]

s1 = tkinter.Spinbox(window  )
s2 = tkinter.Spinbox(window  )
s3 = tkinter.Spinbox(window  )
s4 = tkinter.Spinbox(window  )
s5 = tkinter.Spinbox(window  )
s6 = tkinter.Spinbox(window  )
s7 = tkinter.Spinbox(window  )

#########################
# functions
#########################

def message_func(x , i): #message box function
    points = i
    if x == 1:
        title1 = "Goed gedaan"
        message1  = "Je heeft goed gedaan"
    elif x == 2:
        title1 = "Niet goed"
        message1  = "Je heeft het niet goed gedaan"
    else:
        title1 = "Nog een keer proberen"
        message1  = "Je heeft het niet goed gedaan , je kan nog een keer probern en jouw punten zijn " + str(i)
    
    massage = messagebox.showinfo(title=title1, message=message1  )

def new_window():  #this function will renew the page when the player won the game 
    btn2.grid_forget()
    s1.grid_forget()
    s2.grid_forget()
    s3.grid_forget()
    s4.grid_forget()
    s5.grid_forget()
    s6.grid_forget()
    s7.grid_forget()
    label1.config(text="Vul een word in")
    entry.grid(row= 9 ,  column=1  , pady=10  )
    btn1.config(text="submit" , command=function_button)
    btn1.grid(row=11 ,  column=1  , pady=20  )
    print("good job!")


def function_button2(): #this function check if the word is correct
    global word  , spin1 , lists , points
    len1 = len(word)
    if len1 >= 4 : 
            spin1 = s1.get() + s2.get() + s3.get() + s4.get()
            if len1 >= 5 :
                spin1 = s1.get() + s2.get() + s3.get() + s4.get() + s5.get()
                if len1 >=6:
                    spin1 = s1.get() + s2.get() + s3.get() + s4.get() + s5.get() + s6.get()
                    if len1 == 7:
                        spin1 = s1.get() + s2.get() + s3.get() + s4.get() + s5.get() + s6.get() + s7.get()
    if spin1 == word:
        message_func(1 , 0)
        new_window()
    else:
        if points == 0:
            message_func(2 , 0)
            new_window()
        else:
            message_func(3 , points)
            missing = ' '
            for letter in word:
                if letter not in spin1:
                    missing = missing+letter
            x = len(missing) - 1
            for i in range(x):
                points-=2
            print(x)
            missing = " "

def function_button(): #this function makes new window for the spin boxses and add lists to them
    global word , spin1 , lists , points
    label2.grid_forget()
    entry.grid_forget()
    btn1.grid_forget()

    label1.config(text="Raad het word")
    alphabets = string.ascii_lowercase
    alphabets_list = list(alphabets)

    x = 0
    word = entry.get()
    word_list =list(word)
    len1 = len(word)
    points = len1 * len1

    lists = [[] for i in range(len1)]
    for i in lists:
        for i in range (4):
            y = random.choice(alphabets_list) 
            lists[x].append(y)
        for i in range(1):
            lists[x].append(word_list[x])
        x+=1  

    if len1 >= 4: 
        s1.config( values=lists[0])
        s2.config(values=lists[1])
        s3.config( values=lists[2])
        s4.config( values=lists[3])
        s1.grid(row=2 ,  column=1)
        s2.grid(row=3 ,  column=1)
        s3.grid(row=4 , column=1)
        s4.grid(row=5 , column=1)
        if len1 >=5:
            s5.config( values=lists[4])
            s5.grid(row=6 , column=1)
            if len1 >=6:
                s6.config( values=lists[5])
                s6.grid(row=7 , column=1)
                if len1 == 7:
                    s7.config( values=lists[6])
                    s7.grid(row=8 , column=1)
    btn2.config(text="Doe een gok" , command=function_button2 )
    btn2.grid(row=11 , column=1)

##################
# widget placement
##################

label1.grid(row=1 , column=1   )
entry.grid(row= 9 ,  column=1  , pady=10  )
label2.grid(row=10 ,  column=1  , pady=20 )
btn1 = tkinter.Button(window , text="submit" , command=function_button)
btn1.grid(row=11 ,  column=1  , pady=20  )


window.mainloop()