from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.geometry("420x170")
root.resizable(0,0)

def time():
    string = strftime("%H:%M:%S %p \n %D")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=('Digital-7 Mono', 50, 'bold'), background='black', foreground='purple')
label.pack(anchor='center')

time()
root.mainloop()
