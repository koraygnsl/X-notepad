from tkinter.constants import BOTH, COMMAND, END, INSERT, LEFT, TRUE, WORD
from tkinter.filedialog import *
import tkinter as tk

def saveFile():
    new_file = asksaveasfile(mode = 'w', filetype = [('text files', 'txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode = 'r', filetype = [('text files', '.text')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)

def clearFile():
    entry.delete(1.0, END)


winbox = tk.Tk()
winbox.geometry("400x600")
winbox.title("NotePad X")
winbox.iconbitmap("C:\\Users\\murat\\Pictures\\cross.png ")
winbox.config(bg = "white")
top = tk.Frame(winbox)
top.pack(padx = 10, pady = 5, anchor = 'nw')

buttonOne = tk.Button(winbox, text="Open", bg="white", command= openFile)
buttonOne.pack(in_ = top, side =LEFT )

buttonTwo = tk.Button(winbox, text="Save", bg="white", command= saveFile)
buttonTwo.pack(in_ = top, side =LEFT)

buttonThree = tk.Button(winbox, text="Clear", bg="white", command= clearFile)
buttonThree.pack(in_ = top, side =LEFT)

buttonFour = tk.Button(winbox, text="Exit", bg="white", command= exit)
buttonFour.pack(in_ = top, side =LEFT)

entry = tk.Text(winbox, wrap = WORD, bg="white", font = ("arial", 15))
entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

winbox.mainloop()