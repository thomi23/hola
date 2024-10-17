from tkinter import*

root = Tk()
root.configure(bg = "#7df59d")
root.geometry("400x400")
root.title("enfermedades")

btn1 = StringVar(value = "0")

label1 = Label(root,text="experimenta dificultades para respirar en sus actividades cotidianas",bg="#7df59d")
label1.pack()

btn1_si = Radiobutton(root,text="si",variable=btn1,value="si",bg="#7df59d")
btn1_si.pack()

btn1_no = Radiobutton(root,text="no",variable=btn1,value="no",bg="#7df59d")
btn1_no.pack()

btn2 = StringVar(value = "0")

label2 = Label(root,text="presenta inchason en el abdomen o pies?",bg="#7df59d")
label2.pack()

btn2_si = Radiobutton(root,text="si",variable=btn1,value="si",bg="#7df59d") 
btn2_si.pack()

btn2_no = Radiobutton(root,text="no",variable=btn1,value="no",bg="#7df59d")
btn2_no.pack()


btn3 = StringVar(value = "0")

label3 = Label(root,text="presenta sintomas de perdida de momoria o mareos?",bg="#7df59d")
label3.pack()

btn3_si = Radiobutton(root,text="si",variable=btn1,value="si",bg="#7df59d")
btn3_si.pack()

btn3_no = Radiobutton(root,text="no",variable=btn1,value="no",bg="#7df59d")
btn3_no.pack()

btn4 = StringVar(value = "0")

label4 = Label(root,text="siente que le falta el aire cuando estas en reposo o acostado?",bg="#7df59d")
label4.pack()

btn4_si = Radiobutton(root,text="si",variable=btn1,value="si",bg="#7df59d")
btn4_si.pack()

btn4_no = Radiobutton(root,text="no",variable=btn1,value="no",bg="#7df59d")
btn4_no.pack()


btn5 = StringVar(value = "0")

label5 = Label(root,text="experimenta una tos con sangre o mocos en garganta producidos por silbidos?",bg="#7df59d")
label5.pack()

btn5_si = Radiobutton(root,text="si",variable=btn1,value="si",bg="#7df59d")
btn5_si.pack()

btn5_no = Radiobutton(root,text="no",variable=btn1,value="no",bg="#7df59d")
btn5_no.pack()


def fever_score():
    score = 0
    if btn1.get()=="si":
        score = score +20
        print(score)
    if btn2.get()=="si":
        score = score +20
        print(score)    
    if btn3.get()=="si":
        score = score +20
        print(score)
    if btn4.get()=="si":
            score = score +20
            print(score)
    if btn5.get()=="si":
        score = score +20
        print(score)        
    if score <=20:
        messagebox.showinfo("reporte","no es necesario que tengas que ir al doctor")
    elif score >20 and score <=80:
        messagebox.showinfo("reporte","es posible que tengas que ir al doctor")
    else :
        messagebox.showinfo("reporte","necesitas o recomienda ir al doctor")
    
        
        
btn_original = Button(root,text="has clic aqui para saber si esta bien o mal :( ",command=fever_score)
btn_original.pack()    

root.mainloop()

