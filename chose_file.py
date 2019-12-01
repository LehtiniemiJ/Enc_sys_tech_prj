from tkinter import filedialog
from tkinter import *
def chose():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/home/jl/Documents/encryption",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
    return (root.filename)
