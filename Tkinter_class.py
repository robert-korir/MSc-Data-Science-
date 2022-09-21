# from fileinput import close
# import tkinter
# from tkinter import *
# def press_exit():
#     print('Ok')

# def exit_window():
#     print('close')
#     exit()

# # declare the window
# mw = Tk()
# # set window title
# mw.title("Basic Window")
# # set window width and height
# mw.configure(width=200, height=400)
# # set window background color
# mw.configure(background='lightblue')
# # Create a Button
# btn = Button(mw, text = 'OK', bd = '5', bg='green', fg='white', activebackground='lightgreen',command = exit)
# btn2 = Button(mw, text = 'Exit', bg='red',command =close)
# # Set the position of button on the top of window.  
# btn.pack(side = 'bottom') 
# btn2.pack(side = 'top')
# btn.place(x=150, y=350)
# btn2.place(x=150, y=350)

# mw.mainloop()


from tkinter import *
# declare the window
mw = Tk()
# set window title
mw.title("Basic Window")
# set window width and height
mw.configure(width=200, height=400)

# Create a Button
# label = Label(mw, text = 'Temperature:')
# temperature= Entry(mw)
# label2 = Label(mw, text = 'C')
# label.place(x=10, y=20)
# label2.place(x=250, y=20)
# temperature.place(x=15, y=20)

lb1 = Label(mw, text="Temperature: ", bg="lightgray" , fg="black") 
lb1.place(x=20, y=50) 
temperature = Entry(mw, bg="white") 
temperature.place(x=120, y=50) 

lbl2 = Label(mw, text="°C", bg="lightgray" , fg="black") 
lbl2.place(x=300, y=50) 

b3 = Button(mw, text='OK', bg='lightgray', fg='black',activebackground='gray', command=_ConverterCallback)
b3.place(x=400, y=50) 

lb4 =  Label(mw, text="--K", bg="lightgray", fg="black")
lb5 =  Label(mw, text="--F", bg="lightgray", fg="black") 
lb4.place(x=200, y=150)
lb5.place(x=200, y=180)
# def convert():
# celsius = float(e1.get())
#     12.config(text=str(celsius*1.8 + 32)+"F")
#     13.config(text=str(celsius+273.15)+"F")
