from tkinter import *
import random
import os
from PIL import Image, ImageDraw, ImageFont

# Create the required images if they do not exist
for i in range(7):
    if not os.path.exists(f"{i}.png"):
        img = Image.new('RGB', (100, 100), color = (73, 109, 137))
        d = ImageDraw.Draw(img)
        d.text((10, 10), str(i), fill=(255, 255, 0))
        img.save(f"{i}.png")

# Check if all required images are in the directory
image_files = [f"{i}.png" for i in range(7)]
missing_files = [f for f in image_files if not os.path.exists(f)]

if missing_files:
    print(f"Missing image files: {missing_files}")
    exit()

def fname(name):
    img = PhotoImage(file=name)
    dice.config(image=img)
    dice.image = img

def chosedice():
    randvalue = random.randint(1, 6)
    choice = {
        1: '1.png',
        2: '2.png',
        3: '3.png',
        4: '4.png',
        5: '5.png',
        6: '6.png'
    }
    fname(choice[randvalue])

r = Tk()
r.title("Dice Roll Simulator")
frm = Frame(r)
btn = Button(frm, text="Click me to roll", font=('Arial', 10, 'bold'), fg='red', bg='black', command=chosedice)
img = PhotoImage(file="0.png")
dice = Label(frm, image=img)

btn.pack(pady=10)
dice.pack()

frm.place(relx=0.5, rely=0.5, anchor=CENTER)

r.mainloop()
