import time 
from tkinter import messagebox

def show_alert():
    messagebox.showinfo("Alert!", "Take a break!")

duration = 20
start  = time.time()

while True:
    time.sleep(duration*60)
    show_alert()
