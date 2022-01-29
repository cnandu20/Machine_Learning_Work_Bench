
import Machine_Learning_Work_Bench.frames.linear_regression as lr
import Machine_Learning_Work_Bench.frames.logistic_regression  as lg
import Machine_Learning_Work_Bench.frames.knn_frame  as knn_alg
import Machine_Learning_Work_Bench.frames.svm_frame as svm


from tkinter import *



def linear():
    lr.lrframe()

def lgf():
    lg.lgframe()

def knnfun():
    knn_alg.knnframe()

def svmfun():
    svm.svmframe()



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

    logistic_regression = Button(category, text="Logistic Regression", command=lgf).pack(side=TOP)

    knn = Button(category, text="K-Nearest Neighbor", command=knnfun).pack(side=TOP)

    svm = Button(category, text="Support Vector Machine", command=svmfun).pack(side=TOP)

    top.mainloop()

start()

