from tkinter import *

# create a new window
window = Tk()
window.title("Unit Converter")
window.config(padx=20, pady=20)


def convert_unit():
    value = float(value_input.get())
    result = 0.0
    unit = ""

    if conversion_choice.get() == "length":
        if from_unit.get() == "inch" and to_unit.get() == "cm":
            result = value * 2.54
            unit = "cm"
        elif from_unit.get() == "cm" and to_unit.get() == "inch":
            result = value / 2.54
            unit = "inch"
        elif from_unit.get() == "feet" and to_unit.get() == "meter":
            result = value * 0.3048
            unit = "meter"
        elif from_unit.get() == "meter" and to_unit.get() == "feet":
            result = value / 0.3048
            unit = "feet"

    elif conversion_choice.get() == "weight":
        if from_unit.get() == "kg" and to_unit.get() == "grams":
            result = value * 1000
            unit = "grams"
        elif from_unit.get() == "grams" and to_unit.get() == "kg":
            result = value / 1000
            unit = "kg"
        elif from_unit.get() == "lbs" and to_unit.get() == "kg":
            result = value * 0.453592
            unit = "kg"
        elif from_unit.get() == "kg" and to_unit.get() == "lbs":
            result = value / 0.453592
            unit = "lbs"

    elif conversion_choice.get() == "temperature":
        if from_unit.get() == "celsius" and to_unit.get() == "fahrenheit":
            result = (value * 9/5) + 32
            unit = "°F"
        elif from_unit.get() == "fahrenheit" and to_unit.get() == "celsius":
            result = (value - 32) * 5/9
            unit = "°C"

    result_label.config(text=f"{result:.2f} {unit}")


def update_unit_menu(*args):
    selected_conversion = conversion_choice.get()

    if selected_conversion == "length":
        units = ["inch", "cm", "feet", "meter"]
    elif selected_conversion == "weight":
        units = ["kg", "grams", "lbs"]
    elif selected_conversion == "temperature":
        units = ["celsius", "fahrenheit"]

    from_unit_menu['menu'].delete(0, 'end')
    to_unit_menu['menu'].delete(0, 'end')

    for unit in units:
        from_unit_menu['menu'].add_command(label=unit, command=lambda value=unit: from_unit.set(value))
        to_unit_menu['menu'].add_command(label=unit, command=lambda value=unit: to_unit.set(value))


conversion_choice = StringVar(value="length")
conversion_choice.trace_add("write", update_unit_menu)

value_input = Entry(width=7)
value_input.grid(column=1, row=0)

Label(text="Value").grid(column=0, row=0)
Label(text="From Unit").grid(column=0, row=1)
Label(text="To Unit").grid(column=2, row=1)
Label(text="is equal to").grid(column=2, row=0)

# radio button for selection
length_radio = Radiobutton(text="Length", variable=conversion_choice, value="length")
length_radio.grid(column=1, row=4)

weight_radio = Radiobutton(text="Weight", variable=conversion_choice, value="weight")
weight_radio.grid(column=2, row=4)

temperature_radio = Radiobutton(text="Temperature", variable=conversion_choice, value="temperature")
temperature_radio.grid(column=3, row=4)

# Units for conversion
from_unit = StringVar(value="inch")
to_unit = StringVar(value="cm")

from_unit_menu = OptionMenu(window, from_unit, "inch", "cm", "feet", "meter")
to_unit_menu = OptionMenu(window, to_unit, "inch", "cm", "feet", "meter")

from_unit_menu.grid(column=1, row=1)
to_unit_menu.grid(column=3, row=1)

result_label = Label(text="0.00")
result_label.grid(column=1, row=7)

calculate_button = Button(text="Convert", command=convert_unit)
calculate_button.grid(column=1, row=9)

window.mainloop()
