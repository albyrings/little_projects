import numpy as np
_author_='Alberto Anelli'
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('EEE.csv')
print(df)
x = df[RVERO]
y = df[human_time]
#z = df[]

#grafico
plt.title('grafico rate')
plt.xlabel('data e ora')
plt.ylabel('rate')
red_patch = mpatches.Patch(color='red', label='rate totale')
green_patch = mpatches.Patch(color='blue', label='rate vero')
#ax=plt.subplot()

#genero un sistema di assi che condivide l'asse x con ax
#a2=ax.twinx()
#ax.plot(x,z)
plt.legend(handles=[red_patch,green_patch])
#plt.plot(x,z,linestyle='solid',color='red',marker='')
plt.plot(x,y,linestyle='solid',color='blue',marker='')

plt.show()
