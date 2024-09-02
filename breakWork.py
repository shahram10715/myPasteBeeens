import time
import threading
from plyer import notification
import tkinter as tk
from tkinter import messagebox

# Function to show notifications
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification display time in seconds
    )

# Function to handle the work-break cycle
def work_break_cycle():
    global running
    work_duration = 50 * 60  # 50 minutes in seconds
    break_duration = 10 * 60  # 10 minutes in seconds

    while running:
        # Work period
        show_notification("Break Reminder", "Time to work for 50 minutes!")
        for i in range(work_duration, 0, -1):
            if not running:
                break
            mins, secs = divmod(i, 60)
            time_left.set(f"Time remaining: {mins:02d}:{secs:02d} (Work)")
            time.sleep(1)
        
        if not running:
            break

        # Break period
        show_notification("Break Reminder", "Time to take a 10-minute break!")
        for i in range(break_duration, 0, -1):
            if not running:
                break
            mins, secs = divmod(i, 60)
            time_left.set(f"Time remaining: {mins:02d}:{secs:02d} (Break)")
            time.sleep(1)

# Start button action
def start_timer():
    global running
    running = True
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    threading.Thread(target=work_break_cycle).start()

# Stop button action
def stop_timer():
    global running
    running = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    time_left.set("Timer stopped.")
    show_notification("Break Timer", "Timer stopped.")

# Function to confirm exit
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        stop_timer()
        root.destroy()

# Initialize the main window
root = tk.Tk()
root.title("Work-Break Timer")

# Variable to hold the remaining time
time_left = tk.StringVar()
time_left.set("Press Start to begin.")

# Add GUI elements
frame = tk.Frame(root)
frame.pack(pady=20)

time_label = tk.Label(frame, textvariable=time_left, font=("Helvetica", 14))
time_label.pack(pady=10)

start_button = tk.Button(frame, text="Start Timer", command=start_timer, width=20)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(frame, text="Stop Timer", command=stop_timer, state=tk.DISABLED, width=20)
stop_button.pack(side=tk.RIGHT, padx=10)

# Handle window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Start the GUI event loop
root.mainloop()
