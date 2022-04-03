from msilib.schema import ComboBox
import tkinter
from tkinter.ttk import Combobox  
import datetime

window =  tkinter.Tk()
window.geometry("650x100")
window.title("Days by date calculator")

#variabels 

#####################
# lists
#####################
days_month = [32 , 29 , 32 , 31 , 31 , 31 , 32 , 32 , 31 , 32 , 31 , 32]

months = [
    "January",
    "February ",
    "March ",
    "April ",
    "May ",
    "June ",
    "July ",
    "August ",
    "September ",
    "October ",
    "November ",
    "December ",
]

#####################
# widgets
#####################

comboBox_months = Combobox(window , value=months)
comboBox_days = Combobox(window)
yearEntry = tkinter.Entry(window ) 
result = tkinter.Label(window)

#####################
# functions
#####################

def dyas_counter(  x ): #appending days to months
    days_list = []
    for i in range(1 , x):
        days_list.append(i)
    comboBox_days.config(value=days_list)

def days_counter(event): #Making lists
    global  months , days_month
    month = months.index(comboBox_months.get())  
    dyas_counter(days_month[month])

def day_culc(): #Calculation of the entered day and todays day
    global months
    today = datetime.date.today()
    year = int(yearEntry.get())
    day = int(comboBox_days.get())
    month = months.index(comboBox_months.get()) + 1
    day2 = datetime.date(year , month , day)
    trill_day =  today  - day2 
    result_day = trill_day.days
    window.update()
    result.config(text="Er zijn {} dagen verstreken sinds deze datum ".format(result_day))
    if result_day <= 1 :
        result.config(text="Er zijn nog {} dagen tot deze datum".format(abs(result_day)))
        
###########################
# widget placment
###########################

comboBox_months.current(0)
comboBox_months.bind("<<ComboboxSelected>>" ,days_counter  )
comboBox_months.grid( column=1 , row=1 ,padx=10 , pady=10)

space1 = tkinter.Label(window , text=" - " ).grid(column=2 , row=1)

comboBox_days.grid( column=3 , row=1 ,padx=10 , pady=10) #Days combox placement

space2 = tkinter.Label(window , text=" - " ).grid(column=4 , row=1 , padx=10 , pady=10)

yearEntry.grid(column=5 , row=1  , padx=10 , pady=10 )  #Year entry placement

space3 = tkinter.Label(window , text=" - " ).grid(column=6 , row=1 , padx=10 , pady=10)

btn = tkinter.Button(window , text="Click" , command=day_culc   ) #Button placment

btn.grid(column=7 , row=1 , padx=10 , pady=10)

result.grid(column=1 , row=2 , padx=10 , pady=10)

window.mainloop()
