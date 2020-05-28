import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
       temp_apps = f.read()
       temp_apps = temp_apps.split(',')
       apps = [x for x in temp_apps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("Executables","*.exe"), ("All files","*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def run_apps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=600, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, fg="white", bg="#263D42", command=addApp)
runApps = tk.Button(root, text="Run Apps", padx=10, fg="white", bg="#263D42", command=run_apps)
openFile.pack()
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')