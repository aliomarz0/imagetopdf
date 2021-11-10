import os
import os.path
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilenames
import img2pdf
from tkinter.font import Font
filename = "loaypdf"
def select_imgs():
    global file_names
    file_names = askopenfilenames(initialdir="/",title="Select Images")
def images2pdf_():
    directorypath = filedialog.askdirectory()
    filepath = os.path.join(directorypath, hotname)
    with open(f"{filepath}.pdf","wb") as file:
        file.write(img2pdf.convert(file_names))
def pdf_name():
    global hotname
    hotname = name1.get()
    donelabel = Label(window,text="Name of PDF File was set!",bg='#FFD53D')
    name1.delete(0,'end')
    donelabel.pack()

window = tk.Tk()
window.title("Mr Loay PDF Converter")
window.configure(bg='#FFD53D')
window.geometry('400x600')
window.iconbitmap('C:/Users/ali/PycharmProjects/PythonProject3/math.ico')
Label(window,text="Mr Loay PDF Convertor", font="italic 15 bold",bg='#FFD53D').pack(pady=10)
font = Font()



tk.Button(window,font="Helvetica 15 ",text="1. Select Images", bg='#40B0DF', width = 29,height = 3,relief = "solid",command = lambda: select_imgs()).pack(pady=20)
tk.Button(window,font="Helvetica 11 ",text = "2.What do you want to save the PDF file name as?",bg='#40B0DF',relief = "solid", width = 37,height = 4, command=lambda: pdf_name()).pack(pady=20)
name1 = Entry(window, width=30, relief="solid",font=('italic',15))
name1.pack()

tk.Button(window,font="Helvetica 15 ",text="3. Convert Images to PDF",bg='#40B0DF',relief = "solid", width = 29,height = 3,command=lambda: images2pdf_()).pack(pady=20)

Label(window,text="Please do the following in the specified order. ", font="italic 10 bold",bg='#FFD53D').pack(pady=10)
Label(window,text=" You must do Button Number 1, then 2 and 3 for it to work",font="italic 10 bold",bg='#FFD53D').pack(pady=10)
window.mainloop()
