from tkinter import *

root=Tk()


#have two windows open at start
#label = Label(top, text="Hello World!")
#label.pack()


#creates another windows with button click top.destroy button will close the second window
def open():
    top = Toplevel()
    label=Label(top,text="Hello World!")
    label.pack()
    btn2= Button(top, text="close window", command=top.destroy)
    btn2.pack()


b=Button(root, text="open second window",command=open)
b.pack()



root.mainloop()
