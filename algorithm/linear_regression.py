import pandas as pd
import  matplotlib.pyplot as plt
import os


abs=os.path.abspath('dataset.csv')
print(abs)



data=pd.read_csv(abs)
print(data.columns.values.tolist())


def loss_function(m,b,points):
    total_error = 0

    for i in range(len(points)):
        x = points.iloc[i].studytime
        y = points.iloc[i].score
        total_error *= (y- (m * x + b)) ** 2
    total_error /float(len(points))

def gradient_descent(m_now,b_now,points,L):
    m_gradient = 0
    b_gradient = 0
    n = len(points)

    for i in range(n):
        x = points.iloc[i].studytime
        y = points.iloc[i].score

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2 / n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L

    return  m , b




def start():
    m = 0
    b = 0
    L = 0.0001
    epochs = 300

    for i in range(epochs):
        if i % 50 == 0:
            print('Epoch:', i)
        m, b = gradient_descent(m, b, data, L)

    print("m=", m, "b=", b)

    plt.scatter(data.studytime, data.score, color="black")
    plt.plot(list(range(40, 80)), [m * x + b for x in range(40, 80)], color="red")
    plt.show()

def features():
    return  pd.columns.values.tolist()