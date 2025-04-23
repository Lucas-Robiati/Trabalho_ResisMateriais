from Formas import Forma
from Formas import Ponto2D
from Formas import Circulo
from Formas import Retangulo
from Formas import Triangulo

class AreaComposta(Forma):
  def __init__(self):
    self.componentes = []
    self.area = 0.0
    self.centroide = Ponto2D()
    # self.Qx, self.Qy = self.momento_estatico()
    # self.centroide = self._c_centroide()
    # self.Ix, self.Iy = self.momento()
    return
  

  def __c_centroide(self) -> Ponto2D:
    if(not self.componentes()):
      return
    
    x = 0.0
    y = 0.0
    for forma in self.componentes:
      x += forma.centroide.x * forma.area * forma.forma_virtual
      y += forma.centroide.y * forma.area * forma.forma_virtual
    x = x/self.area
    y = y/self.area

    self.centroide = Ponto2D(x, y)    

  def __c_area(self) -> None:
    if not self.componentes:
      self.area = 0.0
      return
    
    self.area = 0.0
    for forma in self.componentes:
      self.area += forma.area * forma.forma_virtual



  def append(self, outro) -> None:
    if(isinstance(outro, Circulo)):
      self.componentes.append(outro)
      self.__c_area()
      self.__c_centroide()
      return
    
    if(isinstance(outro, Retangulo)):
      self.componentes.append(outro)
      self.__c_area()
      self.__c_centroide()
      return
    
    if(isinstance(outro, Triangulo)):
      self.componentes.append(outro)
      self.__c_area()
      self.__c_centroide
      return
    
    return
  
  def drop(self, outro) -> None:
    if(outro in self.componentes):
      self.componentes.remove(outro)
      self.__c_area()
      self.__c_centroide()
    return