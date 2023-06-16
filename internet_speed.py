# Internet Speed Tester using Python

from tkinter import *
from tkinter import messagebox
import pyspeedtest

def logic():
     st=pyspeedtest.SpeedTest("www.google.com")
     a=(str(st.download()) + "[Bytes per second]")
     messagebox.showinfo("Your Download speed:",a)
     


top=Tk()
top.title('AK speed Test')
top.geometry('1000x500')
filename=PhotoImage(file="images/internet.png")
background_label=Label(top,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

b=Button(top,text='Click to see the Internet speed',font=('San serif',20),bg='Yellow',height=1,width=30,command=logic).pack()
top.mainloop()