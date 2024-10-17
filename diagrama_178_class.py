from tkinter import * 
from tkinter import ttk

root = Tk()
root.geometry("800x600")
root.title("encapsulacion")

class juice:
    def __init__(self,fruit_name,quantity):
        self.fruit = fruit_name
        self.quantity = int(quantity)
        self.__cost = 250
    
    def __calculatecost(self):
        total_cost = self.quantity * self.__cost
        print("cantidad a pagar es : " + str(total_cost) + " USD")
        if (self.fruit == "Manzana"):
            calorias = self.quantity * 52
        elif (self.fruit == "durazno"):
             calorias = self.quantity * 60
        elif (self.fruit == "naranja"):
             calorias = self.quantity * 47
        print("X " + str(self.quantity) + " = " + str(calorias))
       
    def getcost(self):
        self.__calculatecost()
        
        
def ordenjuice():
    fruit = "durazno"
    quantity = 200
    obj1 = juice(fruit, quantity)
    obj1.getcost()
     
btn = Button(root, text = "total", command=ordenjuice)
btn.place(relx=0.95,rely=0.5, anchor = E) 
       
root.mainloop()             
    