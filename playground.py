from Tkinter import * #gives us access to everything in the Tkinter class
import tkMessageBox
from PIL import Image, ImageTk
from datetime import datetime


def buttonpress1():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("Here's what you typed", entrytxt)

def addtoList():
    entrytxt = entry1.get()
    if check4Dup() == False:
        listbox1.insert(END, entrytxt)
        findsize()
    entry1.delete(0,END)
    
def addtoList2(event):
    entrytxt = entry1.get()
    if check4Dup() == False:
        listbox1.insert(END, entrytxt)
        findsize()
    entry1.delete(0,END) #deletes text after you push enter

def clearList(event):
    listbox1.delete(0, END)
    findsize()
    
def clearList2():
    listbox1.delete(0, END)
    findsize()

def check4Dup():
    names = listbox1.get(0, END)
    if entry1.get() in names:
        return True
    else:
        return False
        
def findsize():
    label1.config(text=listbox1.size())
    
def openfileR():
    clearList2()
    f=open("ReadMe.txt", 'r')
    for line in f:
        name=line[0:-1]
        listbox1.insert(END, name)
    
    f.close()
    findsize()

def openfileW():
    f = open("ReadMe.txt", 'w')
    names = listbox1.get(0, END)
    for i in names:
        f.write(i+"\n")
               
    f.close()



d=datetime.now()
print d
y=d.year
print y
h=d.hour
print h



root = Tk() #gives us a blank canvas object to work with
root.title("My first GUI program with Tkinter")

button1 = Button(root, text="Pop Up", bg="light grey", command=buttonpress1)
button1.grid(row=2, column=2)

button2 = Button(root, text="Check for Duplicate", bg="light grey", command=check4Dup)
button2.grid(row=2, column=0)

addtoList = Button(root, text="Add to List", bg="light grey", command=addtoList)
addtoList.grid(row=2, column=1)

entry1 = Entry(root, bg="seashell")
entry1.grid(row=1,column=0)
entry1.bind("<Return>", addtoList2)

label1 = Label(root, text="Hello World", bg="lavender", anchor=W)
label1.grid(row=0, column=0, sticky=EW, columnspan=3)

scrollbar = Scrollbar(root, orient=VERTICAL)
listbox1 = Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox1.yview)
scrollbar.grid(row=3, column=2, rowspan=10, sticky=NS)
listbox1.grid(row=3, column=0, columnspan=2, sticky=EW, rowspan = 10)
listbox1.bind("<Button-3>", clearList)

#listbox1.insert(END, "Bob")
#listbox1.insert(END, "John")
#listbox1.insert(END, "Mary")

label1.config(text= listbox1.size())

findsize()

image = Image.open("ball.jpg") #make sure you're in the right folder ->
image = image.resize((100, 100))
photo = ImageTk.PhotoImage(image)

labe2 = Label(image=photo)
labe2.image = photo # keep a reference!
labe2.grid(row=7, column=1)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Save", command=openfileW)

menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

mainloop() #causes the windows to display on the screen until program closes













