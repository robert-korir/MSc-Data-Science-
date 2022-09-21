import random
from tkinter import *

def load_file_with_numbers():
    random.seed()

    f=open("measurements.txt", "w")

    for _ in range(0,100):
        f.write(str(random.randint(1, 100)) + "\n")

def examine_numbers():
    f = open("measurements.txt", "r")
    values = f.readlines()
    f.close()
    f = open("results_filtered.txt", "w")
    count = 0

    for x in values:
        value = int(x)
        if value < 80 and value > 20:
            count += 1
            f.write(str(value) + ", ")
    print(str(count) + " entries were valid.")
    f.seek(0, 2)
    print("The file is " + str(f.tell()) + " characters long")
    f.close()

load_file_with_numbers()
examine_numbers()

mw = Tk()
mw.title("SMART PLANT")
mw.config(height=400, width=500, bg='steelblue1')
l1 = Label(mw, text="Enter the Sensor name:")
l1.place(x=20, y=30)
l2 = Label(mw, text="Sensor: ")
l2.place(x=30, y=50)
e1 = Entry(mw, bg="green2")
e1.place(x=80, y=50)
# e2 = Entry(mw, bg="lightblue")
# e2.place(x=80, y=70)
b1 = Button(mw, text="OK")
b1.place(x=170, y=100)
l7=Label(mw, text="Data: Error", fg="red")
l7.place(x=30, y=160)
l5 = Label(mw, text="Error message: -", fg="darkred")
l5.place(x=30, y=360)
l6 = Label(mw, text="Filter and calculate:")
l6.place(x=300, y=20)
tart = IntVar()
l7=Label(mw, text="Date min:")
l7.place(x=260, y=50)
l8=Label(mw, text="Date max:")
l8.place(x=260, y=70)
e3=Entry(mw)
e3.place(x=300, y=720)
e4=Entry(mw)
e4.place(x=300, y=80)
maximum = IntVar()

r2 = Radiobutton(mw, text="MIN")
r2.place(x=260, y=110)
r3 = Radiobutton(mw, text="MAX")
r3.place(x=260, y=140)
r4 = Radiobutton(mw, text="Quantity")
r4.place(x=260, y=170)
r5 = Radiobutton(mw, text="Average")
r5.place(x=260, y=200)

l7 = Label(mw, text="----------------")
l7.place(x=260, y=90)
b2 = Button(mw, text="OK")
b2.place(x=400, y=120)
b6 = Button(mw, text="OK")
b6.place(x=440, y=55)
l8 = Label(mw, text="------------------\nSelect operation!\n------------------")
l8.place(x=30, y=200)
var = StringVar()
var.set("display")
r7 = Checkbutton(mw, text="Display data")
r7.place(x=50, y=250)
r8 = Checkbutton(mw, text="Write to file")
r8.place(x=50, y=270)
l9 = Label(mw, text="Enter the file name in case of SAVE")
l9.place(x=70, y=290)
e3 = Entry(mw, bg="salmon1")
e3.place(x=275, y=290)
b3 = Button(mw, text="OK", bg="springgreen")
b3.place(x=420, y=285)

mw.mainloop()

