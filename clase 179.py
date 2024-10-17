from tkinter import * 
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.geometry("800x600")
root.title("encapsulacion 2.0")
root.configure(bg="orange2")

label_heasding = Label(root, text="tienda de juegos",bg="orange2", font=("Sylfaen",18,"bold","italic"))
label_heasding.place(relx = 0.05,rely = 0.1, anchor= W)

juice = ImageTk.PhotoImage(Image.open ("logo .png"))
juice_image = Label(root, image=juice, bg = "orange2")
juice_image.place(relx=0.2,rely = 0.4,anchor=CENTER)

apple = ImageTk.PhotoImage(Image.open (" apple_img.png"))
mango = ImageTk.PhotoImage(Image.open (" mango_img.png"))
orange = ImageTk.PhotoImage(Image.open (" orange_img.png"))

fruit_image = Label(root, bg="orange2")
fruit_image.place(relx = 0.8, rely=0.8,anchor=CENTER)

label_name = label(rootl, text="seleciona la fruta",bg="orqange2",font=("bahnschrift Light",15))
label_name.place(relx=0.96,rely=0.2,anchor=E)

fruit_list = ["manzana","mango","naranja"]
fruit_combobox = ttk.Combobox(root,state= "readonly", values=fruit_list, justify="right")
fruit_combobox.place(relx=0.95,rely=0.25,anchor=E)

label_quantity = Label(root,text="ingresa la cantidad",bg="orange2", font=("bahnschrift Light",15))
label_quantity.place(relx=0.96,rey=0.35,anchor= E)

input_quantity = Entry(root)
input_quantity.place(relx=0.95,rely=0.8, anchor=E)

label_show_ammount = Label(root,bg="orange2", font=("bahnschrift Light",15))
label_show_ammount.place(relx=0.95,rely=0.7,anchor=E)

label_show_quantity = Label(root,bg="orange2", font=("bahnschrift Light",15))
label_show_quantity.place(relx=0.95,rely=0.8,anchor=E)

class juice:
     def __init__(self,fruit_name,quantity):
         self.fruit = fruit_name
         self.quantity = int(quantity)
         self.__cost = 250
     
     def __calculatecost(self):
         total_cost = self.quantity * self.__cost
         label_show_ammount["text"] = "cantidad a pagar es : " + str(total_cost) + " USD"
         if (self.fruit == "Manzana"):
             calorias = (self.quantity * 52)/100
             fruit_image['image'] = apple
         elif (self.fruit == "durazno"):
              calorias = (self.quantity * 60)/100
              fruit_image['image'] = mango
         elif (self.fruit == "naranja"):
              calorias = (self.quantity * 47)/100
              fruit_image['image'] = orange
              label_show_quantity["text"] = "x"+ str(self.quantity) + " = " + str(calorias)
        
     def getcost(self):
         self.__calculatecost()
         
         
def ordenjuice():
     fruit = fruit_combobox.get()
     quantity = input_quantity.get()
     obj1 = juice(fruit, quantity)
     obj1.getcost()
      
btn = Button(root, text = "total",bg="red", fg="blue",padx=10,pady=1, font=("Arial",11,"bold"), relief=FLAT, command=ordenjuice)
btn.place(relx=0.95,rely=0.5, anchor = E)

root.mainloop()