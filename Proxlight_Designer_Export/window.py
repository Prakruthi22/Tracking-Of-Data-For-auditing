from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x700")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 700,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

canvas.create_text(
    325.5, 109.5,
    text = "FINDING DIFFICULTY IN TRACKING ALL YOUR FINANCIAL RECORDS  ??\n\nYOU’RE AT THE RIGHT PLACE!!",
    fill = "#000000",
    font = ("Roboto-Medium", int(36.0)))

canvas.create_text(
    451.5, 338.0,
    text = "Login",
    fill = "#000000",
    font = ("Offside-Regular", int(48.0)))

canvas.create_text(
    459.0, 421.5,
    text = ".\n",
    fill = "#000000",
    font = ("Offside-Regular", int(36.0)))

canvas.create_text(
    435.5, 551.5,
    text = ".",
    fill = "#000000",
    font = ("Offside-Regular", int(36.0)))

window.resizable(False, False)
window.mainloop()
