from tkinter import *
import tkinter as tk
def calculate():
  if valRadio.get() == 1:
    res = (int(e1.get()) + int(e2.get())) * 2 #Perimeter
  elif valRadio.get() == 2:
    res = int(e1.get()) * int(e2.get()) #Area
  else:
    res ="check radio button"
  myText.set(res)
root = tk.Tk()
root.title("Calculator")     # Add a title
valRadio = tk.IntVar()
myText=tk.StringVar()
e1 =tk.StringVar()
e2 =tk.StringVar()
tk.Label(root,
    text="""Calculator""").grid(row = 0, column = 0)
tk.Label( text="Length :" ).grid(row=1,column = 0)
tk.Label( text="Width :").grid(row=2,column=0)
result=tk.Label(text="(result)", textvariable=myText).grid(row=5,column=0)
r1 = tk.Radiobutton(text="Area?",
      variable=valRadio, value=1).grid(row=3, column=0)
r2 = tk.Radiobutton(text="Perimeter?",
      variable=valRadio, value=2).grid(row=3, column=1)
tk.Entry(textvariable = e1).grid(row=1, column=1)
tk.Entry(textvariable = e2).grid(row=2, column=1)
b = tk.Button(text="Calculate", command=calculate).grid(row=1, column=3)
root.mainloop()