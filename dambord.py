import tkinter  


window =  tkinter.Tk()
window.geometry("500x500")
window.title("Dambord")

x = 0
z = 0
y = 1 
z1 = 1
def return_zer0()->int:
    global x , y 
    x = 0
    y = 1
    return

 
window.rowconfigure(0,weight=2)
window.columnconfigure(0,weight=0)
 

for j in range(10):
    for i in range(5):
        tkinter.Frame(window  , bg="white").grid(column=x , row=z  , padx= 10 , pady= 10   )  
        tkinter.Label(window , bg="black").grid(column=y , row=z    , ipadx= 35 , ipady= 30  ) 
        tkinter.Label(window , bg="white").grid(column=y , row=z1   , ipadx= 35 , ipady= 30   )
        tkinter.Label(window , bg="black").grid(column=x , row=z1    , ipadx= 35 , ipady= 30  ) 
        x+=2
        y+=2
    return_zer0()
    z+=2
    z1+=2
     
 
 
    
    

window.mainloop()