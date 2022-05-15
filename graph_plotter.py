import math as ma
import numpy as np
import matplotlib.pyplot as plt
import time


def runthis3():
    print("type 'linear' for linear eqn, 'quadratic' for quadratic eqn, or 'cubic' for cubic eqn")
    yeet = input("what polynomial do you want to solve: ")
    if yeet == "linear":
        global m
        m = int(input("coefficient| "))
        global c
        c = int(input("constant   | "))
        x = np.arange(-5.7, 3.1, 0.05)
        y = [(m * i + c) for i in x]
        plt.plot(x, y, label='linear', linestyle='-', color='r')
        plt.grid(True)
        plt.show(block=False)
        plt.pause(100)
        plt.close()
    if yeet == "quadratic":
        global a
        a = int(input("first coefficient | "))
        global b
        b = int(input("second coefficient| "))
        c = int(input("constant          | "))
        x = np.arange(-5.7, 3.1, 0.05)
        y = [(a * i ** 2 + b * i + c) for i in x]
        plt.plot(x, y, label='linear', linestyle='-', color='r')
        plt.grid(True)
        plt.show(block=False)
        plt.pause(100)
        plt.close()
    if yeet == "cubic":
        a = int(input("first coefficient | "))
        b = int(input("second coefficient| "))
        c = int(input("third coefficient | "))
        global d
        d = int(input("constant          | "))
        x = np.arange(-5.7, 3.1, 0.05)
        y = [(a * i ** 3 + b * i ** 2 + c * i + d) for i in x]
        plt.plot(x, y, label='cubic', linestyle='-', color='r')
        plt.grid(True)
        plt.show(block=False)
        plt.pause(100)
        plt.close()