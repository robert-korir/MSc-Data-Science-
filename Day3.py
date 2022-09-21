from cmath import inf
from tkinter import * # Importing the GUI library tkinter
import random

##################################################################### 1-2 ################################################################
# Create a 200x400 window with a light blue backgound, then add a green OK button to it that prints out "OK" and a red exit button that prints out "Program colsing" then closes the program

def ok(): # Fucntion that we will call from the OK button on pressing it
    print("OK")

def close(): # Function that we will call from the EXIT button on pressing it
    print("Program Closed")
    exit()

# Creating a new window and specifying the configuration
mw = Tk()
mw.title("Basic Window")
mw.config(background="lightblue", width=200, height=400)

# Creating a new green button, that changes color if pressed and calls the function ok() when pressed
b1 = Button(mw, text="OK", bg="green", fg="white", activebackground="lightgreen", command=ok)
b1.place(x=150, y=350)

# Creating a new red button, that calls the function close() when pressed
b2 = Button(mw, text="EXIT", bg="red", command=close)
b2.place(x=150, y=25)


################################################################# 3 ####################################################################
# Create a simple temperature converter that takes in the temperature from the user in Celsius then convert it to Fahrendheit and Kelvin

def convert(): # The function that we cal when pressing the OK button
    celsius = float(e1.get()) # Getting the user-provided Celsius value from the entry e1 then converting it from string to float
    l2.config(text=str(celsius * 1.8 + 32) + " °F") # Calculating the Fahrenheit value and changing the text on the label accordingly
    l3.config(text=str(celsius+273.15) + " K") # Calculating the Kelvin value and changing the text on the label accordingly

tl1 = Toplevel(mw) # Creating a new window that is connected to the previously used window mw and specifying its' characteristics
tl1.title("Temperature Converter")
tl1.config(width=500, height=300)

# Creating a new green button that calls tthe convert() function when pressed
b3 = Button(tl1, text="OK", bg="green", fg="white", activebackground="lightgreen", command=convert)
b3.place(x=450, y=50)

# Creating the text elements in the window
l1=Label(tl1, text="Temperature [°C]: ")
l1.place(x=50, y=50)
l2=Label(tl1, text="--- °F")
l2.place(x=220, y=160)
l3 = Label(tl1, text="--- K")
l3.place(x=220, y=200)

# Creating the input text field in the window
e1 = Entry(tl1)
e1.place(x=200, y=50)


######################################################## 4 #######################################################
# Create a simple GUI calculator. Read in the operand(s) and operator(s) and display the answer by pressing the OK button

def calc(): # The function that we call after pressig the Calculate button
    l6.config(text=str(eval(e2.get()))) # Getting the user-provided expression from the entr, then evaluating it and converting the result to string

tl2 = Toplevel(mw) # Creating a new window that is connected to the previously used window mw and specifying its' characteristics
tl2.title("Calculator")
tl2.config(width=500, height=300)

#  Creating the entry text field for the user-provided expression
e2 = Entry(tl2)
e2.place(x=100, y=30)

# Creating the text features of the window
l4 = Label(tl2, text="Calculator: ")
l4.place(x=30, y=30)
l5 = Label(tl2, text="Result: ")
l5.place(x=30, y=100)
l6 = Label(tl2, text="-----------")
l6.place(x=100, y=100)

#C Creating the calculate button, that will call the calc() function when pressed
b4 = Button(tl2, text="Calculate", bg="green", fg="white", activebackground="lightgreen", command=calc)
b4.place(x=425, y = 30)


##################################################### 5 ########################################################
# Create a GUI application that can calculate the perimeter or the area of a rectangle, given the two sides by the user

def p_a(): # The function that gets called when a radio button is clicked
    x = float(e3.get())
    y = float(e4.get())

# Deciding which calculation to do, then calculating and displaying the area or the perimeter accordingly    
    if var.get() == "perimeter":
        l7.config(text="Perimeter: " + str(2*(x + y)))
    elif var.get() == "area":
        l7.config(text="Area:  " + str(x * y))

# Creating and configuring a new window
tl3 = Toplevel(mw)
tl3.title("Perimeter-Area")
tl3.config(width=500, height=300)

# Creating the labels and entries of the window
l7 = Label(tl3, text="Area or Perimeter?")
l7.place(x=50, y=250)
e3 = Entry(tl3)
e3.place(x = 350, y = 50)
e4 = Entry(tl3)
e4.place(x=350, y=100)

# Creating and configureing the radio buttons, to be able to set the value of var and to call the p_a() function
var = StringVar()
r1 = Radiobutton(tl3, text="Perimeter", variable=var, value="perimeter", command=p_a)
r1.place(x=50, y=50)
r2 = Radiobutton(tl3, text="Area", variable=var, value="area", command=p_a)
r2.place(x=50, y=100)


##################################################### 6 ########################################################
# Create a GUI application, where the user can give their name, choose from 4 menu options (A, B, C or D) and choose if they'd like Water, Coffee, Wine, or several of them.

def form():
    print("OK")
    f = open("form.txt", "w")
    f.write("Name: " + e5.get() + "\n")
    f.write("Chosen food: " + menu.get() + "\n")
    f.write("Chosen drink(s): ")
    if v1.get():
        f.write("Water ")
    if v2.get():
        f.write("Wine ")
    if v3.get():
        f.write("Coffee ")

tl4 = Toplevel(mw)
tl4.title("Form")
tl4.config(width=400, height=300)
menu = StringVar()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()

l8 = Label(tl4, text="Name: ")
l8.place(x=20, y=30)

e5 = Entry(tl4)
e5.place(x=80, y=30)

l9 = Label(tl4, text="Food:")
l9.place(x=20, y=90)

l10 = Label(tl4, text="Drink(s):")
l10.place(x=250, y=90)

r3 = Radiobutton(tl4, text="Menu A", variable=menu, value="Menu A")
r3.place(x=20, y=120)
r4 = Radiobutton(tl4, text="Menu B", variable=menu, value="Menu B")
r4.place(x=20, y=140)
r5 = Radiobutton(tl4, text="Menu C", variable=menu, value="Menu C")
r5.place(x=20, y=160)
r6 = Radiobutton(tl4, text="Menu D", variable=menu, value="Menu D")
r6.place(x=20, y=180)
menu = "Menu"

c1 = Checkbutton(tl4, text="Water", variable=v1, onvalue=1, offvalue=0)
c1.place(x=250, y=120)
c2 = Checkbutton(tl4, text="Wine", variable=v2, onvalue=1, offvalue=0)
c2.place(x=250, y=140)
c3 = Checkbutton(tl4, text="Coffee", variable=v3, onvalue=1, offvalue=0)
c3.place(x=250, y=160)

b5 = Button(tl4, text="Ok", command=form)
b5.place(x=350, y=250)

# Running the main window and its' connected windows
mw.mainloop()

