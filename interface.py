import tkinter as tk
from PIL import Image
import MAIN

root = tk.Tk()
file = 'interface.gif'

root.configure(bg='black')

info = Image.open(file)
frames = info.n_frames
print(frames)

im = [tk.PhotoImage(file=file,format=f'gif -index {i}') for i in range(frames)]

anim = None
count=0
def animation(count):
    global anim
    im2 = im[count]
    gif_label.configure(image=im2)

    count += 1
    if count == frames:
        count = 0

    root.after(50,lambda :animation(count))
 
def execution():
    exec(MAIN)
gif_label = tk.Label(image="")
gif_label.pack()
start = tk.Button(text="start",command=lambda :animation(count),  )
start.pack()
run = tk.Button(text="run",command=lambda :execution())
run.pack()
root.mainloop()
