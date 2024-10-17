from tkinter import *

root = Tk()
root.geometry("500x500")
root.config(background="#c1e887")
root.title("dictionary")

label_1 = Label(root)
label_2 = Label(root)
label_3 = Label(root)

dictionary = {'aereosol':'Suspensión de partículas diminutas de sólidos o líquidos en el aire u otro gas.','dermico':'Perteneciente o relativo a la dermis y, en general, a la piel o cubierta exterior del animal.','fungi':'reino de los hongos'}

def aereosol():
    label_1["text"] = dictionary["aereosol"]
    
    
def dermico():
    label_2["text"] = dictionary["dermico"]
    
    
    
    
def fungi():
    label_3["text"] = dictionary["fungi"]

btn_1 = Button(root, text="significado de aereosol", command=aereosol)
btn_1.place(relx=0.5,rely=0.3,anchor=CENTER)
    
btn_2 = Button(root, text="significado de dermico", command=dermico)
btn_2.place(relx=0.5,rely=0.5,anchor=CENTER)

btn_3 = Button(root, text="significado de fungi", command=fungi)
btn_3.place(relx=0.5,rely=0.7,anchor=CENTER)

label_1.place(relx=0.5,rely=0.4,anchor=CENTER)

label_2.place(relx=0.5,rely=0.6,anchor=CENTER)

label_3.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()
    