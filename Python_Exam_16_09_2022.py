"""
Korir Robert Kipngeno
"""
import random
from tkinter import *
#GUI main app window
mw = Tk() 
mw.title("SMART PLANT")
mw.geometry("400x500")
background_color = 'SteelBlue1'
mw.config( bg=background_color)

# Creating labels
l = Label(text = "Enter Sensor name:",bg=background_color, fg="black",)
l.place(x=20, y=20)
l1 = Label(text = "Sensor: ",bg=background_color, fg="black",)
l1.place(x=25, y=40)
l2 = Label(text = "Data: ",bg=background_color, fg="red",)
l2.place(x=20, y=170)
errL = Label(text = "Error ",bg=background_color, fg="red",)
errL.place(x=60, y=170)
l3 = Label(text = "-"*23+"\nSelect operation!\n"+"-"*23, bg=background_color, fg="black",)
l3.place(x=20, y=200)
l4 = Label(text = "Enter the file name in case of SAVE  ",bg=background_color, fg="black",)
l4.place(x=40, y=300)
l5= Label(text = "Error message: ",bg=background_color, fg="red",)
l5.place(x=20, y=350)
l6 = Label(text = " -",bg=background_color, fg="red",)
l6.place(x=120, y=350)
l7 = Label(text = "Filter and calculate:",bg=background_color, fg="black",)
l7.place(x=300, y=20)
l8 = Label(text = "Date min: ",bg=background_color, fg="black",)
l8.place(x=300, y=40)
l9 = Label(text = "Date max: ",bg=background_color, fg="black",)
l9.place(x=300, y=60)
l10 = Label(text = "-"*20, bg=background_color, fg="black",)
l10.place(x=360, y=100)
# mw = Tk()
# mw.title("SMART PLANT")
# mw.config(height=400, width=500, bg='steelblue1')
# l1 = Label(mw, text="Enter the Sensor name:")
# l1.place(x=30, y=10)
# l2 = Label(mw, text="Sensor: ")
# l2.place(x=30, y=50)
# e1 = Entry(mw, bg="green2")
# e1.place(x=80, y=50)
# b1 = Button(mw, text="OK")
# b1.place(x=170, y=100)
# l7=Label(mw, text="Data: Error", fg="red")
# l7.place(x=30, y=160)
# l5 = Label(mw, text="Error message: -", fg="darkred")
# l5.place(x=30, y=360)
# l6 = Label(mw, text="Filter and calculate:")
# l6.place(x=300, y=10)
# tart = IntVar()
# l7=Label(mw, text="Date min:")
# l7.place(x=200, y=50)
# l8=Label(mw, text="Date max:")
# l8.place(x=200, y=50)
# r2 = Radiobutton(mw, text="MIN")
# r2.place(x=260, y=110)
# r3 = Radiobutton(mw, text="MAX")
# r3.place(x=260, y=140)
# r4 = Radiobutton(mw, text="Quantity")
# r4.place(x=260, y=170)
# r5 = Radiobutton(mw, text="Average")
# r5.place(x=260, y=200)
# var = StringVar()
# var.set("display")
# r7 = Checkbutton(mw, text="Display data")
# r7.place(x=50, y=250)
# r8 = Checkbutton(mw, text="Write to file")
# r8.place(x=50, y=270)
# l9 = Label(mw, text="Enter the file name in case of SAVE")
# l9.place(x=50, y=300)
# e3 = Entry(mw, bg="salmon1")
# e3.place(x=275, y=290)
# b3 = Button(mw, text="OK", bg="springgreen")
# b3.place(x=420, y=285)
 
# Checkbutton 
a = IntVar()
b = IntVar()
Checkbutton(mw, text="Display data", variable=a,fg="black",  bg=background_color).place(x=30, y=250)
Checkbutton(mw, text="Write to file", variable=b,fg="black",  bg=background_color).place(x=30, y=270)

# Radiobutton
var = StringVar()
r=Radiobutton(mw,variable=var, value="MIN", text="MIN",fg="black", bg=background_color).place(x=360, y=120)
r=Radiobutton(mw,variable=var, value="MAX", text="MAX",fg="black", bg=background_color).place(x=360, y=140)
Radiobutton(mw,variable=var, value="Quantity", text="Quantity",fg="black", bg=background_color).place(x=360, y=160)
Radiobutton(mw,variable=var, value="Average", text="Average",fg="black", bg=background_color).place(x=360, y=180)


# Inputs 
sensorID = Entry(bg="green2", fg="black")
sensorID.place(x=80,y=40)

fileName = Entry(bg="salmon1", fg="black")
fileName.place(x=220,y=300)

dateMin = Entry(bg="white", fg="black")
dateMin.place(x=380,y=40)

dateMax = Entry(bg="white", fg="black")
dateMax.place(x=380,y=60)

#Functions to use

def getCorrectData():
    try:
        f = open("measurements.txt", "r")
    except:
        print("Can't read file!")
        exit()
    finally: 
        print("Reading File Data to file ")   
        text = f.readlines()
        filtered_data = []
        correct_data = 0 
        
        for item in text:
            correct_data = 0
            txt = item.split(", ")
            i = txt
            if(float(i[2]) >0 and float(i[2])<20):
                correct_data +=1
            if(float(i[3]) >0 and float(i[3])<100):
                correct_data +=1   
            if(float(i[4]) >0 and float(i[4])<100):
                correct_data +=1 
            if(float(i[5]) >164 and float(i[5])<340):
                correct_data +=1  
            
            if(correct_data == 4):
                filtered_data.append(i)  
        getCorrectData("correct_data", filtered_data)     
        f.close() 
def get_Sensor():
                    sensor = sensorID.get()

def getdate_Filters():
# format : 2022-12-01 [yyyy-mm-dd]
    startDate = dateMin.get()
    stopDate = dateMax.get()

def calc():
    radioSelection = var.get()
    if(radioSelection == "MIN"):
        print("Finding min")
    elif(radioSelection == "MAX"):
        print("Finding max")
    elif(radioSelection == "Quantity"): # number of correct data packets
        print("Finding Quantity")
    elif(radioSelection == "Average"):
        print("Finding Average")
        
def write_data_to_file(file, data):
    try:
        f = open(file+".txt", "w")
    except:
        print("Can't read file!")
        exit()
    finally: 
        print("Writing Data to file ")
        for i in data:
            for x in range(6):
                if(x < 5):
                   f.write(f"{i[x]}, ") 
                else:
                    f.write(f"{i[x]}")
        f.close()  

def add_numbers():
    random.seed()
    f=open("measurements.txt", "w")

    for _ in range(0,100):
        f.write(str(random.randint(1, 100)) + "\n")
#check numbers
def check_numbers():
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
    print(str(count) + " valid results.")
    f.seek(0, 2)
    print("The file is " + str(f.tell()) + " The characters entered are long")
    f.close()

add_numbers()
check_numbers()
calc()



# buttons
btnSensorName = Button(mw,text="OK",  fg="black", command=add_numbers)
btnSensorName.place(x=150,y=80)

btnFileName = Button(mw,text="OK",bg="springgreen",  fg="black", )
btnFileName.place(x=400,y=300)

btnDateFilter= Button(mw,text="OK" ,  fg="black", command=check_numbers )
btnDateFilter.place(x=560,y=50)

btnFilterCalculate = Button(mw,text="OK" ,  fg="black", command=calc )
btnFilterCalculate.place(x=500, y=120)






if __name__ =='__main__':
    mainloop()