from tkinter import*

root = Tk()
root.configure(bg = "#7df59d")
root.geometry("400x400")
root.title("enfermedades")

btn1 = StringVar(value = "0")

label1 = Label(root,text="tienes dolor de cabeza o dolor de garganta?",bg="#7df59d")
label1.pack()

btn1_si = Radiobutton(root,text="si",variable=btn1,value="si",bg="#7df59d")
btn1_si.pack()

btn1_no = Radiobutton(root,text="no",variable=btn1,value="no",bg="#7df59d")
btn1_no.pack()

btn2 = StringVar(value = "0")

label2 = Label(root,text="tienes temperatura corporal alta?",bg="#7df59d")
label2.pack()

btn2_si = Radiobutton(root,text="si",variable=btn1,value="si",bg="#7df59d") 
btn2_si.pack()

btn2_no = Radiobutton(root,text="no",variable=btn1,value="no",bg="#7df59d")
btn2_no.pack()


btn3 = StringVar(value = "0")

label3 = Label(root,text="tienes algun sintoma de enrojesimiento en los ojos?",bg="#7df59d")
label3.pack()

btn3_si = Radiobutton(root,text="si",variable=btn1,value="si",bg="#7df59d")
btn3_si.pack()

btn3_no = Radiobutton(root,text="no",variable=btn1,value="no",bg="#7df59d")
btn3_no.pack()


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
    if score <=20:
        messagebox.showinfo("reporte","no es necesario que tengas que ir al doctor")
    elif score >20 and score <=40:
        messagebox.showinfo("reporte","es posible que tengas que ir al doctor")
    else :
        messagebox.showinfo("reporte","necesitas o recomienda ir al doctor")
    
        
        
btn_original = Button(root,text="has clic aqui para saber si esta bien o mal :( ",command=fever_score)
wbtn_original.pack()    

root.mainloop()

