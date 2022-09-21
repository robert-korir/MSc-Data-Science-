from tkinter import *
window=Tk()
# lbl = Label(window, text="Name: ", bg="lightgray" , fg="black")
# lbl.place(x=10, y=50) 
Entry = Entry(window, text="Name:", bg="lightgray", fg="black")
Entry.place(x=50, y=20) 
lbl = Label(window, text="Name:", bg="lightgray", fg="black")
lbl.place(x=20, y=50)
lbl.place(x=10, y=50)
lbl1=Label(window, text="Food:", fg='black')
lbl1.place(x=10, y=150)
lbl2=Label(window, text="Drinks:", fg='black')
lbl2.place(x=120, y=150)


window.title('tk')
window.geometry("300x200+10+10")
window.mainloop()