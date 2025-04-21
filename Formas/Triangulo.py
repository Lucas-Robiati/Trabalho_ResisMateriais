from .Forma import Forma
from .Ponto2D import Ponto2D

def modulo(valor:float) -> float:
  if(valor < 0.0):
    return valor * (-1.0)
  return valor

class Triangulo(Forma):
  def __init__(self, base:float, altura:float, lado2:float, lado3:float, origem:Ponto2D = Ponto2D(), centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    self.a = base
    self.b = lado2
    self.c = lado3
    self.altura = altura
    if(not self.__valido()):
      return -1
    super().__init__(origem, centroide, forma_virtual)
    self.Ix, self.Iy = self.momento()

  @property
  def a(self) -> float:
    return self.__a

  @a.setter
  def a(self, a:float) -> None:
    self.__a = a  

  @property
  def b(self) -> float:
    return self.__b

  @b.setter
  def b(self, b:float) -> None:
    self.__b = b

  @property
  def c(self) -> float:
    return self.__c

  @c.setter
  def c(self, c:float) -> None:
    self.__c = c


  def equilatero(self) -> bool:
    return (self.a == self.b) and (self.a == self.c)
  
  def escaleno(self) -> bool:
    return (self.a == self.b) and (self.a != self.c)
  
  def isoceles(self) -> bool:
    if((self. a == self.b) and (self.a != self.c)):
      return True
    
    if((self.a == self.c) and (self.a != self.b)):
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
  
  def momento(self) -> float:
    if(self.equilatero() or self.isoceles()):
      return ((self.a * (self.altura * self.altura * self.altura))/ 12), ((self.altura * (self.a * self.a * self.a))/12)
    
    return -1.0, -1.0