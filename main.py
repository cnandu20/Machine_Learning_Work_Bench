import algorithm.linear_regression as lr
import frames.linear_regression as lr

from tkinter import *



def linear():
    lr.lrframe()



def start():
    top = Tk()
    top.geometry("1200x750")
    top.maxsize(1200, 750)
    top.minsize(1200, 750)

    main = Frame(top)
    main.place(x=0, y=0, width=1200, height=700)

    welcome = Label(main, text="Machine Learning Workbench").place(x=100, y=268)

    category = Frame(main);
    category.place(x=1000, y=80, height=600)

    regression = Button(category, text="Linear Regression", command=linear).pack(side=TOP)

    top.mainloop()

start()

