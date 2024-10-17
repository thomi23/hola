from tkinter import*

root = Tk()
root.geometry("500x500")
root.title("grados")

label1 = Label(root,text="")

label2 = Label(root,text="")

label3 = Label(root,text="")

class grade_1():
      def __int__(self,matematicas,lenguaje):
        self.matematicas = matematicas
        self.lenguaje = lenguaje
      def porcentaje(self):
        total_mark = [self.lenguaje,self.matematicas]
        total_mark_x100 = total_mark * 100
        porcentaje_grade1 = total_mark / 200
        label1["text"] = porcentaje_grade1

class grade_2():
      def __int__(self,matematicas,lenguaje,sociales):
          self.matematicas = matematicas
          self.lenguaje = lenguaje
          self.sociales = sociales
      def porcentaje(self):
          total_mark_2 = [self.lenguaje,self.matematicas,self.sociales]
          total_mark_2_x100 = total_mark * 100
          porcentaje_grade2 = total_mark / 300
          label2["text"] = porcentaje_grade2

class grade_3():
      def __int__(self,matematicas,lenguaje,sociales,quimica):
          self.matematicas = matematicas
          self.lenguaje = lenguaje
          self.sociales = sociales
          self.quimica = quimica
      def porcentaje(self):
          total_mark_3 = [self.lenguaje,self.matematicas,self.sociales,self.quimica]
          total_mark_3_x100 = total_mark * 100
          porcentaje_grade3 = total_mark / 400
          label3["text"] = porcentaje_grade3       


objet_grado1= grade_1(40,50)
btn1 = Button(root,text="grado 1",command= porcentaje_grade1)
btn1.place(relx=0.5,rely=0.9,anchor=CENTER)
objet_grado2= grade_2(50,10,70)
btn2 = Button(root,text="grado 2",command= porcentaje_grade2) 
objet_grado3= grade_2(40,20,60,100) 
btn3 = Button(root,text="grado 3",command= porcentaje_grade3)     

root.mainloop() 