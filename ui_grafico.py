import pandas as pd
import numpy as np
_author_='Alberto Anelli'
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from tkinter import *

class MyWindow:
    def __init__(self, win):

        self.lbl2=Label(win, text='colonna su x')
        self.lbl3=Label(win, text='colonna su y')
        self.lbl4=Label(win, text='colonna su z')
        self.lbl5=Label(win, text='Made by Alberto Anelli')
        self.t2=Entry(bd=3)
        self.t3=Entry(bd=3)
        self.t4=Entry(bd=3)
        self.btn1 = Button(win, text='draw!')
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.lbl4.place(x=100, y=200)
        self.t4.place(x=200,y=200)
        self.b1=Button(win, text='Draw!', command=self.draw)
        self.b1.place(x=100, y=250)
        self.lbl3.place(x=100, y=150)
        self.t3.place(x=200, y=150)
        self.lbl5.place(x=250, y=260)
    def draw(self):
        df=pd.read_excel('EEE.xlsx')
        num2=self.t2.get()
        num3=self.t3.get()
        num4=self.t4.get()
        num2_2=str(num2)
        num3_2=str(num3)
        num4_2=str(num4)
        x = df[num2_2]
        y = df[num3_2]
        z = df[num4_2]
        plt.title('grafico rate')
        plt.xlabel('data e ora')
        plt.ylabel('rate')
        red_patch = mpatches.Patch(color='red', label='rate totale')
        blue_patch = mpatches.Patch(color='blue', label='rate vero')
        #ax=plt.subplot()
        #genero un sistema di assi che condivide l'asse x con ax
        #a2=ax.twinx()
        #ax.plot(x,z)
        plt.legend(handles=[red_patch,blue_patch])
        plt.plot(x,z,linestyle='solid',color='red',marker='')
        plt.plot(x,y,linestyle='solid',color='blue',marker='')
        plt.show()
        plt.savefig('grafico.png')


window=Tk()
mywin=MyWindow(window)
window.title('grafico')
window.geometry("400x300+10+10")
window.mainloop()



