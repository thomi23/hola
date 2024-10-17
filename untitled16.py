from tkinter import*
from tkinter import filedialog
from PIL import ImageTk,Image
root = Tk()
root.title("lienzo")
root.geometry("600x600")

img =  ImageTk.PhotoImage()(Image.open(img_path)) 

image = Label(root,highlightthickness=0.6,bg=green)
image.place(relx=0.5,rely=0.5,anchor=CENTER)

def abrir_image():
    global name
    img_path = filedialog.askopenfilename(title= "abrrir archivo de texto", filetypes=[("archivo de imagen","*.jpg *.gif *.png *.jpeg")])
    image["image"] = img
    img.close()
    
    
    
btn = Button(root,text="abrir image",command=abrir_image)
btn.place(relx=0.5,rely=0.95,anchor=CENTER)    

root.mainloop()
