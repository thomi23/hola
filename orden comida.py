
class orden_comida:
    def __init__(self):
        print("clase padre")
    def menu(platillo):
        if platillo == "perro caliente":
            print("puedes añadir mas complementos")
            print("mas salsas","mas queso")
        elif platillo == "pizza":
            print("puedes agrgarle mas complementos")
            print("peperoni extra", "pollo extra")
        else:
            print("perdon no nos queda esa comida elije una sobrante")
    def total(platillo,complementos):
        if platillo == "perro caliente" and complementos == "mas salsas":
           print("la cantidad a pagar es 60.000 ")
        elif platillo == "perro caliente" and complementos == "mas queso":
           print("la cantidad a pagar es 55.000 ")
        elif platillo == "pizza" and complementos == "peperoni extra":
           print("la cantidad a pagar es 80.000 ")
        elif platillo == "pizza" and complementos == "pollo extra":
           print("la cantidad a pagar es 77.000 ")   
        
        
class hija1(orden_comida):
      def __init__(self,platillo):
          self.nuevo_platillo = platillo
      def manu_final(self):
          orden_comida.menu(self.nuevo_platillo)
          

class hila2(orden_comida):
      def __init__(self,platillo,complementos):
          self.nuevo_platillo = platillo
          self.complementos1 = complementos
      def get_final_menu(self):
          orden_comida.total(self.nuevo_platillo, self.complementos1)
          
objet_class1 = hija1("perro caliente")
objet_class1.manu_final()

objet_class2 = hila2("pizza","peperoni extra")
objet_class2.get_final_menu()         