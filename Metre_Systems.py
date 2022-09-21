# Tkinter

from tkinter import *
import random
import math


def ok():
    print('OK')


def exitWindow():
    print("Program closed")
    # exit()
    exit()


def converttoFareignheight():
    value = temperature.get()
    valueFareignheight = int(value)*1.8 + 32
    lb4.config(text=f"{valueFareignheight} F")
    print("value (F): ", valueFareignheight)


def converttoKelvin():
    value = temperature.get()
    valueKelvin = int(value) + 273.15
    lb5.config(text=f"{valueKelvin} K")
    print("value (K): ", valueKelvin)


def convert():
    converttoFareignheight()
    converttoKelvin()


def calculator():
    result = eval(math_problem.get())
    lb4.config(text=result)


def getArea():
    print("Area")
    x = float(var1.get())
    y = float(var2.get())
    result = x*y
    lb4.config(text=result)


def getPerimeter():
    print("Perimeter")
    x = float(var1.get())
    y = float(var2.get())
    result = (2*x)+(y*2)
    lb4.config(text=result)

def writeToTextFile():
    print("Writing to text file")
    try:
        f = open("user_input.txt","w")
    except:
        print("File could not open")
        exit()
    finally:  
        # Get the input from GUI
        nameEntry = name.get()
        radioSelection = var.get()
        wineSelection = var1.get() # returns bool integer representation 1 or 0
        coffeeSelection = var2.get()# returns bool integer representation 1 or 0
        waterSelection = var3.get() # returns bool integer representation 1 or 0

        # Write to file   
        f.write("⭐"*10)
        f.write(f"\nName : {nameEntry}\n")
        f.write(f"Menu Selected : {radioSelection}\n")
        f.write(f"Drinks Selected :\n")
        if(wineSelection == 1):
           f.write(f"⭐ Wine \n")
        if(coffeeSelection == 1):
           f.write(f"⭐ Coffee \n")
        if(waterSelection == 1):
           f.write(f"⭐ Water \n")
        f.write("⭐"*10)
        f.close() 
        exit()  

def generateRandomValues():
    print("\nWriting to text file")
    try:
        f = open("raw_results.txt","w")
    except:
        print("File could not open")
        exit()
    finally:
        maxValue = 100
        startValue = 0
        values = []
        for i in range(99):
            randomValue = random.randint(startValue,maxValue)
            f.write(f"{randomValue} ")  
        
        f.close() 

def filterValuesFromFile():
    print("\nFiltering values between 20-80 in the raw_results.txt file")
    try:
        f = open("raw_results.txt", "r")
        fw = open("result_filtered.txt", "w")
        fr = open("result_filtered.txt", "r")
    except:
        print("Could not open file !")
        exit()
    finally:      
        text = f.read()
        for i in (text.split(" ")):
            if i == "":
                break
            # print(f"value - {i}") - debugginh purposes
            if(int(i) >20 and int(i) <80):
                fw.write(f"{i},")
        text = fr.read()
        print(f"Size of result_filtered.txt is {len(text)}")
        fw.close()     
        fr.close()
        f.close()

def getsizeOfResultFilterFile():
    print("\ngetting size of result_filtered.txt file")
    try: 
        fr = open("result_filtered.txt", "r")
    except:
        print("Could not open file !")
        exit()
    finally:       
        text = fr.read() 
        print(f"Size of result_filtered.txt is {len(text)}")    
        fr.close() 

def minMax():
    print("MIn MAx generation.")

def getcompanyDetails():
    print("Comapny Details ")


def createMeterSystem2000():
    mw = Tk()
    # What Toplevel(mw)
    mw.title("METER SYSTEM 2000")
    mw.config(background="lightgray")
    mw.geometry("800x800")
    Frame(mw, bg='white')

    # labels
    lbl1 = Label(mw, text="Add the company and the measurement number!", bg="lightgray", fg="black")
    lbl1.place(x=10, y=20)
    lbl2 = Label(mw, text="Generate data:", bg="lightgray", fg="black")
    lbl2.place(x=400, y=20)
    lbl3 = Label(mw,text="Comp.:", bg="lightgray", fg="black")
    lbl3.place(x=10, y=50)
    lbl4 = Label(mw,text="No.:", bg="lightgray", fg="black")
    lbl4.place(x=10, y=70)
    lbl5 = Label(mw,text="MIN", bg="lightgray", fg="black")
    lbl5.place(x=400, y=50)
    lbl6 = Label(mw,text="MAX", bg="lightgray", fg="black")
    lbl6.place(x=400, y=70)


    lbl7 = Label(mw,text="Range: ", bg="lightgray", fg="black")
    lbl7.place(x=10, y=200)
    lbl8 = Label(mw,text="na", bg="lightgray", fg="black")
    lbl8.place(x=60, y=200)
    lbl9 = Label(mw,text="Generate data: ", bg="lightgray", fg="red")
    lbl9.place(x=10, y=230)
    lbl10 = Label(mw,text="na", bg="lightgray", fg="black")
    lbl10.place(x=120, y=230)

    lbl11 = Label(mw,text="-"*25, bg="lightgray", fg="black")
    lbl11.place(x=10, y=300)
    lbl12 = Label(mw,text="Select Operation!", bg="lightgray", fg="black")
    lbl12.place(x=10, y=320) 
    lbl14 = Label(mw,text="-"*25, bg="lightgray", fg="black")
    lbl14.place(x=10, y=340)

    lbl15 = Label(mw,text="Enter the file name in case of SAVE", bg="lightgray", fg="black")
    lbl15.place(x=20, y=420)

    lbl15 = Label(mw,text="Enter the file name in case of SAVE", bg="lightgray", fg="black")
    lbl15.place(x=20, y=420)
    
    # Entries
    companyName = Entry(mw, bg="white", fg="black")
    companyName.place(x=60, y=50)
    measurementNumber =Entry(mw, bg="white", fg="black")
    measurementNumber.place(x=60, y=70)
    minValue = Entry(mw, bg="white", fg="black")
    minValue.place(x=450, y=50)
    maxValue =Entry(mw, bg="white", fg="black")
    maxValue.place(x=450, y=70)
    fileName = Entry(mw, bg="pink", fg="black")
    maxValue.place(x=400, y=420)



    # radiobutton
    var = StringVar()
    Radiobutton(mw, variable=var, borderwidth=0, text="Display data", value="Menu A", bg="lightgray", fg="black", command=getArea).place(x=10, y=370)
    Radiobutton(mw, variable=var, borderwidth=0, text="Write to file", value="Menu A", bg="lightgray", fg="black", command=getArea).place(x=10, y=390)



    # buttons
    btn = Button(text="OK", bg="blue", fg="white", command=minMax)
    btn.place(x=650, y=60)
    btn1 = Button(text="OK", bg="green", fg="black", command=minMax)
    btn1.place(x=200, y=100)
    mw.mainloop()


generateRandomValues() # generate and wrote random values to txt file
filterValuesFromFile() # filter values that range between 20 and 80
getsizeOfResultFilterFile()# size of the result fltered.txt
createMeterSystem2000()# meter system 2000

mw.mainloop()

# 6
# labels
lb1 = Label(mw, text="Name",  bg="lightgray", fg="black")
lb1.place(x=10, y=50)
lb2 = Label(mw, text="Food : ",  bg="lightgray", fg="black")
lb2.place(x=10, y=100)
lb3 = Label(mw, text="Drink(s) : ",  bg="lightgray", fg="black")
lb3.place(x=100, y=100)

# inputs
name = Entry(mw, bg="white", fg="black")
name.place(x=100, y=50)
# Radiobutton
var = StringVar()
Radiobutton(mw, variable=var, borderwidth=0, text="Menu A", value="Menu A",
            bg="lightgray", fg="black", command=getArea).place(x=10, y=140)
Radiobutton(mw, variable=var, borderwidth=0, text="Menu A", value="Menu B",
            bg="lightgray", fg="black", command=getArea).place(x=10, y=160)
Radiobutton(mw, variable=var, borderwidth=0, text="Menu A", value="Menu C",
            bg="lightgray", fg="black", command=getArea).place(x=10, y=180)
Radiobutton(mw, variable=var, borderwidth=0, text="Menu A", value="Menu D",
            bg="lightgray", fg="black", command=getArea).place(x=10, y=200)

# checkbox
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
Checkbutton(mw, variable=var1, borderwidth=0, text="Water", bg="lightgray", fg="black").place(x=100, y=140)
Checkbutton(mw, variable=var2, borderwidth=0, text="Wine", bg="lightgray", fg="black").place(x=100, y=160)
Checkbutton(mw, variable=var3, borderwidth=0, text="Coffee", bg="lightgray", fg="black").place(x=100, y=180)


# Button
b1 = Button(mw, text="OK", bg="green", fg='white',activebackground='lightgreen', command=writeToTextFile)
b1.place(x=300,y=200)

 2
b1 = Button(mw, text='Okay', bg='green', fg='white',activebackground='lightgreen', command=ok)
b1.place(x=150,y=350)

 3
b2 = Button(mw, text='Exit', bg='red', fg='white',activebackground='pink', command=exitWindow)
b2.place(x=150, y=10)

3

creating labels
lb1 = Label(mw, text="Temperature: ", bg="lightgray" , fg="black")
lb1.place(x=20, y=50)

lbl2 = Label(mw, text="°C", bg="lightgray" , fg="black")
lbl2.place(x=300, y=50)

b3 = Button(mw, text='OK', bg='lightgray', fg='black',activebackground='gray', command=convert)
b3.place(x=400, y=50)

lb4 =  Label(mw, text="--K", bg="lightgray", fg="black")
lb5 =  Label(mw, text="--F", bg="lightgray", fg="black")
lb4.place(x=200, y=150)
lb5.place(x=200, y=180)

temperature = Entry(mw, bg="white")
temperature.place(x=120, y=50)


4
labels
lb3 =  Label(mw, text="Area/Perimeter = ", bg="lightgray", fg="black")
lb3.place(x=20, y=180)
lb4 =  Label(mw, text="???", bg="lightgray", fg="black")
lb4.place(x=150, y=180)

# Entries
var1 = Entry(mw, bg="white", fg="black")
var1.place(x=120, y=50)
var2 = Entry(mw, bg="white", fg="black")
var2.place(x=120, y=80)


Buttons
b3 = Button(mw, text='OK', bg='green', fg='white',activebackground='gray', command=calculator)
b3.place(x=400, y=50)

5
Radio Buttons
var = StringVar()
Radiobutton(text="Area" , bg="lightgray",fg="black", variable= var, value="area", command=getArea).place(x=20, y=50)
Radiobutton(text="Perimeter" ,bg="lightgray",fg="black", variable= var,value="perimeter", command=getPerimeter).place(x=20, y=80)
