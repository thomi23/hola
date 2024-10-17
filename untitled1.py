from tkinter import *
import random

root=Tk()
root.title("ruleta_aleatoria_nombres")
root.geometry("300x300")
root.configure(background= "white")

list_names = ["juan manuel","mariangel","caicedo","latorre","santiago"]
print (list_names)

def random_number():
    random_num=random.randint(0,4)
    print (random_num)
    random_friends = list_names[random_num]
    print("tu amigo elegido es:" + random_friends)
    
btn1 = Button(root,text = "amigo aleatorio", command=random_number, bg = "#47a7f5", fg = "black")
btn1.place(relx=0.5, rely=0.4, anchor=CENTER)
     

root.mainloop()



