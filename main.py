from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
miles_input = Entry()
miles_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
km_value = Label(text="0")
km_value.grid(column=1, row=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def convert_miles_to_km():
  km = float(miles_input.get())*1.60934
  km_value.config(text=km)

calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
