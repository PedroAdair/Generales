class ClaseA():
    def __init__(self, par1:str, par2:str) -> None:
         self.parametro1 = par1
         self.parametro2 = par2
    
    def suman(self):
         print(f"{self.parametro1} y {self.parametro2} son amigos")

class ClaseB():

    def __init__(self, par3:int, par4:int, par5:int) -> None:
         self.parametro3 = par3
         self.parametro4 = par4
         self.parametro5 = par5

    def composicion(self):
         total = self.parametro3*self.parametro4 + self.parametro5
         print(f"{self.parametro3}*{self.parametro4} + {self.parametro5} = {total}")

class ClaseX(ClaseA, ClaseB):
    def __init__(self, par1: str, par2: str ,par3:int,  par4:int, par5:int) -> None:
        #   super().__init__(par1, par2)
          ClaseA.__init__(self, par1, par2)
          ClaseB.__init__(self, par3, par4, par5)

    def compromiso(self):
         print(f"{self.parametro1} y {self.parametro2} han ahorrado ${self.parametro3} y ${self.parametro4}, respectivamente. Aun les falta por ahorrar ${self.parametro5} ")

cX1 = ClaseX("Hugo", "Paco",3,4,5)
cX1.compromiso()