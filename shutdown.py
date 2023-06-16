from tkinter import *
import os
root=Tk()
root.title("ShutDown")
root.geometry("400x500")

def restarttime():
    return os.system("c:\Windows\System32\shutdown.exe /r /t 30")

def restart():
    os.system("c:\Windows\System32\shutdown.exe /r /t 1") 

def shutdown():
    os.system("c:\Windows\System32\shutdown.exe /s /t 1")       

# first button
restart_time_button=PhotoImage(file="images/restart.png")
first_button=Button(root,image=restart_time_button,borderwidth=0,cursor="hand2",command=restarttime)
first_button.place(x=10,y=10)

# second button
close_button=PhotoImage(file="images/close.png")
second_button=Button(root,image=close_button,borderwidth=0,cursor="hand2",command=root.destroy)
second_button.place(x=200,y=10)

# third button
restart_button=PhotoImage(file="images/restart1.png")
third_button=Button(root,image=restart_button,borderwidth=0,cursor="hand2",command=restart)
third_button.place(x=10,y=200)

# fourth button
shutdown_button=PhotoImage(file="images/shutdown.png")
fourth_button=Button(root,image=shutdown_button,borderwidth=0,cursor="hand2",command=shutdown)
fourth_button.place(x=200,y=200)

root.mainloop()