class doctor:
      def __init__(self):
          print("esta es la clase doctor")
      def masa_Corporal(peso,altura):
       result = peso /( altura * altura)
       print("la masa corporal del indivuduo es de: "+str(result))
      def frecuencia_cardiaca1(frecuencia_cardiaca2):
           if (frecuencia_cardiaca2>60 and frecuencia_cardiaca2<100):
               print("estas bien")
           else:
               print("no estas bien")
               
class patience(doctor):
      
    def __init__(self,name,fecha_de_nacimiento,peso,altura,frecuencia_cardiaca):
          self.name_pacient = name
          self.fecha_de_nacimiento_pacient = fecha_de_nacimiento
          self.peso_pacient = peso
          self.altura_pacient = altura
          self.frecuencia_cardiaca_pacient = frecuencia_cardiaca
          

    def informe_Salud(self):
       print("nombre del paciente: "+self.name_pacient)
       doctor.masa_Corporal(self.peso_pacient, self.altura_pacient)
       doctor.frecuencia_cardiaca1(self.frecuencia_cardiaca_pacient)
       
pacient1 = patience("juan", 1999, 5, 2, 66)
pacient1.informe_Salud()

pacint2 = patience("migel", 2004, 100, 1, 70) 
pacint2.informe_Salud()      
      
      