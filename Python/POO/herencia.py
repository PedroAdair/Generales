class Persona():
    def __init__(self,
                 apePat:str, 
                 apeMat:str, 
                 nom:str):
        
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = nom
    
    def mostrarNombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)
    
    def datos(self):
         print(self.mostrarNombreCompleto())
         


class Estudiante(Persona): 
        def __init__(self, 
                     apePat: str, 
                     apeMat: str, 
                     nom: str,
                     pro:str):
             super().__init__(apePat, apeMat, nom)
             self.profesion = pro
        
        def datos(self):
            super().datos()
            print("Profesion: {0}".format(self.profesion))

estu1 = Estudiante("Torres", "Perez", "Luis", "Ing")

# print(estu1.mostrarNombreCompleto())
# print(estu1.profesion)

estu1.datos()
print("hola mundo")