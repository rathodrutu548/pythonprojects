import tkinter
from tkinter import *

root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_List=[]

def addtask():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_List.append(task)
        listbox.insert(END,task)

def deletetask():
    global task_List
    task=str(listbox.get(ANCHOR))
    if task in task_List:
        task_List.remove(task)
        with open("tasklist.txt","w") as taskfile:
            for task in task_List:
                taskfile.write(task+"\n")
    listbox.delete(ANCHOR)            
def opentaskfile():
    try:
        global task_List
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task!='\n':
                task_List.append(task)
                listbox.imsert(END,task)
    except:
        file=open('tasklist.txt','w')
        file.close()
# icon
Image_icon=PhotoImage(file="images/task.png")
root.iconphoto(False,Image_icon)

# Topbar
TopImage=PhotoImage(file="images/topbar.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="images/dock.png")
Label(root,image=dockImage,bg='#32405b').place(x=30,y=25)

noteImage=PhotoImage(file="images/task.png")
Label(root,image=noteImage,bg='#32405b').place(x=340,y=25)

heading=Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg='#32405b')
heading.place(x=130,y=20)

# main
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)

button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg='#5a95ff',fg="white",bd=0,command=addtask)
button.place(x=300,y=0)

# listbox
frame1=Frame(root,bd=3,width=700,height=280,bg='#32405b')
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg='#32405b',fg="white",cursor="hand2",selectbackground='#5a95ff')
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

opentaskfile()

# delete
Delete_icon=PhotoImage(file="images/delete.png")
Button(root,image=Delete_icon,bd=0,command=deletetask).pack(side=BOTTOM,pady=13)

root.mainloop()