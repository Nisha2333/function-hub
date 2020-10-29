import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy as np
import matplotlib.pyplot as plt

import function
def cos():
    x = np.arange(-10,10,1)
    y = np.cos(x)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('cos[n]')
    plt.xlabel('x')
    ax1.scatter(x, y, c='b', marker='o')
    plt.legend('x1')
    plt.grid(True)
    plt.show()

def un():
    def function1(x):
      y = x >= 0
      return y.astype(np.int)
    x = np.arange(-10, 10)
    y = function1(x)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('u[n]')
    plt.xlabel('x')
    plt.ylabel('y')
    ax1.scatter(x, y, c='b', marker='o')
    plt.legend('x1')
    plt.grid(True)
    plt.show()
 
def ss():
    def function(x):
      y = x == 0
      return y.astype(np.int)
    x = np.arange(-10, 10)
    y = function(x)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('δ(n)')
    plt.xlabel('x')
    plt.ylabel('y')
    ax1.scatter(x, y, c='b', marker='o')
    plt.legend('x1')
    plt.grid(True)
    plt.show()

def cose():
     x = np.arange(-50,50,0.1)
     y = np.cos(x)*np.exp(0.01*x)
     fig = plt.figure()
     ax1 = fig.add_subplot(111)
     ax1.set_title('e^j[n]')
     plt.xlabel('x')
     plt.ylabel('y')
     ax1.scatter(x, y, c='b', marker='o')
     plt.legend('x1')
     plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = function.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(cos)
    ui.pushButton_2.clicked.connect(un)
    ui.pushButton_3.clicked.connect(ss)
    ui.pushButton_4.clicked.connect(cose)
    sys.exit(app.exec_())