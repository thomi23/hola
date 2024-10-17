from tkinter import *

root= Tk()
root.title("matrices multidimencinales")
root.geometry("500x500")

label = Label(root)

array_1d = ["daniel","sara","martin"]
print(array_1d[0])
array_2d = [["daniel","a"],["sara","b"],["martin","c"]]
print(array_2d[2][1])
array_3d = [[["daniel","a","exelente"],["sara","b","muy bueno"],["martin","c","bueno"]]]
print(array_3d[0][2][2])

def matrises():
    label["text"] = array_3d[0][1][0] + " obtuvo la calificacion de " + array_3d[0][1][1] + " y le fue " + array_3d[0][1][2]


btn = Button(root, text="mostrar reporte", command = matrises)
btn.place(relx=0.5,rely=0.5, anchor=CENTER)    
label.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()