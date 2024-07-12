import tkinter as tk
from tkinter import Label
import time
import datetime

app = tk.Tk()
app.title("Digital Clock")
app.configure(bg='red')  # Set background color to red

def update_time():
    current_time = time.strftime('%H:%M:%S')
    current_date = datetime.date.today().strftime('%B %d, %Y')
    current_day = datetime.date.today().strftime('%A')
    time_label.config(text=current_time)
    date_label.config(text=f"{current_day}, {current_date}")
    app.after(1000, update_time)  # Update the time every second

time_label = Label(app, text="", font=("Helvetica", 48), bg='red', fg='white')  # Set label background to red and text color to white
time_label.pack(padx=20, pady=10)

date_label = Label(app, text="", font=("Helvetica", 18), bg='red', fg='white')  # Label for displaying date and day
date_label.pack(padx=20, pady=10)

update_time()
app.mainloop()
