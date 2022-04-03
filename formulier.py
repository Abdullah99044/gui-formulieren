from msilib.schema import CheckBox
import tkinter
from tkinter import messagebox
from typing_extensions import IntVar

window = tkinter.Tk()
window.geometry("1000x500")
window.title("Sports Club Membership")

####################
# Widgets
####################

nameLabel = tkinter.Label(window , text="Name              :" , font=("arial" , 18) )

firstEntry = tkinter.Entry(window  )
lasttEntry = tkinter.Entry(window )

emaillabael = tkinter.Label(window , text="Email              :" , font=("arial" , 18)  )
emailEntry = tkinter.Entry(window , )

phoneLabel = tkinter.Label(window ,text="Phone            :" , font=("arial" , 18))
phoneEntry = tkinter.Entry(window , )

adresLabel = tkinter.Label(window , text="Adres              :", font=("arial" , 18))
streetEntry = tkinter.Entry(window )
cityEntry = tkinter.Entry(window )
postCode = tkinter.Entry(window)


datumLabel = tkinter.Label(window , text="your age         :", font=("arial" , 18))
dayEntry = tkinter.Entry(window )
monthEntry = tkinter.Entry(window )
yearEntry = tkinter.Entry(window )




variable = tkinter.IntVar()

keuzen = tkinter.Label(window )
tkinter.Radiobutton(window , text="Football" , font=("arial" , 12) , variable=variable , value=1).grid(row=9 , column=1 , sticky=tkinter.W)
tkinter.Radiobutton(window , text="Hockey" , font=("arial" , 12) , variable=variable , value=2).grid(row=10 , column=1 , sticky=tkinter.W)
tkinter.Radiobutton(window , text="Tennis" , font=("arial" , 12) , variable=variable , value=3).grid(row=11 , column=1 , sticky=tkinter.W)
tkinter.Radiobutton(window , text="Shuttle" , font=("arial" , 12) , variable=variable , value=4).grid(row=12 , column=1 , sticky=tkinter.W) 

argment = tkinter.StringVar()

x =  tkinter.IntVar()
termsLabel = tkinter.Label(window , text="Terms of Service" , font=("arial" , 18))
termsCheck = tkinter.Checkbutton(window , text="I agree to the terms of service" , font=("arial" , 10)   ,variable = x)




#################
# functions
#################

def message(x , z): #Information message for the user
    if x == 1:
        true = messagebox.showinfo(title="True information" , message=" Done")
    if x == 0:
        false = messagebox.showinfo(title="false information" , message="Check the your information ({})".format(str(z)))
 
def check_function(): #This function will check the input information
    global x

    entry = [firstEntry.get() , lasttEntry.get() , emailEntry.get() , phoneEntry.get() , streetEntry.get() , cityEntry.get() , postCode.get() , dayEntry.get() , monthEntry.get() , yearEntry.get() ]
    entry_name = ["first name"  , "last name  " , "email" , "phone" , "street adres" , "city name" , "postcode" , "day" , "month" , "year"]

    year = int(yearEntry.get())
    month = int(monthEntry.get())

    if year <= 2004:
        print("true age")
        if x.get()  :
            print("true check box")
            if tkinter.Radiobutton:
                print("True radio button")
                if month < 12:
                    print("true month")
                    r = 8
                    z = 0
                    chance = 12
                    for i in entry:
                        if len(entry[0]) == 0:
                            for ra in range(1):
                                print("flase " + entry_name[z])
                                btn.config(command=check_function)
                                chance-=1
                        else :
                            for rb in range(1):
                                print("true " +  entry_name[z])
                                
                                btn.config(command=check_function)
                                chance+=1
                        z+=1
                        r+=1
                    if chance < 12:
                        message(0 , "Enter your information")
                    else:
                        message(1 , 0)

                else:
                    message(0 , " invalid month")
            else:
                message(0 , "Chose one sport")
        else:
            message(0 , "Accept terms of use")
    else:
        message(0 , "You have to be 18 or older")
     

##########################
# widget placement
##########################

#Name 
 


nameLabel.grid(row=1 , column=1 , padx=2, pady=2 , sticky=tkinter.W)
firstEntry.grid(row=1 , column=3 , padx=2 , pady=2 , ipadx=10 )
lasttEntry.grid(row=1 , column=5 , padx=2, pady=2 , ipadx=10)
firstEntry_label = tkinter.Label(window , text="First name  " , font=("arial" , 10) ).grid(row=1 , column=2 , sticky=tkinter.W)
lasttEntry_label = tkinter.Label(window , text=" Last name  " , font=("arial" , 10) ).grid(row=1 , column=4 , sticky=tkinter.W)

#email

emaillabael.grid(row=2 , column=1 , padx=2 , pady=2 , sticky=tkinter.W)
emailEntry.grid(row=2 , column=3 , padx=2 , pady=2 , ipadx=10 ) 
emailEntry_label = tkinter.Label(window , text="email  " , font=("arial" , 10) ).grid(row=2 , column=2 , sticky=tkinter.W)
 

#phone

phoneLabel.grid(row=3 , column=1 , padx=2 , pady=2 , sticky=tkinter.W)
phoneEntry.grid(row=3 , column=3 , padx=2 , pady=2 , ipadx=10)  
phoneEntry_label = tkinter.Label(window , text="phone  " , font=("arial" , 10) ).grid(row=3 , column=2 , sticky=tkinter.W)

#Adres

adresLabel.grid(row=4 , column=1 , padx=2 , pady=2 , sticky=tkinter.W)

cityEntry.grid(row=4 , column=3 , padx=10 , pady=10 , ipadx=10)  
cityEntry_label = tkinter.Label(window , text="city  " , font=("arial" , 10) ).grid(row=4 , column=2 , sticky=tkinter.W)

streetEntry.grid(row=4 , column=5 , padx=10 , pady=10   , ipadx=10)  
streetEntry_label = tkinter.Label(window , text="street  " , font=("arial" , 10) ).grid(row=4 , column=4 , sticky=tkinter.W)

postCode.grid(row=4 , column=7 , padx=10 , pady=10 ,   ipadx=10)  
postcodeEntry_label = tkinter.Label(window , text="postcode  " , font=("arial" , 10) ).grid(row=4 , column=6 , sticky=tkinter.W)

#Birth day

datumLabel.grid(row=5 , column=1 , padx=2 , pady=2 , sticky=tkinter.W)

dayEntry.grid(row=5 , column=3 , padx=10 , pady=10 , ipadx=10)  
dayEntry_label = tkinter.Label(window , text="day  " , font=("arial" , 10) ).grid(row=5 , column=2 , sticky=tkinter.W)

monthEntry.grid(row=5 , column=5 , padx=10 , pady=10 , ipadx=10)
monthEntry_label = tkinter.Label(window , text="month  " , font=("arial" , 10) ).grid(row=5 , column=4 , sticky=tkinter.W)

yearEntry.grid(row=5 , column=7 , padx=10 , pady=10 , ipadx=10)  
yearEntry_label = tkinter.Label(window , text="year  " , font=("arial" , 10) ).grid(row=5 , column=6 , sticky=tkinter.W)

#Terms

termsLabel.grid(row=6 , column=1 ,padx=2 , pady=10 , sticky=tkinter.W )
termsCheck.grid(row=7 , column=1 , padx=2 , pady=2 , sticky=tkinter.W)

#button

btn = tkinter.Button(window , text="Submit" , command=check_function)
btn.grid(row=13 , column=2 , padx=10 , pady=15 , ipadx=10  )


window.mainloop()

