from tkinter import *
from tkinter.filedialog import askopenfile
import  os

def lrframe():
    print("called succeful")
    lr=Frame(bg='blue')
    lr.place(x=0,y=0,width=1200,height=750)
    print(lr)

    # user=Frame(lr,bg='red')
    # user.place(x=800,width=400,height=750)
    # print(user)
    backbtn=Button(lr,text="go back",command=lambda :back(lr))
    backbtn.place(x=25,y=25)

    l1 =Label(lr, text="Trainset")
    l2 = Label(lr, text="Gradient:")
    l3 = Label(lr, text="Intersect:")
    l4 = Label(lr, text="Epoch:")
    l5 = Label(lr, text="Learning rate:")

    l1.place(x = 810, y = 50)
    l2.place(x = 810, y = 120)
    l3.place(x = 810, y = 190)
    l4.place(x = 810, y = 260)
    l5.place(x=810, y=320)



    button1 = Button(lr, text="Upload Dataset", command=fileopen)
    m = Entry(lr)
    b = Entry(lr)
    epoch = Entry(lr)
    L = Entry(lr)
    button2 = Button(lr, text="Train Model")

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



def back(lr):
    lr.destroy()