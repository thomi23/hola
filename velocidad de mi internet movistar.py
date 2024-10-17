from tkinter import*
import speedtest
from tkinter import font as tkFont

root = Tk()
root.geometry("500x500")
root.title("verificando mi internet patata")
root.configure(bg="lightgreen")

mi_fuente = tkFont.Font(family='Helvetica', size=28, weight='bold')
mi_fuente2 = tkFont.Font(family='Helvetica', size=15, weight='bold')
mi_fuente3 = tkFont.Font(family='Helvetica', size=8, weight='bold')


title = Label(root,text="verificar internet",font=mi_fuente)
title.place(relx=0.5,rely=0.1,anchor=CENTER)

velocidad = Label(root,text="velocidad de descarga",font=mi_fuente2)
velocidad.place(relx=0.25,rely=0.5,anchor=CENTER)

velocidad2 = Label(root,text="velocidad de carga",font=mi_fuente2)
velocidad2.place(relx=0.75,rely=0.5,anchor=CENTER)

result1 = Label(root,font=mi_fuente3)
result1.place(relx=0.25,rely=0.6,anchor=CENTER)

result2 = Label(root,font=mi_fuente3)
result2.place(relx=0.75,rely=0.6,anchor=CENTER)

def calculador():
    variable = speedtest.Speedtest()
    velocity = round(variable.download()/1000000,2)
    result1["text"] = str(velocity) + "mbps"
    carga = round(variable.upload()/1000000,2)
    result2["text"] = str(carga) + "mbps"
    
btn = Button(root,text="as clik para que funcione",bg="green",command=calculador)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

root.mainloop()    