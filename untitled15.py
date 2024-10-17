from tkinter import*
from tkinter import ttk

root = Tk()
root.title("lienzo")
root.geometry("600x600")

etiquetas = ["boton","etiqueta","menu despegable"]

list_1 = ttk.Combobox(root, state="readonly",values= etiquetas)
list_1.pack()


class createElements():
    def __int__(self,):
        print("esta es la clase createElments")
    def createlabel(self) :
        label = Label(root,text="se a creado una nueva etiqueta",fg="green")
        label.pack()
    def creteButton(self):
        btn = Button(root,text="boton",fg="red",comand= self.message)
        brn.pack(padx,pady)
    def createdrowbok(self):
        valores = ["1","2","3"]
        list_2 = ttk.Combobox(root,state="readonly",values=valores)
        list_2.pack()
    def chose(self):
        
        
    


root.mainloop()