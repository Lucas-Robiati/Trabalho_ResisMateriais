from .Forma import Forma
from .Ponto2D import Ponto2D

def modulo(valor:float) -> float:
  if(valor < 0.0):
    return valor * (-1.0)
  return valor

class Triangulo(Forma):
  def __init__(self, lado1:float = 0.0, lado2:float = 0.0, lado3:float = 0.0, origem:Ponto2D = Ponto2D(), centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    self.a = lado1
    self.b = lado2
    self.c = lado3
    if(not self.__valido()):
      return
    super().__init__(origem, centroide, forma_virtual)


  def equilatero(self) -> bool:
    return (self.a == self.b) and (self.a == self.c)
  
  def escaleno(self) -> bool:
    return (self.a == self.b) and (self.a != self.c)
  
  def isoceles(self) -> bool:
    if((self. a == self.b) and (self.a != self.c)):
      return True
    
    if((self.a == self.c) and (self.a != b)):
      return True
    
    if((self.b == self.c) and (self.b != self.a)):
      return True

  def __valido(self) -> bool:
    
    if(not (self.a < modulo(self.c + self.b))):
      return False
    
    if(not (self.b < modulo(self.a + self.c))):
      return False
    
    if(not (self.c < modulo(self.a + self.b))):
      return False
    
    return True