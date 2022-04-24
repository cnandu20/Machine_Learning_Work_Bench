import pandas as pd
import  matplotlib.pyplot as plt
import numpy as nm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression



def logistic_regression(path,feature_list,category_list):
    data = pd.read_csv(path)

    feature_list_index=[]
    category_list_index=[]

    for i in feature_list:
        feature_list_index.append(data.columns.get_loc(i)-1)
    for i in category_list:
        category_list_index.append(data.columns.get_loc(i)-1)

    print(feature_list_index)

    #indepedent feautere values stored in x and depedent features in y

    x = data.iloc[:, feature_list_index].values
    y = data.iloc[:, category_list_index].values


    #random_state=0
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    print("in algo")
    print(x_test)

    st_x = StandardScaler()
    x_train = st_x.fit_transform(x_train)
    x_test = st_x.transform(x_test)

    classifier = LogisticRegression(random_state=0)
    classifier.fit(x_train, y_train)

    y_pred = classifier.predict(x_test)
    print("predited testdata")
    print(y_pred)

    return classifier.score(x_test,y_test),classifier,feature_list_index



def features(path):
    print("feauter function called successfull")
    print(path)

    data = pd.read_csv(path)
    print(data.columns.values.tolist())
    return  data.columns.values.tolist()

