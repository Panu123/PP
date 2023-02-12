"""Basic alarm/Timer"""

import tkinter as tk
import time
import winsound


def alarm():
    # Play a sound
    winsound.PlaySound("sound.wav", winsound.SND_FILENAME)


def snooze():
    # Snooze for 5 minutes
    time.sleep(300)
    alarm()


def set_alarm():
    # Get the number of minutes from the user
    minutes = int(e1.get())

    # Convert minutes to seconds
    seconds = minutes * 60

    # Sleep for the specified number of seconds
    time.sleep(seconds)

    # Call the alarm function
    alarm()


# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create a label
label1 = tk.Label(root, text="Enter the number of minutes:")
label1.pack()

# Create an entry widget
e1 = tk.Entry(root)
e1.pack()

# Create a set alarm button
button1 = tk.Button(root, text="Set Alarm", command=set_alarm)
button1.pack()

# Create a snooze button
button2 = tk.Button(root, text="Snooze", command=snooze)
button2.pack()

# Start the main event loop
root.mainloop()
