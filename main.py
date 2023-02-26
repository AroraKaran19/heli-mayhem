#!/usr/bin/python3
import os
from tkinter import *
from tkinter import messagebox
import subprocess

background = "#20203d"

def exit():
    root.destroy()

def main_menu():
    global root
    root = Tk()
    root.title("Heli - Mayhem")
    root.resizable(False, False)
    
    canvas = Canvas(root, height=400, width=400, bg=background)
    canvas.pack()
    
    title = Label(canvas, text="Heli - Mayhem", bg=background, font=('Fira Sans', 30, "bold"), fg="black")
    canvas.create_window(200, 50, window=title)
    
    logo = PhotoImage(file=os.path.join("res", "drone.png"))
    img = Label(canvas, image=logo, background=background)
    canvas.create_window(200, 140, window=img)
    
    play_button = Button(canvas, text="Play", height=2, width=5, border=0, bg=background, font=('Fira Sans', 10), fg="white")
    canvas.create_window(200, 260, window=play_button)
    
    exit_button = Button(canvas, text="Exit", height=2, width=5, border=0, bg=background, font=('Fira Sans', 10), fg="white", command=exit)
    canvas.create_window(200, 350, window=exit_button)
    
    root.eval('tk::PlaceWindow . center')
    root.mainloop()
    
    root.mainloop()

if __name__ == "__main__":
    try: 
        import pygame
        from pygame import font
        main_menu()
    except ModuleNotFoundError:
        ask = messagebox.askyesno("Module Not Found!", "This program requires PYGAME Module\nDo you wish to install it?")
        if ask:
            result = subprocess.run(["pip", "install", "pygame"], capture_output=True)
            if result:
                messagebox.showinfo("PYGAME Module has been Installed!", "Module Installed Successfully!")
                main_menu()
            else:
                messagebox.showerror("Error", "Error")
