from cgitb import text
from distutils.cmd import Command
from msilib.schema import RadioButton
from tkinter import *
window = Tk()
window.minsize(width=300,height=200)
window.title("Converter")
window.config(padx=20,pady=20)


#Functions

def change_to_mileK():
    miles_label.config(text="Miles")
    km_label.config(text="Km")
    window.title("Mile to Kilometer Converter")
    calculate_button["command"] = miles_to_kilometers

def change_to_celciusf():
    miles_label.config(text="Celcius")
    km_label.config(text="Fahrenheit")
    window.title("Celcius to Fahrenheit Converter")
    calculate_button["command"] = celcius_to_fahrenheit
    

def change_to_celciusk():
    miles_label.config(text="Celcius")
    km_label.config(text="Kelvin")
    window.title("Celcius to Kelvin Converter")
    calculate_button["command"] = celcius_to_kelvin
    
def celcius_to_fahrenheit():
    fahrenheit = float(miles_input.get()) 
    result = fahrenheit*1.8 +32
    km_result_label.config(text=f"{result}")
    
def miles_to_kilometers():
    miles = float(miles_input.get()) 
    result = miles*1.609
    km_result_label.config(text=f"{result}")
    
    
def celcius_to_kelvin():
    kelvin = float(miles_input.get()) 
    result = kelvin + 300
    km_result_label.config(text=f"{result}")
#label

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

km_result_label = Label(text="0",)
km_result_label.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

#Entry

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)

#Button

calculate_button = Button(text="Calculate",command=change_to_mileK)
calculate_button.grid(column=1,row=2)

r = IntVar()


celcius_to_f = Radiobutton(text="Celcius to Fahrenheit",
                      variable=r, value=0, highlightthickness=0,command=change_to_celciusf)
celcius_to_f.grid(column=0, row=3, sticky="W")

celcius_to_k = Radiobutton(text="Celcius to Kelvin",
                     variable=r, value=1,    highlightthickness=0,command=change_to_celciusk)
celcius_to_k.grid(column=0, row=4, sticky="W")

miles_to_kilometer = Radiobutton(text="Miles to Kilometer",
                     variable=r, value=2,    highlightthickness=0,command=change_to_mileK)
miles_to_kilometer.grid(column=0, row=5, sticky="W")




window.mainloop()