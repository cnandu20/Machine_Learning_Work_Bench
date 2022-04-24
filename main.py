
import frames.linear_regression as lr
import frames.logistic_regression  as lg
import frames.knn_frame  as knn_alg
import frames.svm_frame as svm
import frames.naive_bayes_frame as nb
import frames.random_forest_frame as random_forest


from tkinter import *



def linear():
    lr.lrframe()

def lgf():
    lg.lgframe()

def knnfun():
    knn_alg.knnframe()

def svmfun():
    svm.svmframe()

def nbfun():
    nb.nbframe()

def rffun():
    random_forest.random_forest_frame()


def start():

    top = Tk()
    top.geometry("1200x750")
    top.maxsize(1200, 750)
    top.minsize(1200, 750)

    top.title('Machine learning workbench')

    main = Frame(top)

    main.place(x=0, y=0, width=1200, height=750)

    # welcome image.........from here upto the end is edited.........................................................
    mlbimg = PhotoImage(file='mlb.png')
    welcome = Label(main, image=mlbimg)
    welcome.pack(side=LEFT)

    # side frame
    category = Frame(main, bg='#C4C4C4', highlightbackground="black", highlightthickness=1);
    category.place(x=900, y=0, width=300, height=750)

    choose = Label(category, bg='#141414', text="Choose algorithms", font=20, fg='white', width=300,
                   height=5).pack(side=TOP)

    # button icons
    lrimg = PhotoImage(file='lr.png')

    lgimg = PhotoImage(file='lg.png')

    knnimg = PhotoImage(file='knn.png')

    svmimg = PhotoImage(file='svm.png')

    nbimg = PhotoImage(file='nb.png')

    rfimg = PhotoImage(file='rf.png')



    logistic_regression = Button(category, image=lgimg, compound=LEFT, text="   Logistic Regression", anchor=W,
                                 width=300, command=lgf).pack(side=TOP, pady=20)

    knn = Button(category, image=knnimg, compound=LEFT, text="    K-Nearest Neighbor", anchor=W, width=300,
                 command=knnfun).pack(side=TOP, pady=20)

    svm = Button(category, image=svmimg, compound=LEFT, text="    Support Vector Machine", anchor=W, width=300,
                 command=svmfun).pack(side=TOP, pady=20)

    nb = Button(category, image=nbimg, compound=LEFT, text="     Naive Bayes  ", anchor=W, width=300,
                command=nbfun).pack(side=TOP, pady=20)

    rf = Button(category, image=rfimg, compound=LEFT, text="    Random Forest", anchor=W, width=300,
                command=rffun).pack(side=TOP, pady=20)

    top.mainloop()

start()

