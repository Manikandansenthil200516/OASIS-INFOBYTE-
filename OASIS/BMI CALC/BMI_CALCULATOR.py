import tkinter as tk
from customtkinter import CTk, CTkLabel, CTkEntry
import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())  # Get value from weight_entry

        if height <= 0 or weight <= 0:
            messagebox.showerror('Error', 'Please enter a positive number for height and weight.')
            return

        bmi = weight / (height ** 2)
        result_label.configure(text=f'Your BMI is: {round(bmi, 2)}')

    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numbers for height and weight.')

app = CTk()
app.title('BMI-CALCULATOR')
app.geometry('450x450')
app.config(bg='#000')

font1 = ('oswald', 30)
font2 = ('oswald', 20)
font3 = ('oswald', 20)

title_label = CTkLabel(app, font=font1, text='BMI-CALCULATOR', text_color='#fff', bg_color='#000')
title_label.place(x=130, y=40)

height_label = CTkLabel(app, font=font2, text='HEIGHT (m):', text_color='#fff', bg_color='#000')
height_label.place(x=40, y=130)

weight_label = CTkLabel(app, font=font2, text='WEIGHT (kg):', text_color='#fff', bg_color='#000')
weight_label.place(x=40, y=190)

height_entry = CTkEntry(app, width=80, font=font2)
height_entry.place(x=230, y=130)

weight_entry = CTkEntry(app, width=80, font=font2)
weight_entry.place(x=230, y=190)

result_label = CTkLabel(app, text='', text_color='#0ff', bg_color='#000')
result_label.place(x=40, y=310)

calculate_button = tk.Button(app, text='Calculate', command=calculate_bmi, font=font2)
calculate_button.place(x=230, y=300)

app.mainloop()