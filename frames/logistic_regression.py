from tkinter import *
from tkinter.filedialog import askopenfile
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd
import  os
import Machine_Learning_Work_Bench.algorithm.logistic_regression as lgalgorithm

def lgframe():
    features=[]

    print("called succeful")
    lg=Frame()
    lg.place(x=0,y=0,width=1200,height=750)

    user = Frame(lg,bd=2).place(x=800,width=400,height=750)

    l1 =Label(user, text="Trainset")

    l1.place(x=810, y=50)

    button1 = Button(user, text="Upload Dataset", command=lambda :gettraindata(user))

    # this will arrange  widgets

    button1.place(x = 950,y = 50)

    title=Label(lg,text="Logistic Regression").place(x=290,y=50)


def gettraindata(user):
    file= askopenfile(mode ='r', filetypes =[('CSV Files', '*.csv')])
    if(file):
        path = os.path.realpath(file.name)
        Label(text=str(path)).place(x = 805 ,y = 75)
        feature_list = Listbox(user, selectmode="multiple",exportselection=False)
        feature_list.place(x=810, y=150)
        features = lgalgorithm.features(path)
        for i in range(len(features)):
            feature_list.insert(END, features[i])

        category_list = Listbox(user, selectmode="multiple",exportselection=False)
        category_list.place(x=810, y=350)
        for i in range(len(features)):
            category_list.insert(END, features[i])
        l2 = Label(user, text="select independent features:")
        l3 = Label(user, text="select dependent features:")
        l2.place(x=810, y=120)
        l3.place(x=810, y=320)
        button2 = Button(user, text="Train Model",command=lambda :train(path,feature_list,category_list,user))
        button2.place(x=1000, y=600)
    else:
        Label(text="unable to load file".place(x=805, y=75))


def getlistitem(listbox):
    l=[]
    for i in listbox.curselection():
        l.append(listbox.get(i))
    return l

def train(path,feature_list,category_list,user):

  msgframe=Frame(user).place(x=810,y=650,width=400,height=250)

  print(len(feature_list.curselection()))
  print(len(category_list.curselection()))
  if((len(feature_list.curselection())>0) & (len(category_list.curselection()))>0):
      print("training")
      feature_list = getlistitem(feature_list);
      print(feature_list)

      category_list = getlistitem(category_list);
      print(category_list)
      l4 = Label(msgframe, text="preparing model,please wait").place(x=810, y=650)

      score,classifier,feature_list_index = lgalgorithm.logistic_regression(path,feature_list,category_list)
      if(score):
          output_frame=Frame(bg='red').place(x=150,y=150,width=400,height=250)
          Label(output_frame,text="Test Score:").place(x=160,y=120)
          Label(output_frame, text=score).place(x=250, y=120)

          l1 = Label(output_frame, text="Tsetdata")
          l1.place(x=160, y=180)
          button1 = Button(user, text="Upload Dataset", command=lambda: gettestfile(classifier,output_frame,feature_list_index)).place(x=250,y=180)

  else:
      print("invalid training")
      l4=Label(msgframe, text="canot proceed").place(x=810,y=650)



def model(path,classifier,feature_list_index):
    data = pd.read_csv(path)

    x_test = data.iloc[:, feature_list_index].values
    print(x_test)
    st_x = StandardScaler()
    x_test = st_x.transform(x_test)
    print(x_test)
    print(classifier.predict([[   26,5000]]))


def gettestfile(classifier,output_frame,feature_list_index):
    file = askopenfile(mode='r', filetypes=[('CSV Files', '*.csv')])
    if (file):
        path = os.path.realpath(file.name)
        Label(text=str(path)).place(x=200, y=220)
        button3 = Button(output_frame, text="Test data", command=lambda: model(path,classifier,feature_list_index,))
        button3.place(x=160, y=280)