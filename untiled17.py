class estanteria_de_libros:
    def __init__(self,nombre,autor,precio,fecha_publicacion):
        self.nombre_libro = nombre
        self.precio_libro = precio
        self.fecha_publicacion_libro = fecha_publicacion
        self.autor_libro = autor
    
    def add_book(self):
        print("nombre del libro:"+self.nombre_libro)
        print("autor del libro:"+self.autor_libro)
        print("precio del libro:"+str(self.precio_libro))
        print("fecha de publicascion:"+str(self.fecha_publicacion_libro))
        print("libro añadido")
        
    def año_publicado(self):
        año_publicado1 = 2024 - self.fecha_publicacion_libro
        print("este libro se publico hace:"+str(año_publicado1)+"años")

book = estanteria_de_libros("arbol", "arbol estiven", 10000, 1600)
book.add_book()
book.año_publicado()
