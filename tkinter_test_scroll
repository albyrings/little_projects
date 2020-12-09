import tkinter as Tkinter

F1 = Tkinter.Frame()
s = Tkinter.Scrollbar(F1)
L = Tkinter.Listbox(F1)

s.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
L.pack(side=Tkinter.LEFT, fill=Tkinter.Y)

s['command'] = L.yview
L['yscrollcommand'] = s.set

for i in range(30): 
   L.insert(Tkinter.END, str(i))

F1.pack(side=Tkinter.TOP)

F2 = Tkinter.Frame()
lab = Tkinter.Label(F2)

def poll():
    lab.after(200, poll)
    sel = L.curselection()
    lab.config(text=str(sel))

lab.pack()
F2.pack(side=Tkinter.TOP)

poll()
Tkinter.mainloop()
