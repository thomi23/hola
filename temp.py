from tkinter import *

#Descomenta la sigueinte línea si tienes MacOS.
#Pide al alumno que escriba la siguiente línea si el alumno tiene MacOS.

#from tkmacosx import *

root=Tk()
root.title("pou")

root.geometry("600x600")
root.configure(background = '#a0ff47')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text = "Nombre en ASCII: ", bg="#0565f5", fg="black")

def asciiConverter():
    input_word = enter_word.get()

    for letter in input_word :
        label["text"] += str(ord(letter)) + "  "
        
btn=Button(root,text="Muestra el nombre en ASCII",command=asciiConverter, bg='#fa0000', fg = 'black')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()
