from tkinter import *
import random

root=Tk()
root.title("ruleta_aleatoria_numeros")
root.geometry("500x500")
root.configure(background= "#05a3ff")


random_number_list = Label(root)
random_number_sorted_list = Label(root)

def random_list():
    randomlist = random.sample(range(1,30),7)
    random_number_list["text"] = "lista aleatoria:" + str(randomlist)
    randomlist.sort()
    random_number_sorted_list["text"] = "lista ordenada aleatoria:" + str(randomlist)

btn = Button(root,text="generar lista aleatoria", command= random_list, bg= "#ff0d0d", radio= "")
btn.place(relx=0.5, rely=0.4, anchor=CENTER,  )

random_number_list.place(relx=0.5, rely=0.5, anchor=CENTER,  )

random_number_sorted_list.place(relx=0.5, rely=0.6, anchor=CENTER,  )





mainloop()



