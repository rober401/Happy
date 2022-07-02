# Libarys
import os
import random
import time
import tkinter
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import time
import calendar
import datetime
from pytube import Playlist
# Color stuff
# Green – Quiet and restful, green is a soothing color that can invite harmony and diffuse anxiety.
# Blue – A highly peaceful color, blue can be especially helpful for stress management because it can encourage a powerful sense of calm.
# Purple – In many cultures, shades of violet represent strength, wisdom and peace.


import tkinter as tk





def show_frame(frame):
    frame.tkraise()


win = tk.Tk()

win.title('Let\'s take a minute to relax')
win.geometry('350x200')
win.resizable(width=False, height=False)

win.pack_propagate(0)
win.rowconfigure(0, weight=1)
win.columnconfigure(0, weight=1)

# Frames
Profile = tk.Frame(win)
Mainpage = tk.Frame(win)
Ratedaypage = tk.Frame(win)
Whatmadeufeel = tk.Frame(win)
Calender = tk.Frame(win)

# Ai = tk.Frame(win)

for frame in (Profile, Mainpage, Ratedaypage, Whatmadeufeel, Calender):
    frame.grid(row=0, column=0, sticky='nsew')


def reset_code():
    # Checking for reset code
    try:
        lines = [0, 1, 2, 3, 4, 5]
        CODE = []
        i = 0

        if 'RESET' in CODE:
            f = open("Saved_input.txt", "w")
            f.write(f"")
            f.close()

        with open("Saved_input.txt", "r+") as fp:
            while True:
                line = fp.readline()
                if i in lines:
                    CODE.append(line.strip())
                if i > lines[-1]:
                    break;
                i = i + 1
                pass
    except:
        pass
reset_code()
# Functions

def Secturty():
    path = (r"C:\Users\Rob\Desktop\Happy")
    dir_list = str(os.listdir(path))

    if "'README.txt'" in dir_list:
        pass

    elif "profileCo.txt" in dir_list:
        pass

    elif "Saved_input.txt" in dir_list:
        pass

    elif "Songs.txt" in dir_list:
        pass

    elif "Music Genres.txt" in dir_list:
        pass

    elif "Cutedog.jpg" in dir_list:
        pass

    elif "'Together.jpg'" in dir_list:
        pass

    else:
        quit()
Secturty()
def Changesize():
    win.geometry('600x300')


def Changesize_C():
    win.geometry('600x400')


def Saved_inputs():
    lines = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
             29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
             56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,
             83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
             108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
             129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]
    Asaves = []
    i = 0

    def Checkforsave():
        # ROW 1
        if 'C1b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C1b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C1b.place(x=42, y=80)

        if 'C2b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C2b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C2b.place(x=115, y=80)

        if 'C3b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C3b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C3b.place(x=190, y=80)

        if 'C4b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C4b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C4b.place(x=290, y=80)

        if 'C5b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C5b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C5b.place(x=372, y=80)

        if 'C6b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C6b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C6b.place(x=433, y=80)

        if 'C7b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C7b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C7b.place(x=512, y=80)

        if 'C8b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C8b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C8b.place(x=42, y=120)

        if 'C9b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C9b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C9b.place(x=115, y=120)

        if 'C10b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C10b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C10b.place(x=512, y=160)

        if 'C11b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C11b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C11b.place(x=290, y=120)

        if 'C12b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C12b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C12b.place(x=372, y=120)

        if 'C13b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C13b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C13b.place(x=433, y=120)

        if 'C14b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C14b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C14b.place(x=512, y=120)

        if 'C15b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C15b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C15b.place(x=42, y=160)

        if 'C16b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C16b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C16b.place(x=115, y=160)

        if 'C17b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C17b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C17b.place(x=190, y=160)

        if 'C18b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C18b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C18b.place(x=290, y=160)

        if 'C19b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C19b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C19b.place(x=372, y=160)

        if 'C20b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C20b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C20b.place(x=433, y=160)

        if 'C21b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C21b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C21b.place(x=512, y=160)

        if 'C22b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C22b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C22b.place(x=42, y=200)

        if 'C23b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C23b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C23b.place(x=115, y=200)

        if 'C24b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C24b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C24b.place(x=190, y=200)

        if 'C25b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C25b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C25b.place(x=290, y=200)

        if 'C26b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C26b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C26b.place(x=372, y=200)

        if 'C27b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C27b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C27b.place(x=433, y=200)

        if 'C28b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C28b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C28b.place(x=512, y=200)

        if 'C29b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C29b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C29b.place(x=42, y=240)

        if 'C30b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C30b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C30b.place(x=115, y=240)

        if 'C31b = tk.Label(Calender, text=f" 1 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C31b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C31b.place(x=190, y=240)

        # ROW 2
        if 'C1b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C1b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C1b.place(x=42, y=80)

        if 'C2b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C2b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C2b.place(x=115, y=80)

        if 'C3b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C3b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C3b.place(x=190, y=80)

        if 'C4b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C4b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C4b.place(x=290, y=80)

        if 'C5b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C5b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C5b.place(x=372, y=80)

        if 'C6b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C6b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C6b.place(x=433, y=80)

        if 'C7b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C7b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C7b.place(x=512, y=80)

        if 'C8b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C8b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C8b.place(x=42, y=120)

        if 'C9b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C9b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C9b.place(x=115, y=120)

        if 'C10b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C10b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C10b.place(x=512, y=160)

        if 'C11b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C11b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C11b.place(x=290, y=120)

        if 'C12b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C12b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C12b.place(x=372, y=120)

        if 'C13b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C13b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C13b.place(x=433, y=120)

        if 'C14b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C14b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C14b.place(x=512, y=120)

        if 'C15b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C15b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C15b.place(x=42, y=160)

        if 'C16b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C16b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C16b.place(x=115, y=160)

        if 'C17b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C17b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C17b.place(x=190, y=160)

        if 'C18b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C18b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C18b.place(x=290, y=160)

        if 'C19b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C19b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C19b.place(x=372, y=160)

        if 'C20b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C20b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C20b.place(x=433, y=160)

        if 'C21b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C21b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C21b.place(x=512, y=160)

        if 'C22b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C22b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C22b.place(x=42, y=200)

        if 'C23b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C23b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C23b.place(x=115, y=200)

        if 'C24b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C24b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C24b.place(x=190, y=200)

        if 'C25b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C25b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C25b.place(x=290, y=200)

        if 'C26b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C26b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C26b.place(x=372, y=200)

        if 'C27b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C27b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C27b.place(x=433, y=200)

        if 'C28b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C28b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C28b.place(x=512, y=200)

        if 'C29b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C29b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C29b.place(x=42, y=240)

        if 'C30b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C30b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C30b.place(x=115, y=240)

        if 'C31b = tk.Label(Calender, text=f" 2 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C31b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C31b.place(x=190, y=240)

        # ROW 3
        if 'C1b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C1b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C1b.place(x=42, y=80)

        if 'C2b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C2b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C2b.place(x=115, y=80)

        if 'C3b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C3b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C3b.place(x=190, y=80)

        if 'C4b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C4b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C4b.place(x=290, y=80)

        if 'C5b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C5b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C5b.place(x=372, y=80)

        if 'C6b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C6b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C6b.place(x=433, y=80)

        if 'C7b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C7b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C7b.place(x=512, y=80)

        if 'C8b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C8b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C8b.place(x=42, y=120)

        if 'C9b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C9b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C9b.place(x=115, y=120)

        if 'C10b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C10b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C10b.place(x=512, y=160)

        if 'C11b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C11b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C11b.place(x=290, y=120)

        if 'C12b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C12b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C12b.place(x=372, y=120)

        if 'C13b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C13b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C13b.place(x=433, y=120)

        if 'C14b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C14b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C14b.place(x=512, y=120)

        if 'C15b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C15b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C15b.place(x=42, y=160)

        if 'C16b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C16b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C16b.place(x=115, y=160)

        if 'C17b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C17b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C17b.place(x=190, y=160)

        if 'C18b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C18b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C18b.place(x=290, y=160)

        if 'C19b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C19b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C19b.place(x=372, y=160)

        if 'C20b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C20b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C20b.place(x=433, y=160)

        if 'C21b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C21b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C21b.place(x=512, y=160)

        if 'C22b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C22b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C22b.place(x=42, y=200)

        if 'C23b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C23b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C23b.place(x=115, y=200)

        if 'C24b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C24b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C24b.place(x=190, y=200)

        if 'C25b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C25b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C25b.place(x=290, y=200)

        if 'C26b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C26b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C26b.place(x=372, y=200)

        if 'C27b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C27b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C27b.place(x=433, y=200)

        if 'C28b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C28b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C28b.place(x=512, y=200)

        if 'C29b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C29b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C29b.place(x=42, y=240)

        if 'C30b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C30b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C30b.place(x=115, y=240)

        if 'C31b = tk.Label(Calender, text=f" 3 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C31b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C31b.place(x=190, y=240)
        # Row 4
        if 'C1b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C1b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C1b.place(x=42, y=80)

        if 'C2b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C2b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C2b.place(x=115, y=80)

        if 'C3b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C3b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C3b.place(x=190, y=80)

        if 'C4b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C4b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C4b.place(x=290, y=80)

        if 'C5b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C5b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C5b.place(x=372, y=80)

        if 'C6b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C6b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C6b.place(x=433, y=80)

        if 'C7b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C7b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C7b.place(x=512, y=80)

        if 'C8b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C8b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C8b.place(x=42, y=120)

        if 'C9b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C9b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C9b.place(x=115, y=120)

        if 'C10b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C10b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C10b.place(x=512, y=160)

        if 'C11b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C11b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C11b.place(x=290, y=120)

        if 'C12b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C12b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C12b.place(x=372, y=120)

        if 'C13b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C13b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C13b.place(x=433, y=120)

        if 'C14b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C14b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C14b.place(x=512, y=120)

        if 'C15b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C15b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C15b.place(x=42, y=160)

        if 'C16b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C16b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C16b.place(x=115, y=160)

        if 'C17b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C17b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C17b.place(x=190, y=160)

        if 'C18b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C18b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C18b.place(x=290, y=160)

        if 'C19b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C19b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C19b.place(x=372, y=160)

        if 'C20b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C20b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C20b.place(x=433, y=160)

        if 'C21b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C21b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C21b.place(x=512, y=160)

        if 'C22b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C22b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C22b.place(x=42, y=200)

        if 'C23b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C23b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C23b.place(x=115, y=200)

        if 'C24b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C24b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C24b.place(x=190, y=200)

        if 'C25b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C25b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C25b.place(x=290, y=200)

        if 'C26b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C26b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C26b.place(x=372, y=200)

        if 'C27b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C27b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C27b.place(x=433, y=200)

        if 'C28b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C28b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C28b.place(x=512, y=200)

        if 'C29b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C29b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C29b.place(x=42, y=240)

        if 'C30b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C30b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C30b.place(x=115, y=240)

        if 'C31b = tk.Label(Calender, text=f" 4 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C31b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C31b.place(x=190, y=240)
        # ROW 5
        if 'C1b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C1b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C1b.place(x=42, y=80)

        if 'C2b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C2b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C2b.place(x=115, y=80)

        if 'C3b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C3b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C3b.place(x=190, y=80)

        if 'C4b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C4b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C4b.place(x=290, y=80)

        if 'C5b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C5b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C5b.place(x=372, y=80)

        if 'C6b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C6b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C6b.place(x=433, y=80)

        if 'C7b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C7b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C7b.place(x=512, y=80)

        if 'C8b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C8b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C8b.place(x=42, y=120)

        if 'C9b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C9b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C9b.place(x=115, y=120)

        if 'C10b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C10b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C10b.place(x=512, y=160)

        if 'C11b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C11b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C11b.place(x=290, y=120)

        if 'C12b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C12b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C12b.place(x=372, y=120)

        if 'C13b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C13b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C13b.place(x=433, y=120)

        if 'C14b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C14b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C14b.place(x=512, y=120)

        if 'C15b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C15b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C15b.place(x=42, y=160)

        if 'C16b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C16b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C16b.place(x=115, y=160)

        if 'C17b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C17b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C17b.place(x=190, y=160)

        if 'C18b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C18b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C18b.place(x=290, y=160)

        if 'C19b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C19b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C19b.place(x=372, y=160)

        if 'C20b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C20b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C20b.place(x=433, y=160)

        if 'C21b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C21b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C21b.place(x=512, y=160)

        if 'C22b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C22b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C22b.place(x=42, y=200)

        if 'C23b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C23b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C23b.place(x=115, y=200)

        if 'C24b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C24b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C24b.place(x=190, y=200)

        if 'C25b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C25b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C25b.place(x=290, y=200)

        if 'C26b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C26b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C26b.place(x=372, y=200)

        if 'C27b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C27b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C27b.place(x=433, y=200)

        if 'C28b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C28b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C28b.place(x=512, y=200)

        if 'C29b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C29b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C29b.place(x=42, y=240)

        if 'C30b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C30b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C30b.place(x=115, y=240)

        if 'C31b = tk.Label(Calender, text=f" 5 ", font="times 15", bg=\'light blue\', borderwidth=2,relief="groove")' in Asaves:
            C31b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            C31b.place(x=190, y=240)

        if 'RESET' in Asaves:
            f = open("Saved_input.txt", "w")
            f.write(f"")
            f.close()

    with open("Saved_input.txt", "r+") as fp:
        while True:
            line = fp.readline()
            if i in lines:
                Asaves.append(line.strip())
            if i > lines[-1]:
                Checkforsave()
                break;
            i = i + 1

def reset():
    f = open("Saved_input.txt", "w")
    f.write(f"RESET")
    f.close()

    f = open("Saved_input.txt", "w")
    f.write(f"")
    f.close()

    quit()

def calculateMusic():
    RockLIST = ["https://www.youtube.com/watch?v=ErvgV4P6Fzc&list=PL7jltt09rbExM1jU0dB8ajHFlofSKxeHQ",
                "https://www.youtube.com/watch?v=8295rOMvtQI&list=PL2tb4KBOS-tlw4Drtem0GCyKkUqfvwzp7",
                "https://www.youtube.com/watch?v=Ud4HuAzHEUc&list=PLTFJ2bxPtLTd6bzHwoDmBqzSHP5EjHkHi",
                "https://www.youtube.com/watch?v=pAgnJDJN4VA&list=RDQMqWHGGVJuIsA&start_radio=1",
                "https://www.youtube.com/watch?v=UrIiLvg58SY&list=PLpOehZ0r85ixl-tdCfLqH7JmZe7BwxM2L",
                "https://www.youtube.com/watch?v=g8z-qP34-1Y&list=PLlOll-NAMPotWYOYkLqP4u16fERVfF56E"]
    PopLIST = ["https://www.youtube.com/watch?v=iKzRIweSBLA&list=PLwpFrtWg2EJF3KZy3URO7qZ3fpoZPH-ex",
               "https://www.youtube.com/watch?v=CveANi17YfU&list=PL3-sRm8xAzY-w9GS19pLXMyFRTuJcuUjy",
               "https://www.youtube.com/watch?v=KrgJp7Z1Hv8&list=PLgzTt0k8mXzHcKebL8d0uYHfawiARhQja",
               "https://www.youtube.com/watch?v=OpQFFLBMEPI&list=RDQMCMiuwb0BlcY&start_radio=1",
               "https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PL6BA2D5208E8EF161",
               "https://www.youtube.com/watch?v=CveANi17YfU&list=PL3-sRm8xAzY-w9GS19pLXMyFRTuJcuUjy"]
    Hip_HopLIST = ["https://www.youtube.com/watch?v=2Mu7LAhxyp8&list=RDnDDzUyGvloE&start_radio=1",
                   "https://www.youtube.com/watch?v=MGhSsRGCM7U&list=PLTmaZB7buLofEvaP2Igrd8_tde6iC1ws1",
                   "https://www.youtube.com/watch?v=MGhSsRGCM7U&list=PLTmaZB7buLofEvaP2Igrd8_tde6iC1ws1",
                   "https://www.youtube.com/watch?v=SLsTskih7_I&list=PL6FZAmQwSblcLD6QzwbU3_jvq8Mc_gtCs",
                   "https://www.youtube.com/watch?v=jb6HZa151s8&list=PLenIjFQBKQH4PIiefeQUw_60IWEY1iPrp",
                   "https://www.youtube.com/watch?v=MGhSsRGCM7U&list=PLTmaZB7buLofEvaP2Igrd8_tde6iC1ws1"]
    Rhythm_and_bluesLIST = ["https://www.youtube.com/watch?v=rqqAnjY2Rmo&list=PLfUMJyOkx98Fv7Wo4lFVtAtIuyg4LJNtR",
                            "https://www.youtube.com/watch?v=LWqHLULuMUA&list=PLFKvKs_qHyI7DMSULb51VSnzHAQ3z44DT",
                            "https://www.youtube.com/watch?v=LWqHLULuMUA&list=PLFKvKs_qHyI7DMSULb51VSnzHAQ3z44DT",
                            "https://www.youtube.com/watch?v=8WYHDfJDPDc&list=PLGBuKfnErZlCS2d4oJQY6LmPRTDSO2-FW",
                            "https://www.youtube.com/watch?v=6YNZlXfW6Ho&list=PLplXQ2cg9B_okySP1Z7MTETWHRKCj1fJ-",
                            "https://www.youtube.com/watch?v=LWqHLULuMUA&list=PLFKvKs_qHyI7DMSULb51VSnzHAQ3z44DT"]
    JazzLIST = ["https://www.youtube.com/watch?v=ZZcuSBouhVA&list=PL8F6B0753B2CCA128",
                "https://www.youtube.com/watch?v=z4PKzz81m5c&list=PL1jUtM1tmw6CLyH-s7Goq9ofwMtAnrwD4",
                "https://www.youtube.com/watch?v=z4PKzz81m5c&list=PL1jUtM1tmw6CLyH-s7Goq9ofwMtAnrwD4",
                "https://www.youtube.com/watch?v=Y-JQ-RCyPpQ&list=RDY-JQ-RCyPpQ&start_radio=1",
                "https://www.youtube.com/watch?v=_WcWHZc8s2I&list=PLh7IzJ3mFYA4KMbZHo93g9_ynU7XWAvQW",
                "https://www.youtube.com/watch?v=z4PKzz81m5c&list=PL1jUtM1tmw6CLyH-s7Goq9ofwMtAnrwD4"]
    FolkLIST = ["https://www.youtube.com/watch?v=_PLq0_7k1jk&list=PLGBuKfnErZlAn6KQURHt9biYXrIcHZbKW",
                "https://www.youtube.com/watch?v=KQetemT1sWc&list=PLGBuKfnErZlBLNzS_JlDAeiH5aW26rvHc",
                "https://www.youtube.com/watch?v=k8Mc8YRigmw&list=PLSDt8OAN0wbF42vrACaH1Js-qCD3Aei03",
                "https://www.youtube.com/watch?v=K-5EDwy0Xho&list=PLo3pNg0eiPc8HrbDZQ-8awp7JRoGVdftY",
                "https://www.youtube.com/watch?v=vq2wZyi4vBE&list=PL0Whem5OxgRONHJ1it9Dv6w1ockq-s-8y",
                "https://www.youtube.com/watch?v=KQetemT1sWc&list=PLGBuKfnErZlBLNzS_JlDAeiH5aW26rvHc"]
    CountryLIST = ["https://www.youtube.com/watch?v=0xXD9-1mLBY&list=PLL4ZEHd9T5ZYheoYbj6Lr4Sc33HbztjQ7",
                   "https://www.youtube.com/watch?v=eM213aMKTHg&list=PLvFYFNbi-IBHkSxfeh_Q-QKGsCRgYd72A",
                   "https://www.youtube.com/watch?v=eM213aMKTHg&list=PLvFYFNbi-IBHkSxfeh_Q-QKGsCRgYd72A",
                   "https://www.youtube.com/watch?v=0xXD9-1mLBY&list=PLL4ZEHd9T5ZYheoYbj6Lr4Sc33HbztjQ7",
                   "https://www.youtube.com/watch?v=zDo0H8Fm7d0&list=PLSgTywHngOwMlZpv8laCA_wTQCC31yDg4",
                   "https://www.youtube.com/watch?v=IZbN_nmxAGk&list=PLbnfhymC8OwT5QG3SmLLb25rvHW3OM6Hk"]
    ClassicalLIST = ["https://www.youtube.com/watch?v=P2l0lbn5TVg&list=PL2788304DC59DBEB4",
                     "https://www.youtube.com/watch?v=qq09UkPRdFY&list=PLwNv9Hhd8gZjNoQdpd2kBa3fwXNeJjzDX",
                     " https://www.youtube.com/watch?v=P2l0lbn5TVg&list=PL2788304DC59DBEB4",
                     "https://www.youtube.com/watch?v=qq09UkPRdFY&list=PLwNv9Hhd8gZjNoQdpd2kBa3fwXNeJjzDX",
                     "https://www.youtube.com/watch?v=qq09UkPRdFY&list=PLwNv9Hhd8gZjNoQdpd2kBa3fwXNeJjzDX",
                     "https://www.youtube.com/watch?v=P2l0lbn5TVg&list=PL2788304DC59DBEB4"]
    Electronic_danceLIST = ["https://www.youtube.com/watch?v=oC-GflRB0y4&list=PLw6eTMMKY24QLYfmrU2rB8x-lP5Fas2dY",
                            "https://www.youtube.com/watch?v=cwOa0HcT2d0&list=PLN5xhqjiEOrDtlRORl0qBAEd7cJbgvlev",
                            "https://www.youtube.com/watch?v=oC-GflRB0y4&list=PLw6eTMMKY24QLYfmrU2rB8x-lP5Fas2dY",
                            "https://www.youtube.com/watch?v=e7HBypw4lhY&list=PLgzTt0k8mXzHksBAyoa15hjvGBfwaZ2fY",
                            "https://www.youtube.com/watch?v=e7HBypw4lhY&list=PLgzTt0k8mXzHksBAyoa15hjvGBfwaZ2fY",
                            "https://www.youtube.com/watch?v=cwOa0HcT2d0&list=PLN5xhqjiEOrDtlRORl0qBAEd7cJbgvlev"]
    Alternative_rockLIST = ["https://www.youtube.com/channel/UCj5JkqIJaPQ6DOibFFPTM6g",
                            "https://www.youtube.com/channel/UCj5JkqIJaPQ6DOibFFPTM6g",
                            "https://www.youtube.com/channel/UCj5JkqIJaPQ6DOibFFPTM6g",
                            "https://www.youtube.com/watch?v=hTWKbfoikeg&list=PLD58ECddxRngHs9gZPQWOCAKwV1hTtYe4",
                            "https://www.youtube.com/watch?v=gS9o1FAszdk&list=PLNMTXgsQnLlANICjq56Qg1rQubU8LNLwL",
                            "https://www.youtube.com/channel/UCj5JkqIJaPQ6DOibFFPTM6g"]
    SingingLIST = ["https://www.youtube.com/watch?v=PoaT6WXUV_M&list=PLsQujjGx2zbIRBlRt200nl7sfhQUEj2ON",
                   "https://www.youtube.com/watch?v=2Vv-BfVoq4g&list=PL7v1FHGMOadDghZ1m-jEIUnVUsGMT9jbH",
                   "https://www.youtube.com/watch?v=PoaT6WXUV_M&list=PLsQujjGx2zbIRBlRt200nl7sfhQUEj2ON",
                   "https://www.youtube.com/watch?v=K-5EDwy0Xho&list=PLo3pNg0eiPc8HrbDZQ-8awp7JRoGVdftY",
                   "https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLMws9SCqJ1JCeVMVPsdamuUM0HK0MbA6g",
                   "https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLMws9SCqJ1JCeVMVPsdamuUM0HK0MbA6g"]
    Heavy_metalLIST = ["https://www.youtube.com/watch?v=xnKhsTXoKCI&list=PLhQCJTkrHOwSX8LUnIMgaTq3chP1tiTut",
                       "https://www.youtube.com/watch?v=kXYiU_JCYtU&list=PLKz7GpiORb4cqSnRd9jLIxbPbDHyVPjwz",
                       "https://www.youtube.com/watch?v=kXYiU_JCYtU&list=PLKz7GpiORb4cqSnRd9jLIxbPbDHyVPjwz",
                       "https://www.youtube.com/watch?v=xnKhsTXoKCI&list=PLhQCJTkrHOwSX8LUnIMgaTq3chP1tiTut",
                       "https://www.youtube.com/watch?v=94bGzWyHbu0&list=PLOUzUrKhNae6JqXAjG56Akc79vuzYCOYz",
                       "https://www.youtube.com/watch?v=xnKhsTXoKCI&list=PLhQCJTkrHOwSX8LUnIMgaTq3chP1tiTut"]
    SoulLIST = ["https://www.youtube.com/watch?v=6YNZlXfW6Ho&list=PLplXQ2cg9B_okySP1Z7MTETWHRKCj1fJ-",
                "https://www.youtube.com/watch?v=rUSddpvB4X0&list=PLesydLs-NkJ-UtmpLJeD3Kdzt1xqB48Nq",
                "https://www.youtube.com/watch?v=rUSddpvB4X0&list=PLesydLs-NkJ-UtmpLJeD3Kdzt1xqB48Nq",
                "https://www.youtube.com/watch?v=6YNZlXfW6Ho&list=PLplXQ2cg9B_okySP1Z7MTETWHRKCj1fJ-",
                "https://www.youtube.com/watch?v=rUSddpvB4X0&list=PLesydLs-NkJ-UtmpLJeD3Kdzt1xqB48Nq",
                "https://www.youtube.com/watch?v=6YNZlXfW6Ho&list=PLplXQ2cg9B_okySP1Z7MTETWHRKCj1fJ-"]
    InstrumentalLIST = ["https://www.youtube.com/watch?v=Ri3WsPDi4MY&list=RDRi3WsPDi4MY&start_radio=1",
                        "https://www.youtube.com/watch?v=Ri3WsPDi4MY&list=RDRi3WsPDi4MY&start_radio=1",
                        "https://www.youtube.com/watch?v=8yYpQi96bng&list=PLrgkRQ9954-Rv7gNesYeAzmjwzuBbkM47",
                        "https://www.youtube.com/watch?v=8yYpQi96bng&list=PLrgkRQ9954-Rv7gNesYeAzmjwzuBbkM47",
                        "https://www.youtube.com/watch?v=Ri3WsPDi4MY&list=RDRi3WsPDi4MY&start_radio=1",
                        "https://www.youtube.com/watch?v=8yYpQi96bng&list=PLrgkRQ9954-Rv7gNesYeAzmjwzuBbkM47"]
    DanceLIST = ["https://www.youtube.com/watch?v=taSubkjZUA4&list=PL6Go6XFhidEAH6LrK-RKxR5xwhdZ0g4vm",
                 "https://www.youtube.com/watch?v=taSubkjZUA4&list=PL6Go6XFhidEAH6LrK-RKxR5xwhdZ0g4vm",
                 "https://www.youtube.com/watch?v=1AJmKkU5POA&list=PL1tswHXyCDmcnX2itIRS9PUnPRM7CoCVU",
                 "https://www.youtube.com/watch?v=ypQZV03l80g&list=RDypQZV03l80g&start_radio=1",
                 "https://www.youtube.com/watch?v=1AJmKkU5POA&list=PL1tswHXyCDmcnX2itIRS9PUnPRM7CoCVU",
                 "https://www.youtube.com/watch?v=1AJmKkU5POA&list=PL1tswHXyCDmcnX2itIRS9PUnPRM7CoCVU"]
    Pop_rockLIST = ["https://www.youtube.com/watch?v=hT_nvWreIhg&list=PLTC7VQ12-9rZRMqzpt9t69WxbcBBcMA5N",
                    "https://www.youtube.com/watch?v=8295rOMvtQI&list=PL2tb4KBOS-tlw4Drtem0GCyKkUqfvwzp7",
                    "https://www.youtube.com/watch?v=eVTXPUF4Oz4&list=PL2hGGKKbxvqIuHrIBEeNjytlqPAcnjuOS",
                    "https://www.youtube.com/watch?v=hT_nvWreIhg&list=PLTC7VQ12-9rZRMqzpt9t69WxbcBBcMA5N",
                    "https://www.youtube.com/watch?v=UrIiLvg58SY&list=PLpOehZ0r85ixl-tdCfLqH7JmZe7BwxM2L",
                    "https://www.youtube.com/watch?v=hT_nvWreIhg&list=PLTC7VQ12-9rZRMqzpt9t69WxbcBBcMA5N"]
    FunkLIST = ["https://www.youtube.com/watch?v=OPf0YbXqDm0&list=PL7IyjolaORJ1kM2JEO4s9VGp4CUJZu5Gr",
                "https://www.youtube.com/watch?v=mbQhFqfnHyc&list=PLsCmb0qV7ti9cm9OU5n-mg9lACANBtsGo",
                "https://www.youtube.com/watch?v=mbQhFqfnHyc&list=PLsCmb0qV7ti9cm9OU5n-mg9lACANBtsGo",
                "https://www.youtube.com/watch?v=OPf0YbXqDm0&list=PL7IyjolaORJ1kM2JEO4s9VGp4CUJZu5Gr",
                "https://www.youtube.com/watch?v=Nm-ISatLDG0&list=PLivVJZQFKuWeHD9Vy-qDuARi6NeFBc2EX",
                "https://www.youtube.com/watch?v=OPf0YbXqDm0&list=PL7IyjolaORJ1kM2JEO4s9VGp4CUJZu5Gr"]

    MUSICLIKED = []

    lines = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    result = []
    i = 0

    with open("Music Genres.txt", "r+") as fp:
        # access each line
        while True:
            line = fp.readline()
            # check line number
            if i in lines:
                result.append(line.strip())
            # line number greater than needed exit the loop
            # lines[-1] give last item from list
            if i > lines[-1]:
                break;
            i = i + 1

    def main():

        if 'Rock = 1' in result:
            MUSICLIKED.append("Rock")

        if 'Pop  = 1' in result:
            MUSICLIKED.append("Pop")

        if 'Hip Hop = 1' in result:
            MUSICLIKED.append("Hip Hop")

        if 'Rhythm and blues = 1' in result:
            MUSICLIKED.append("Rhythm and blues")

        if 'Jazz = 1' in result:
            MUSICLIKED.append("Jazz")

        if 'Folk = 1' in result:
            MUSICLIKED.append("Folk")

        if 'Country = 1' in result:
            MUSICLIKED.append("Country")

        if 'Classical = 1' in result:
            MUSICLIKED.append("Classical")

        if 'Electronic dance = 1' in result:
            MUSICLIKED.append("Electronic dance")

        if 'Alternative rock = 1' in result:
            MUSICLIKED.append("Alternative rock")

        if 'Singing = 1' in result:
            MUSICLIKED.append("Singing")

        if 'Heavy metal = 1' in result:
            MUSICLIKED.append("Heavy metal")

        if 'Soul = 1' in result:
            MUSICLIKED.append("Soul")

        if 'Instrumental = 1' in result:
            MUSICLIKED.append("Instrumental")

        if 'Dance = 1' in result:
            MUSICLIKED.append("Dance")

        if 'Pop rock = 1' in result:
            MUSICLIKED.append("Pop rock")

        if 'Funk = 1' in result:
            MUSICLIKED.append("Funk")

    if __name__ == '__main__':
        main()

    PICKEDMUSIC = random.choice(MUSICLIKED)

    if PICKEDMUSIC == "Rock":
        selectedmusic = random.choice(RockLIST)

    elif PICKEDMUSIC == "Pop":
        selectedmusic = random.choice(PopLIST)

    elif PICKEDMUSIC == "Hip Hop":
        selectedmusic = random.choice(Hip_HopLIST)

    elif PICKEDMUSIC == "Rhythm and blues":
        selectedmusic = random.choice(Rhythm_and_bluesLIST)

    elif PICKEDMUSIC == "Jazz":
        selectedmusic = random.choice(JazzLIST)

    elif PICKEDMUSIC == "Folk":
        selectedmusic = random.choice(FolkLIST)

    elif PICKEDMUSIC == "Country":
        selectedmusic = random.choice(CountryLIST)

    elif PICKEDMUSIC == "Classical":
        selectedmusic = random.choice(ClassicalLIST)

    elif PICKEDMUSIC == "Electronic dance":
        selectedmusic = random.choice(Electronic_danceLIST)

    elif PICKEDMUSIC == "Alternative rock":
        selectedmusic = random.choice(Alternative_rockLIST)

    elif PICKEDMUSIC == "Singing":
        selectedmusic = random.choice(SingingLIST)

    elif PICKEDMUSIC == "Heavy metal":
        selectedmusic = random.choice(Heavy_metalLIST)

    elif PICKEDMUSIC == "Soul":
        selectedmusic = random.choice(SoulLIST)

    elif PICKEDMUSIC == "Instrumental":
        selectedmusic = random.choice(InstrumentalLIST)

    elif PICKEDMUSIC == "Dance":
        selectedmusic = random.choice(DanceLIST)

    elif PICKEDMUSIC == "Pop rock":
        selectedmusic = random.choice(PopLIST)

    elif PICKEDMUSIC == "Funk":
        selectedmusic = random.choice(FunkLIST)

    def getplaylist(playlists):
        try:
            urls = []

            for playlist in playlists:
                playlist_urls = Playlist(playlist)

                for url in playlist_urls:
                    urls.append(url)

            return urls
        except:
            Errorb = tk.Label(Calender, text=f"Music: No Wifi Connection ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
            Errorb.place(x=20, y=280)

    try:
        playlist = [selectedmusic]
        pl_urls = getplaylist(playlist)

        with open('Songs.txt', 'w') as f:
            for url in pl_urls:
                f.write(url + '\n')

        f = open('Songs.txt', "r")

        x = random.randint(1, 40)

        for I in range(x):
            link = (f.readline())

        link = (f.readline())
        musicb = tk.Label(Calender, text=f"Music: {link} ", font="times 15", bg='light blue', borderwidth=2,
                          relief="groove")
        musicb.place(x=20, y=280)
    except:
        Errorb = tk.Label(Calender, text=f"Music: No Wifi Connection ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        Errorb.place(x=20, y=280)

def close():
    quit()


def Onceopen():
    MusicCount = (f"""
Rock = {w1V.get()}
Pop = {w2V.get()}
Hip Hop = {w3V.get()}
Rhythm and blues = {w4V.get()}
Jazz = {w5V.get()}
Folk = {w6V.get()}
Country = {w7V.get()}
Classical = {w8V.get()}
Electronic dance = {w9V.get()}
Alternative rock = {w10V.get()}
Singing = {w11V.get()}
Heavy metal = {w12V.get()}
Soul = {w13V.get()}
Instrumental = {w14V.get()}
Dance = {w15V.get()}
Pop rock = {w16V.get()}
Funk = {w17V.get()}   
    """)

    f = open("Music Genres.txt", "w")
    f.write(f"{MusicCount}")
    f.close()

    f = open("profileCo.txt", "w")
    f.write("profileCount = 1")
    f.close()
    quit()  # Collected music


# Profile will only appear once
Profile_Title = tk.Label(Profile, text='Profile', font='times 18', bg='light blue')
Profile_Title.pack()
Profile.configure(bg='light blue')

Close = tk.Button(Profile, text="Save & Continue", width=14, height=2, command=lambda: ([Onceopen()]))
Close.place(x=180, y=340)

Profile_never = tk.Label(Profile, text='[!] This will only appear once', font='times 10', bg='light blue')
Profile_never.place(x=120, y=310)

Profile_music = tk.Label(Profile, text='[!] We only collect music types', font='times 10', bg='light blue')
Profile_music.place(x=120, y=290)
# Check Box
# Var - CheckBoxs
w1V = IntVar()
w2V = IntVar()
w3V = IntVar()
w4V = IntVar()
w5V = IntVar()
w6V = IntVar()
w7V = IntVar()
w8V = IntVar()
w9V = IntVar()
w10V = IntVar()
w11V = IntVar()
w12V = IntVar()
w13V = IntVar()
w14V = IntVar()
w15V = IntVar()
w16V = IntVar()
w17V = IntVar()

# w1V.get()

w1 = tk.Checkbutton(Profile, text="Rock", variable=w1V)
w2 = tk.Checkbutton(Profile, text="Pop", variable=w2V)
w3 = tk.Checkbutton(Profile, text="Hip Hop", variable=w3V)
w4 = tk.Checkbutton(Profile, text="Rhythm and blues", variable=w4V)
w5 = tk.Checkbutton(Profile, text="Jazz", variable=w5V)
w6 = tk.Checkbutton(Profile, text="Folk", variable=w6V)
w7 = tk.Checkbutton(Profile, text="Country", variable=w7V)
w8 = tk.Checkbutton(Profile, text="Classical", variable=w8V)
w9 = tk.Checkbutton(Profile, text="Electronic dance", variable=w9V)
w10 = tk.Checkbutton(Profile, text="Alternative rock", variable=w10V)
w11 = tk.Checkbutton(Profile, text="Singing", variable=w11V)
w12 = tk.Checkbutton(Profile, text="Heavy metal", variable=w12V)
w13 = tk.Checkbutton(Profile, text="Soul", variable=w13V)
w14 = tk.Checkbutton(Profile, text="Instrumental", variable=w14V)
w15 = tk.Checkbutton(Profile, text="Dance", variable=w15V)
w16 = tk.Checkbutton(Profile, text="Pop rock", variable=w16V)
w17 = tk.Checkbutton(Profile, text="Funk", variable=w17V)

w1.place(x=24, y=24)
w2.place(x=24, y=44)
w3.place(x=24, y=64)
w4.place(x=24, y=84)
w5.place(x=24, y=104)
w6.place(x=24, y=124)
w7.place(x=24, y=144)
w8.place(x=24, y=164)
w9.place(x=24, y=184)
w10.place(x=24, y=204)
w11.place(x=24, y=224)
w12.place(x=24, y=244)
w13.place(x=24, y=264)
w14.place(x=24, y=284)
w15.place(x=24, y=304)
w16.place(x=24, y=324)
w17.place(x=24, y=344)

# ==================Frame 1 code
Mainpage_title = tk.Label(Mainpage, text='Let\'s Start Today \n Great!', font='times 15', bg='light blue')
Mainpage_title.pack()

# CONFIGURE
Mainpage.configure(bg='light blue')
img = ImageTk.PhotoImage(Image.open("Cutedog.jpg"))  # IMAGE
IMG = Label(Mainpage, image=img, bg='light blue')
IMG.pack(pady="10")

Mainpage_btn = tk.Button(Mainpage, text="Continue", width=7, height=2, command=lambda: show_frame(Ratedaypage))
Mainpage_btn.place(x=290, y=150)

# ==================Frame 2 code

Ratedaypage_title = tk.Label(Ratedaypage, text='Rate your day?', font='times 15', bg='light blue')
Ratedaypage_title.pack()

# CONFIGURE
Ratedaypage.configure(bg='light blue')

Ratedaypage.rowconfigure(0, weight=1)
Ratedaypage.columnconfigure(0, weight=1)

img1 = ImageTk.PhotoImage(Image.open("Together.jpg"))  # IMAGE
IMG1 = Label(Ratedaypage, image=img1, bg='light blue')
IMG1.pack(pady="10")


def RateOne():
    Needmonth = str(datetime.date.today().month)
    month_num = Needmonth
    datetime_object = datetime.datetime.strptime(month_num, "%m")
    full_month_name = datetime_object.strftime("%B")

    if full_month_name == "September":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "October":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "November":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    elif full_month_name == "December":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "January":
        dayint = (datetime.date.today().day)
        dayint = dayint + 5
        daystr = str(dayint)

    elif full_month_name == "February":
        dayint = (datetime.date.today().day)
        dayint = dayint + 1
        daystr = str(dayint)

    elif full_month_name == "March":
        dayint = (datetime.date.today().day)
        dayint = dayint + 1
        daystr = str(dayint)

    elif full_month_name == "April":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "May":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    elif full_month_name == "June":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "July":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "August":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    else:
        print("error")
        quit()

    Corretday = ("C" + daystr)

    if Corretday == "C1":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC1b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C1b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C1b.place(x=42, y=80)

    if Corretday == "C2":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC2b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C2b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C2b.place(x=115, y=80)

    if Corretday == "C3":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC3b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C3b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C3b.place(x=190, y=80)

    if Corretday == "C4":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC4b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C4b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C4b.place(x=290, y=80)

    if Corretday == "C5":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC5b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C5b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C5b.place(x=372, y=80)

    if Corretday == "C6":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC6b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C6b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C6b.place(x=433, y=80)

    if Corretday == "C7":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC7b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C7b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C7b.place(x=512, y=80)

    if Corretday == "C8":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC8b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C8b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C8b.place(x=42, y=120)

    if Corretday == "C9":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC9b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C9b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C9b.place(x=115, y=120)

    if Corretday == "C10":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC10b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C10b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C10b.place(x=512, y=160)

    if Corretday == "C11":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC11b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C11b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C11b.place(x=290, y=120)

    if Corretday == "C12":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC12b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C12b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C12b.place(x=372, y=120)

    if Corretday == "C13":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC13b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C13b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C13b.place(x=433, y=120)

    if Corretday == "C14":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC14b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C14b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C14b.place(x=512, y=120)

    if Corretday == "C15":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC15b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C15b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C15b.place(x=42, y=160)

    if Corretday == "C16":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC16b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C16b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C16b.place(x=115, y=160)

    if Corretday == "C17":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC17b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C17b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C17b.place(x=190, y=160)

    if Corretday == "C18":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC18b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C18b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C18b.place(x=290, y=160)

    if Corretday == "C19":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC19b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C19b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C19b.place(x=372, y=160)

    if Corretday == "C20":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC20b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C20b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C20b.place(x=433, y=160)

    if Corretday == "C21":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC21b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C21b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C21b.place(x=512, y=160)

    if Corretday == "C22":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC22b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C22b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C22b.place(x=42, y=200)

    if Corretday == "C23":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC23b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C23b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C23b.place(x=115, y=200)

    if Corretday == "C24":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC24b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C24b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C24b.place(x=190, y=200)

    if Corretday == "C25":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC25b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C25b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C25b.place(x=290, y=200)

    if Corretday == "C26":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC26b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C26b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C26b.place(x=372, y=200)

    if Corretday == "C27":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC27b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C27b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C27b.place(x=433, y=200)

    if Corretday == "C28":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC28b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C28b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C28b.place(x=512, y=200)

    if Corretday == "C29":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC29b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C29b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C29b.place(x=42, y=240)

    if Corretday == "C30":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC30b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C30b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C30b.place(x=115, y=240)

    if Corretday == "C31":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC31b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C31b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C31b.place(x=190, y=240)

        # save somthing like


# C21b = tk.Label(Calender, text=f" 1 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")
# C21b.place(x=512, y=160)
# in a file to 'save it'

def RateTwo():
    Needmonth = str(datetime.date.today().month)
    month_num = Needmonth
    datetime_object = datetime.datetime.strptime(month_num, "%m")
    full_month_name = datetime_object.strftime("%B")

    if full_month_name == "September":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "October":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "November":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    elif full_month_name == "December":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "January":
        dayint = (datetime.date.today().day)
        dayint = dayint + 5
        daystr = str(dayint)

    elif full_month_name == "February":
        dayint = (datetime.date.today().day)
        dayint = dayint + 1
        daystr = str(dayint)

    elif full_month_name == "March":
        dayint = (datetime.date.today().day)
        dayint = dayint + 1
        daystr = str(dayint)

    elif full_month_name == "April":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "May":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    elif full_month_name == "June":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "July":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "August":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    else:
        print("error")
        quit()

    Corretday = ("C" + daystr)

    if Corretday == "C1":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC1b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C1b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C1b.place(x=42, y=80)

    if Corretday == "C2":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC2b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C2b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C2b.place(x=115, y=80)

    if Corretday == "C3":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC3b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C3b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C3b.place(x=190, y=80)

    if Corretday == "C4":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC4b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C4b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C4b.place(x=290, y=80)

    if Corretday == "C5":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC5b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C5b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C5b.place(x=372, y=80)

    if Corretday == "C6":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC6b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C6b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C6b.place(x=433, y=80)

    if Corretday == "C7":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC7b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C7b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C7b.place(x=512, y=80)

    if Corretday == "C8":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC8b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C8b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C8b.place(x=42, y=120)

    if Corretday == "C9":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC9b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C9b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C9b.place(x=115, y=120)

    if Corretday == "C10":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC10b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C10b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C10b.place(x=512, y=160)

    if Corretday == "C11":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC11b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C11b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C11b.place(x=290, y=120)

    if Corretday == "C12":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC12b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C12b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C12b.place(x=372, y=120)

    if Corretday == "C13":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC13b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C13b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C13b.place(x=433, y=120)

    if Corretday == "C14":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC14b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C14b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C14b.place(x=512, y=120)

    if Corretday == "C15":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC15b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C15b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C15b.place(x=42, y=160)

    if Corretday == "C16":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC16b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C16b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C16b.place(x=115, y=160)

    if Corretday == "C17":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC17b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C17b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C17b.place(x=190, y=160)

    if Corretday == "C18":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC18b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C18b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C18b.place(x=290, y=160)

    if Corretday == "C19":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC19b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C19b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C19b.place(x=372, y=160)

    if Corretday == "C20":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC20b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C20b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C20b.place(x=433, y=160)

    if Corretday == "C21":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC21b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C21b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C21b.place(x=512, y=160)

    if Corretday == "C22":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC22b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C22b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C22b.place(x=42, y=200)

    if Corretday == "C23":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC23b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C23b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C23b.place(x=115, y=200)

    if Corretday == "C24":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC24b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C24b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C24b.place(x=190, y=200)

    if Corretday == "C25":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC25b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C25b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C25b.place(x=290, y=200)

    if Corretday == "C26":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC26b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C26b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C26b.place(x=372, y=200)

    if Corretday == "C27":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC27b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C27b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C27b.place(x=433, y=200)

    if Corretday == "C28":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC28b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C28b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C28b.place(x=512, y=200)

    if Corretday == "C29":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC29b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C29b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C29b.place(x=42, y=240)

    if Corretday == "C30":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC30b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C30b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C30b.place(x=115, y=240)

    if Corretday == "C31":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC31b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C31b = tk.Label(Calender, text=f" 2 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C31b.place(x=190, y=240)


def RateThree():
    Needmonth = str(datetime.date.today().month)
    month_num = Needmonth
    datetime_object = datetime.datetime.strptime(month_num, "%m")
    full_month_name = datetime_object.strftime("%B")

    if full_month_name == "September":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "October":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "November":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    elif full_month_name == "December":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "January":
        dayint = (datetime.date.today().day)
        dayint = dayint + 5
        daystr = str(dayint)

    elif full_month_name == "February":
        dayint = (datetime.date.today().day)
        dayint = dayint + 1
        daystr = str(dayint)

    elif full_month_name == "March":
        dayint = (datetime.date.today().day)
        dayint = dayint + 1
        daystr = str(dayint)

    elif full_month_name == "April":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "May":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    elif full_month_name == "June":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "July":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "August":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    else:
        print("error")
        quit()

    Corretday = ("C" + daystr)

    if Corretday == "C1":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC1b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C1b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C1b.place(x=42, y=80)

    if Corretday == "C2":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC2b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C2b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C2b.place(x=115, y=80)

    if Corretday == "C3":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC3b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C3b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C3b.place(x=190, y=80)

    if Corretday == "C4":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC4b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C4b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C4b.place(x=290, y=80)

    if Corretday == "C5":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC5b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C5b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C5b.place(x=372, y=80)

    if Corretday == "C6":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC6b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C6b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C6b.place(x=433, y=80)

    if Corretday == "C7":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC7b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C7b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C7b.place(x=512, y=80)

    if Corretday == "C8":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC8b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C8b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C8b.place(x=42, y=120)

    if Corretday == "C9":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC9b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C9b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C9b.place(x=115, y=120)

    if Corretday == "C10":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC10b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C10b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C10b.place(x=512, y=160)

    if Corretday == "C11":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC11b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C11b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C11b.place(x=290, y=120)

    if Corretday == "C12":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC12b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C12b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C12b.place(x=372, y=120)

    if Corretday == "C13":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC13b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C13b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C13b.place(x=433, y=120)

    if Corretday == "C14":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC14b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C14b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C14b.place(x=512, y=120)

    if Corretday == "C15":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC15b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C15b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C15b.place(x=42, y=160)

    if Corretday == "C16":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC16b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C16b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C16b.place(x=115, y=160)

    if Corretday == "C17":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC17b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C17b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C17b.place(x=190, y=160)

    if Corretday == "C18":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC18b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C18b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C18b.place(x=290, y=160)

    if Corretday == "C19":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC19b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C19b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C19b.place(x=372, y=160)

    if Corretday == "C20":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC20b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C20b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C20b.place(x=433, y=160)

    if Corretday == "C21":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC21b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C21b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C21b.place(x=512, y=160)

    if Corretday == "C22":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC22b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C22b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C22b.place(x=42, y=200)

    if Corretday == "C23":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC23b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C23b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C23b.place(x=115, y=200)

    if Corretday == "C24":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC24b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C24b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C24b.place(x=190, y=200)

    if Corretday == "C25":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC25b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C25b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C25b.place(x=290, y=200)

    if Corretday == "C26":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC26b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C26b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C26b.place(x=372, y=200)

    if Corretday == "C27":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC27b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C27b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C27b.place(x=433, y=200)

    if Corretday == "C28":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC28b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C28b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C28b.place(x=512, y=200)

    if Corretday == "C29":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC29b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C29b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C29b.place(x=42, y=240)

    if Corretday == "C30":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC30b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C30b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C30b.place(x=115, y=240)

    if Corretday == "C31":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC31b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C31b = tk.Label(Calender, text=f" 3 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C31b.place(x=190, y=240)


def RateFour():
    Needmonth = str(datetime.date.today().month)
    month_num = Needmonth
    datetime_object = datetime.datetime.strptime(month_num, "%m")
    full_month_name = datetime_object.strftime("%B")

    if full_month_name == "September":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "October":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "November":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    elif full_month_name == "December":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "January":
        dayint = (datetime.date.today().day)
        dayint = dayint + 5
        daystr = str(dayint)

    elif full_month_name == "February":
        dayint = (datetime.date.today().day)
        dayint = dayint + 1
        daystr = str(dayint)

    elif full_month_name == "March":
        dayint = (datetime.date.today().day)
        dayint = dayint + 1
        daystr = str(dayint)

    elif full_month_name == "April":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "May":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    elif full_month_name == "June":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "July":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "August":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    else:
        print("error")
        quit()

    Corretday = ("C" + daystr)

    if Corretday == "C1":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC1b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C1b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C1b.place(x=42, y=80)

    if Corretday == "C2":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC2b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C2b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C2b.place(x=115, y=80)

    if Corretday == "C3":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC3b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C3b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C3b.place(x=190, y=80)

    if Corretday == "C4":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC4b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C4b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C4b.place(x=290, y=80)

    if Corretday == "C5":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC5b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C5b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C5b.place(x=372, y=80)

    if Corretday == "C6":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC6b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C6b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C6b.place(x=433, y=80)

    if Corretday == "C7":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC7b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C7b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C7b.place(x=512, y=80)

    if Corretday == "C8":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC8b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C8b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C8b.place(x=42, y=120)

    if Corretday == "C9":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC9b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C9b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C9b.place(x=115, y=120)

    if Corretday == "C10":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC10b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C10b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C10b.place(x=512, y=160)

    if Corretday == "C11":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC11b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C11b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C11b.place(x=290, y=120)

    if Corretday == "C12":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC12b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C12b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C12b.place(x=372, y=120)

    if Corretday == "C13":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC13b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C13b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C13b.place(x=433, y=120)

    if Corretday == "C14":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC14b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C14b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C14b.place(x=512, y=120)

    if Corretday == "C15":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC15b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C15b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C15b.place(x=42, y=160)

    if Corretday == "C16":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC16b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C16b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C16b.place(x=115, y=160)

    if Corretday == "C17":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC17b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C17b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C17b.place(x=190, y=160)

    if Corretday == "C18":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC18b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C18b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C18b.place(x=290, y=160)

    if Corretday == "C19":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC19b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C19b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C19b.place(x=372, y=160)

    if Corretday == "C20":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC20b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C20b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C20b.place(x=433, y=160)

    if Corretday == "C21":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC21b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C21b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C21b.place(x=512, y=160)

    if Corretday == "C22":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC22b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C22b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C22b.place(x=42, y=200)

    if Corretday == "C23":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC23b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C23b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C23b.place(x=115, y=200)

    if Corretday == "C24":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC24b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C24b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C24b.place(x=190, y=200)

    if Corretday == "C25":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC25b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C25b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C25b.place(x=290, y=200)

    if Corretday == "C26":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC26b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C26b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C26b.place(x=372, y=200)

    if Corretday == "C27":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC27b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C27b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C27b.place(x=433, y=200)

    if Corretday == "C28":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC28b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C28b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C28b.place(x=512, y=200)

    if Corretday == "C29":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC29b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C29b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C29b.place(x=42, y=240)

    if Corretday == "C30":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC30b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C30b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C30b.place(x=115, y=240)

    if Corretday == "C31":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC31b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C31b = tk.Label(Calender, text=f" 4 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C31b.place(x=190, y=240)


def RateFive():
    Needmonth = str(datetime.date.today().month)
    month_num = Needmonth
    datetime_object = datetime.datetime.strptime(month_num, "%m")
    full_month_name = datetime_object.strftime("%B")

    if full_month_name == "September":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "October":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "November":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    elif full_month_name == "December":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "January":
        dayint = (datetime.date.today().day)
        dayint = dayint + 5
        daystr = str(dayint)

    elif full_month_name == "February":
        dayint = (datetime.date.today().day)
        dayint = dayint + 1
        daystr = str(dayint)

    elif full_month_name == "March":
        dayint = (datetime.date.today().day)
        dayint = dayint + 1
        daystr = str(dayint)

    elif full_month_name == "April":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "May":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    elif full_month_name == "June":
        dayint = (datetime.date.today().day)
        dayint = dayint + 2
        daystr = str(dayint)

    elif full_month_name == "July":
        dayint = (datetime.date.today().day)
        dayint = dayint + 4
        daystr = str(dayint)

    elif full_month_name == "August":
        dayint = (datetime.date.today().day)
        dayint = dayint + 0  # Need testing
        daystr = str(dayint)

    else:
        print("error")
        quit()

    Corretday = ("C" + daystr)

    if Corretday == "C1":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC1b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C1b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C1b.place(x=42, y=80)

    if Corretday == "C2":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC2b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C2b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C2b.place(x=115, y=80)

    if Corretday == "C3":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC3b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C3b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C3b.place(x=190, y=80)

    if Corretday == "C4":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC4b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C4b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C4b.place(x=290, y=80)

    if Corretday == "C5":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC5b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C5b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C5b.place(x=372, y=80)

    if Corretday == "C6":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC6b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C6b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C6b.place(x=433, y=80)

    if Corretday == "C7":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC7b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C7b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C7b.place(x=512, y=80)

    if Corretday == "C8":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC8b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C8b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C8b.place(x=42, y=120)

    if Corretday == "C9":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC9b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C9b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C9b.place(x=115, y=120)

    if Corretday == "C10":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC10b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C10b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C10b.place(x=512, y=160)

    if Corretday == "C11":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC11b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C11b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C11b.place(x=290, y=120)

    if Corretday == "C12":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC12b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C12b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C12b.place(x=372, y=120)

    if Corretday == "C13":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC13b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C13b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C13b.place(x=433, y=120)

    if Corretday == "C14":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC14b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C14b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C14b.place(x=512, y=120)

    if Corretday == "C15":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC15b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C15b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C15b.place(x=42, y=160)

    if Corretday == "C16":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC16b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C16b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C16b.place(x=115, y=160)

    if Corretday == "C17":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC17b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C17b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C17b.place(x=190, y=160)

    if Corretday == "C18":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC18b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C18b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C18b.place(x=290, y=160)

    if Corretday == "C19":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC19b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C19b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C19b.place(x=372, y=160)

    if Corretday == "C20":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC20b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C20b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C20b.place(x=433, y=160)

    if Corretday == "C21":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC21b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C21b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C21b.place(x=512, y=160)

    if Corretday == "C22":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC22b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C22b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C22b.place(x=42, y=200)

    if Corretday == "C23":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC23b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C23b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C23b.place(x=115, y=200)

    if Corretday == "C24":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC24b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C24b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C24b.place(x=190, y=200)

    if Corretday == "C25":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC25b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C25b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C25b.place(x=290, y=200)

    if Corretday == "C26":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC26b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C26b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C26b.place(x=372, y=200)

    if Corretday == "C27":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC27b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C27b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C27b.place(x=433, y=200)

    if Corretday == "C28":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC28b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C28b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C28b.place(x=512, y=200)

    if Corretday == "C29":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC29b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C29b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C29b.place(x=42, y=240)

    if Corretday == "C30":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC30b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C30b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C30b.place(x=115, y=240)

    if Corretday == "C31":
        f = open("Saved_input.txt", "a")
        f.write(
            f"""\nC31b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2,relief="groove")""")
        f.close()
        C31b = tk.Label(Calender, text=f" 5 ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
        C31b.place(x=190, y=240)


Ratedaypage_btn1 = tk.Button(Ratedaypage, text="1", width=5, height=2,
                             command=lambda: [RateOne(), show_frame(Whatmadeufeel), Changesize()])
Ratedaypage_btn1.place(x=60, y=40)

Ratedaypage_btn2 = tk.Button(Ratedaypage, text="2", width=5, height=2,
                             command=lambda: [RateTwo(), show_frame(Whatmadeufeel), Changesize()])
Ratedaypage_btn2.place(x=105, y=40)

Ratedaypage_btn3 = tk.Button(Ratedaypage, text="3", width=5, height=2,
                             command=lambda: [RateThree(), show_frame(Whatmadeufeel), Changesize()])
Ratedaypage_btn3.place(x=150, y=40)

Ratedaypage_btn4 = tk.Button(Ratedaypage, text="4", width=5, height=2,
                             command=lambda: [RateFour(), show_frame(Whatmadeufeel), Changesize()])
Ratedaypage_btn4.place(x=195, y=40)

Ratedaypage_btn5 = tk.Button(Ratedaypage, text="5", width=5, height=2,
                             command=lambda: [RateFive(), show_frame(Whatmadeufeel), Changesize()])
Ratedaypage_btn5.place(x=240, y=40)

# ==================Frame 3 code

Whatmadeufeel_title = tk.Label(Whatmadeufeel, text='What made you feel \n this way?', font='times 15', bg='light blue')
Whatmadeufeel_title.pack()

# CONFIGURE
Whatmadeufeel.configure(bg='light blue')

# Buttons
wmuf_btn_Family = tk.Button(Whatmadeufeel, text="Family", width=10, height=2,
                            command=lambda: [(wmuf_btn_Family.config(relief=SUNKEN))])
wmuf_btn_Family.place(x=120, y=60)

wmuf_btn_Stress = tk.Button(Whatmadeufeel, text="Stress", width=10, height=2,
                            command=lambda: [(wmuf_btn_Stress.config(relief=SUNKEN))])
wmuf_btn_Stress.place(x=210, y=60)

wmuf_btn_People = tk.Button(Whatmadeufeel, text="People", width=10, height=2,
                            command=lambda: [(wmuf_btn_People.config(relief=SUNKEN))])
wmuf_btn_People.place(x=300, y=60)

wmuf_btn_Emotions = tk.Button(Whatmadeufeel, text="Emotions", width=10, height=2,
                              command=lambda: [(wmuf_btn_Emotions.config(relief=SUNKEN))])
wmuf_btn_Emotions.place(x=390, y=60)

wmuf_btn_Pain = tk.Button(Whatmadeufeel, text="Pain", width=10, height=2,
                          command=lambda: [(wmuf_btn_Pain.config(relief=SUNKEN))])
wmuf_btn_Pain.place(x=120, y=112)

wmuf_btn_Work = tk.Button(Whatmadeufeel, text="Work", width=10, height=2,
                          command=lambda: [(wmuf_btn_Work.config(relief=SUNKEN))])
wmuf_btn_Work.place(x=210, y=112)

wmuf_btn_Society = tk.Button(Whatmadeufeel, text="Society", width=10, height=2,
                             command=lambda: [(wmuf_btn_Society.config(relief=SUNKEN))])
wmuf_btn_Society.place(x=300, y=112)

wmuf_btn_School = tk.Button(Whatmadeufeel, text="School", width=10, height=2,
                            command=lambda: [(wmuf_btn_School.config(relief=SUNKEN))])
wmuf_btn_School.place(x=390, y=112)

wmuf_btn_Online = tk.Button(Whatmadeufeel, text="Online", width=10, height=2,
                            command=lambda: [(wmuf_btn_Online.config(relief=SUNKEN))])
wmuf_btn_Online.place(x=120, y=164)

wmuf_btn_Love = tk.Button(Whatmadeufeel, text="Love", width=10, height=2,
                          command=lambda: [(wmuf_btn_Love.config(relief=SUNKEN))])
wmuf_btn_Love.place(x=210, y=164)

wmuf_btn_Overwhelmed = tk.Button(Whatmadeufeel, text="Overwhelmed", width=10, height=2,
                                 command=lambda: [(wmuf_btn_Overwhelmed.config(relief=SUNKEN))])
wmuf_btn_Overwhelmed.place(x=300, y=164)

wmuf_btn_Depressed = tk.Button(Whatmadeufeel, text="Depressed", width=10, height=2,
                               command=lambda: [(wmuf_btn_Depressed.config(relief=SUNKEN))])
wmuf_btn_Depressed.place(x=390, y=164)

wmuf_btn_Continue = tk.Button(Whatmadeufeel, text="Continue", width=10, height=2,
                              command=lambda: [Saved_inputs(), calculateMusic(), show_frame(Calender), Changesize_C()])
wmuf_btn_Continue.place(x=480, y=230)

# ==================Frame 4 code
Calender_title = tk.Label(Calender, text='Calendar', font='times 25', bg='light blue')

# CONFIGURE
Calender.configure(bg='light blue')

# Day's of the week

Monday_C = tk.Label(Calender, text="Monday", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Tuesday_C = tk.Label(Calender, text="Tuesday", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Wednesday_C = tk.Label(Calender, text="Wednesday", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Thursday_C = tk.Label(Calender, text="Thursday", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Friday_C = tk.Label(Calender, text="Friday", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Saturday_C = tk.Label(Calender, text="Saturday", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Sunday_C = tk.Label(Calender, text="Sunday", font="times 15", bg='light blue', borderwidth=2, relief="groove")

Calender_title.pack()

# Day Placements

Monday_C.place(x=42, y=40)
Tuesday_C.place(x=115, y=40)
Wednesday_C.place(x=190, y=40)
Thursday_C.place(x=290, y=40)
Friday_C.place(x=372, y=40)
Saturday_C.place(x=433, y=40)
Sunday_C.place(x=512, y=40)

# Save Old recored data EX: how was your day June 19 = 2
# Save Old recored data EX: how was your day June 19 = 2
# Save Old recored data EX: how was your day June 19 = 2

# Left off

# Last thing to do before testing & finally polish


# 31 days
C1 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C2 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C3 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C4 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C5 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C6 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C7 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C8 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C9 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C10 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C11 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C12 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C13 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C14 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C15 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C16 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C17 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C18 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C19 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C20 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C21 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C22 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C23 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C24 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C25 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C26 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C27 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C28 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C29 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C30 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
C31 = tk.Label(Calender, text=f"  ", font="times 15", bg='light blue', borderwidth=2, relief="groove")

# Months Placements

C1.place(x=42, y=80)
C2.place(x=115, y=80)
C3.place(x=190, y=80)
C4.place(x=290, y=80)
C5.place(x=372, y=80)
C6.place(x=433, y=80)
C7.place(x=512, y=80)

C8.place(x=42, y=120)
C9.place(x=115, y=120)
C10.place(x=190, y=120)
C11.place(x=290, y=120)
C12.place(x=372, y=120)
C13.place(x=433, y=120)
C14.place(x=512, y=120)

C15.place(x=42, y=160)
C16.place(x=115, y=160)
C17.place(x=190, y=160)
C18.place(x=290, y=160)
C19.place(x=372, y=160)
C20.place(x=433, y=160)
C21.place(x=512, y=160)

C22.place(x=42, y=200)
C23.place(x=115, y=200)
C24.place(x=190, y=200)
C25.place(x=290, y=200)
C26.place(x=372, y=200)
C27.place(x=433, y=200)
C28.place(x=512, y=200)

C29.place(x=42, y=240)
C30.place(x=115, y=240)
C31.place(x=190, y=240)

# recommend music
music = tk.Label(Calender, text=f"Music: ", font="times 15", bg='light blue', borderwidth=2, relief="groove")
music.place(x=20, y=300)

# AI
AI_C_btn = tk.Button(Calender, text="Chat bot", width=10, height=2, command=lambda: ())
AI_C_btn.place(x=20, y=340)

# Close Program
Close = tk.Button(Calender, text="Close", width=10, height=2, command=lambda: (close()))
Close.place(x=500, y=340)

# Reset Function
Reset = tk.Button(Calender, text="Reset", width=10, height=2, command=lambda: (reset()))
Reset.place(x=500, y=285)


f = open("profileCo.txt", "r")
profileCount = (f.readline())


def startMain():
    Secturty()
    show_frame(Mainpage)


def startProfile():
    Secturty()
    show_frame(Profile)
    win.geometry('300x400')


if profileCount == "profileCount = 1":
    Secturty()
    startMain()
else:
    Secturty()
    startProfile()

win.mainloop()