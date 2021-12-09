#!/usr/bin/env python3
import socket
import re
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

HOST = '192.168.1.210'  # The server's hostname or IP address
PORT = 8001  # The port used by the server
IMAGEPATH = dir_path + '/images/'
VIDEOPATH = '/share/VPiBackglass/videos/'
START=TRUE

print('starting')
tableRegex = re.compile(r'with ROM=\'(\w+)\'')
root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
# root.geometry("200x200")
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
canvas = tkinter.Canvas(root, width=w, height=h)
canvas.pack()
canvas.configure(background='black')

l = Label()
l.pack()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def main():
    global s
    global l
    global img
    global canvas
    global START
    if START:
        START = FALSE
        img = ImageTk.PhotoImage(Image.open(IMAGEPATH + "PinballFX3.png"))
        canvas.create_image(w/2, h/2, image=img)

    data = s.recv(1024)
    match = tableRegex.search(repr(data))
    if (match != None):
        tableName = match.group(1)
        print(tableName)
        try:
            img = ImageTk.PhotoImage(Image.open(
                IMAGEPATH + tableName + ".png"))
            canvas.create_image(w/2, h/2, image=img)
        except:
            print("table nog found")

    root.after(500, main)

main()
root.mainloop()
