from cgitb import enable, text
from faulthandler import disable
from os import stat
from pickle import TRUE
from sre_parse import State
import tkinter
from tkinter import DISABLED, NORMAL, Checkbutton, Event, Label, StringVar, font
from tkinter.constants import E, N
from typing import Text

window = tkinter.Tk()
window.title("Clicket v4")
window.configure(bg="gray")
window.geometry("700x500")

number = 0
n = str(number)


label = tkinter.Label( window , text=number , font=("Arial" , 15) , bg="white" , width = 20 , fg="black" )

def checkBox_func():
    global number 
    window.update()
    while TRUE:
        window.after(200 )
        counter_func(1)

argment = StringVar()


checkBox =  Checkbutton(window  , text="check" , state=DISABLED ,  command=checkBox_func  ,variable=argment , onvalue="agree" , offvalue="disagree") 


def Chechbox_enable():
    return checkBox.config(state=NORMAL)

def counter_func(num):
    global number , n
    number += num
    labe(number)
    if number > 0:
        window.update()
        window.configure(bg="green")
        Chechbox_enable()
    elif number == 0:
        window.update()
        window.configure(bg="gray")
    elif number < 0:
        window.update()
        window.configure(bg="Red")
        Chechbox_enable()


def up_func(event):
    counter_func(1)

def labe(n):
    window.update()
    label.configure(text=str(n))      

def down_func(event):
    counter_func(-1)

def crusorIn_func(event):
    print(str(event))
    window.update()
    window.configure(bg="yellow")   
    
    

def crusorOut_func(event):
    global number
    if number > 0:
        window.update()
        window.configure(bg="green")
    elif number == 0:
        window.update()
        window.configure(bg="gray")
    elif number < 0:
        window.update()
        window.configure(bg="Red")

    

def click_Up(event):
    global number
    print(str(event))
    if number > 0:
        number = number + 3
        n = str(number)
    elif number < 0:
        number = number - 3
        n = str(number)
    window.update()
    label.configure(text=n)

   

checkBox.deselect()
checkBox.pack()




btn1 = tkinter.Button(window , text="Up" , font=("Arial" , 15) , width = 20, bg="white" , fg="black" , command= lambda :  up_func(Event)    )
btn1.pack(
    pady=50,
    padx=40,
    expand=True
)

label.pack(
    pady=40,
    padx=40,
    expand=True
)


btn2 = tkinter.Button(window , text="Down" , font=("Arial" , 15) , width = 20 , bg="white" , fg="black" , command= lambda : down_func(Event)    )
btn2.pack(
    pady=40,
    padx=40,
    expand=True
)

label.bind("<Enter>" , crusorIn_func )
label.bind("<Leave>" , crusorOut_func)
label.bind("<Double-Button>",  click_Up  )

window.bind("<Up>",up_func)
window.bind("<+>",up_func)

window.bind("<Down>",down_func)
window.bind("-",down_func)

window.bind("<space>",click_Up )
 
 
window.mainloop()