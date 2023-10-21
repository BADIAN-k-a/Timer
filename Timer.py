
import tkinter as tk
import time
import winsound
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image


paused = False
remaining_time = 0

def stop_timer():
    global paused
    button_start.pack()
    button_stop.pack_forget()
    pause_timer()
    paused = True

def start_timer():
    global paused, remaining_time
    try:
        duration = entry_duration.get()
        if not duration.isdigit():
            raise ValueError('Enter the correct time')
        duration = int(duration)
        if duration <= 0:
            raise ValueError("Enter the correct time")
        if paused:
            resume_timer()
        else:
            remaining_time = duration
            countdown(remaining_time)
        paused = False
    except ValueError as e:
        label_timer.config(text=str(e))

def reset_timer():
    global remaining_time
    remaining_time = 0
    label_timer.config(text="")

def countdown(seconds):
    global paused, remaining_time
    button_start.pack_forget()
    button_stop.pack()
    label_timer.config(text=f"{seconds} seconds left.")
    remaining_time = seconds
    if seconds > 0 and not paused:
        window.after(1000, countdown, seconds-1)
    elif seconds == 0:
        label_timer.config(text="Beeb!")
        play_sound()
        paused = False
        button_stop.pack_forget()
        button_start.pack()
        remaining_time = 0

def play_sound():
    frequency = 2500
    lasting = 1000
    winsound.Beep(frequency, lasting)

def pause_timer():
    global paused
    paused = True

def resume_timer():
    global paused
    paused = False
    countdown(remaining_time)

window = tk.Tk()
window.title("Timer")
window.configure(bg='black')
window.geometry('1000x700')
window.resizable(False, False)

label_name = tk.Label(window, text="Tomato Timer", fg='red', bg='black', font=('Arial', 20))
label_name.pack()

label_duration = tk.Label(window, text="Enter the duration of the timer (in seconds):", fg='red', bg='black', font=('Arial', 12))
label_duration.pack(anchor="center",padx=[20],pady=[70,40])

entry_duration = tk.Entry(window, fg='red', font=('Arial', 12))
entry_duration.pack()

button_start = tk.Button(window, text="Start", command=start_timer, fg='red', bg='black', bd=0, font=('Arial', 12))
button_start.pack()

button_stop = tk.Button(window, text='Stop', command=stop_timer, fg='red', bg='black', bd=0, font=('Arial', 12))
button_stop.pack_forget()

label_timer = tk.Label(window, text="", fg='red', bg='black', font=('Arial', 14))
label_timer.pack()

python_logo = PhotoImage(file="./tomato.png")

 
label = ttk.Label(image=python_logo)
label.pack()


window.mainloop()