from tkinter import *
from tkinter import colorchooser

def click():
    color= colorchooser.askcolor()
    if color[1]:
        window.config(bg=color[1])
        color_label.config(text=f"Chosen Color:{color[1]}")
        print(color[-1])
    else:
        color_label.config(text="NO color chosen")
        print("YOU didn't use color nigga")
    # window.destroy() #if you wnant you can use it
window = Tk()

window.geometry("240x240")
button = Button(window,text="choose click me!!",command=click)
button.pack()

color_label = Label(window,text="Chosen Color:")
color_label.pack()

window.mainloop()


