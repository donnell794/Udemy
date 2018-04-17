from tkinter import *

window = Tk()

def convert_kg():
    gram = float(e1_val.get()) * 1000.0
    pound = float(e1_val.get()) * 2.20462
    ounce = float(e1_val.get()) * 35.274
    t1.delete("1.0", END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)

b1 = Button(window, text="Convert", command=convert_kg)
b1.grid(row=0, column=2)

e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0,column=1)

e2 = Label(window, text="kg")
e2.grid(row=0, column=0)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
