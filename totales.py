from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk

root = Tk()
root.title("totales")
root.geometry("500x500")

class jugos:
    def __init__(self,nombre_de_fruta,cantidad):
        self.fruta = nombre_de_fruta
        self.cantidad = int(cantidad)
        self.__costo = 100
    def __calculator(self):
        total = self.cantidad * self.costo
        print("cantidad a pagar es: " + str(total) + "usd")
        if (self.fruta == "manzana"):
            calorias  = self.cantidad * 75
        elif(self.fruta == "banano"):
            calorias = self.cantidad *31
        elif(self.fruta == "mango"):
            calorias = self.cantidad *65
        print(self.fruta + "tiene estas calorias:"+  str(calorias))    
    def cost(self) :
        self.__caculator()
        
def orden() :
    fruta = "manzana"
    cantidad = 201
    obj_1 = jugos(fruta, cantidad)
    obj_1.cost()
    
btn_total  = Button(root,text="funcionar",command=orden)
btn_total.place(relx=0.95,rely=0.5,anchor=E)


root.mainloop()
     
        
    
        
    