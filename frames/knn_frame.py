from tkinter import *
from tkinter.filedialog import askopenfile
from sklearn.preprocessing import StandardScaler
import pandas as pd
import  os
import Machine_Learning_Work_Bench.algorithm.knn_algorithm as knn_algorithm
from subprocess import Popen
from tkinter import ttk


def knnframe():
    features=[]

    print("called succeful")
    knn=Frame()
    knn.place(x=0,y=0,width=1200,height=750)


    # user = Frame(knn,bd=2).place(x=800,width=400,height=750)

    backbtn = Button(knn, text="Go back", height=3, width=9, command=lambda: back(knn))
    backbtn.place(x=0, y=10)

    l1 =Label(knn, text="Trainset")

    l1.place(x=810, y=50)

    button1 = Button(knn, text="Upload Dataset", command=lambda :gettraindata(knn))

    # this will arrange  widgets

    button1.place(x = 950,y = 50)

    title = Label(knn, text="  K-NEAREST NEIGHBOUR   ", font=20, bg='#141414', fg='white', height=2, ).place(x=75, y=10)


def gettraindata(user):
    file= askopenfile(mode ='r', filetypes =[('CSV Files', '*.csv')])
    if(file):
        path = os.path.realpath(file.name)
        Label(user,text=str(path)).place(x = 805 ,y = 75)
        feature_list = Listbox(user, selectmode="multiple",exportselection=False)
        feature_list.place(x=810, y=150)
        features = knn_algorithm.features(path)
        for i in range(len(features)):
            feature_list.insert(END, features[i])

        category_list = Listbox(user, selectmode="multiple",exportselection=False)
        category_list.place(x=810, y=350)
        for i in range(len(features)):
            category_list.insert(END, features[i])
        l2 = Label(user, text="select independent features:")
        l3 = Label(user, text="select dependent features:")
        l4 = Label(user, text="k-value:")
        k = Entry(user)
        k.place(x=860,y=520)
        l2.place(x=810, y=120)
        l3.place(x=810, y=320)
        l4.place(x=810,y=520)

        button2 = Button(user, text="Train Model",command=lambda :train(path,feature_list,category_list,user,k))
        button2.place(x=1000, y=600)
    else:
        Label(user,text="unable to load file".place(x=805, y=75))


def getlistitem(listbox):
    l=[]
    for i in listbox.curselection():
        l.append(listbox.get(i))
    return l

def train(path,feature_list,category_list,user,k):
  print("training")
  k_value=int(k.get())
  print(k_value)
  # msgframe=Frame(user).place(x=810,y=650,width=400,height=250)

  print(len(feature_list.curselection()))
  print(len(category_list.curselection()))

  if((len(feature_list.curselection())>0) & (len(category_list.curselection()))>0 & (k_value >(len(category_list.curselection())))):
      feature_list = getlistitem(feature_list);
      print(feature_list)

      category_list = getlistitem(category_list);
      print(category_list)
      l4 = Label(user, text="preparing model,please wait").place(x=810, y=650)

      score,classifier,feature_list_index = knn_algorithm.k_nearest(path,feature_list,category_list,k_value)
      if(score):
          # output_frame=Frame().place(x=150,y=150,width=400,height=250)
          Label(user, text="Test Score:").place(x=160, y=120)
          Label(user, text=score).place(x=250, y=120)

          l1 = Label(user, text="Test dataset")
          l1.place(x=160, y=180)
          button1 = Button(user, text="Upload Dataset", command=lambda: gettestfile(classifier,user,feature_list_index)).place(x=250,y=180)

  else:
      print("invalid training")
      l4=Label(user, text="can't proceed with out selection complete").place(x=810,y=650)



def model(path,classifier,feature_list_index,output_frame):
    data = pd.read_csv(path)

    x_test = data.iloc[:, feature_list_index].values

    st_x = StandardScaler()
    st_x.fit(x_test)
    x_test = st_x.transform(x_test)


    print(x_test)
    y_pred=classifier.predict(x_test)
    data['prediction']=y_pred
    data.to_csv("prediction.csv",index=False)
    if(Popen('prediction.csv',shell=True)):
        Label(output_frame,text="Result is saved to prediction.csv file with prediction column").place(x=160,y=320)

    else:
        Label(output_frame, text="Cant open your excel \n""check directory Result is saved to prediction.csv file").place(x=160, y=320)

def gettestfile(classifier,output_frame,feature_list_index):
    file = askopenfile(mode='r', filetypes=[('CSV Files', '*.csv')])
    if (file):
        path = os.path.realpath(file.name)
        Label(output_frame,text=str(path)).place(x=200, y=220)
        button3 = Button(output_frame, text="Test data", command=lambda: model(path,classifier,feature_list_index,output_frame))
        button3.place(x=160, y=280)



def back(frame1):
    frame1.destroy()
