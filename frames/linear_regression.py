from tkinter import *
from tkinter.filedialog import askopenfile
import  os

def lrframe():
    print("called succeful")
    lr=Frame()
    lr.place(x=0,y=0,width=1200,height=750)

    user=Frame(lr,bd=2).place(x=800,width=400,height=750)



    l1 =Label(user, text="Trainset")
    l2 = Label(user, text="Gradient:")
    l3 = Label(user, text="Intersect:")
    l4 = Label(user, text="Epoch:")
    l5 = Label(user, text="Learning rate:")

    l1.place(x = 810, y = 50)
    l2.place(x = 810, y = 120)
    l3.place(x = 810, y = 190)
    l4.place(x = 810, y = 260)
    l5.place(x=810, y=320)



    button1 = Button(user, text="Upload Dataset", command=fileopen)
    m = Entry(user)
    b = Entry(user)
    epoch = Entry(user)
    L = Entry(user)
    button2 = Button(user, text="Train Model")

    # this will arrange  widgets

    button1.place(x = 950,y = 50)
    m.place(x = 950, y = 120)
    b.place(x = 950, y = 190)
    epoch.place(x = 950, y = 260)
    L.place(x = 950,y = 320)
    button2.place(x = 1000 , y = 360)



    title=Label(lr,text="Linear Regression").place(x=290,y=50)


def fileopen():
    file= askopenfile(mode ='r', filetypes =[('CSV Files', '*.csv')])
    if(file):
        path = os.path.abspath(file.name)
        Label(text=str(path)).place(x = 805 ,y = 75)



