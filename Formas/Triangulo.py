from .Forma import Forma
from .Ponto2D import Ponto2D

def modulo(valor:float) -> float:
  if(valor < 0.0):
    return valor * (-1.0)
  return valor


"""
triangulo retangulo
vertice a -> ponto2d
vertice b -> ponto2d
vertice c -> ponto2d

"""

class Triangulo(Forma):
  def __init__(self, a:Ponto2D, b:Ponto2D, c:Ponto2D, forma_virtual:bool = False):
    self.Pa = a
    self.Pb = b
    self.Pc = c
    self.base = 0.0
    self.cat = 0.0
    self.cat2 = 0.0
    self.altura = 0.0
    self.semiperimetro = 0.0

    self.__runtime() 


    # |\  
    # | \
    # |  \
    # |___\
    return
    # if(not self.__valido()):
      # return -1
    # super().__init__(centroide, forma_virtual)
    # self.area = self.__c_area()
    # self.Qx, self.Qy = self.momento_estatico()
    # self.Ix, self.Iy = self.momento()

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

  def __c_semiperimetro(self) -> None:
    semiperimetro = ((self.base + self.cat + self.cat2) / 2)
    return 
  
  # Migrar para ponto2D faria mais sentido por se tratar da distancia entre dois
  # pontos no plano
  def __distancia_p2p(p1:Ponto2D, p2:Ponto2D) -> float:
    medida = ((((p2.x - p1.x)*(p2.x - p1.x))+((p2.y - p1.y)(p2.y - p1.y))) ** 0.5)
    return medida
  
  def __runtime(self) -> None:
    self.base = self.__distancia_p2p(self.Pa, self.Pb)
    self.cat = self.__distancia_p2p(self.Pb, self.Pc)
    self.cat2 = self.__distancia_p2p(self.Pa, self.Pc)

    self.__c_semiperimetro()
    
    return
  
  """
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
  """
  def __c_area(self):
    return ((self.a * self.altura) / 2)
  
  '''
  def momento(self) -> float:
    if(self.equilatero() or self.isoceles()):
      return ((self.a * (self.altura * self.altura * self.altura))/ 12), ((self.altura * (self.a * self.a * self.a))/12)
    
    return -1.0, -1.0
  
  def momento_estatico(self) -> float:
    qx = self.centroide.y * self.area
    qy = self.centroide.x * self.area
    return qx, qy
  
  def update_runtime(self):
    if(not self.__valido()):
      return -1
    
    self.area = self.__c_area()
    self.Qx, self.Qy = self.momento_estatico()
    self.Ix, self.Iy = self.momento()
  '''
