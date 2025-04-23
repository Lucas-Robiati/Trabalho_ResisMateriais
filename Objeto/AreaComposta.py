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
    self.Ix, self.Iy = 0.0, 0.0
    return
  

  def __c_centroide(self) -> Ponto2D:
    if(not self.componentes):
      return
    
    x = 0.0
    y = 0.0
    for forma in self.componentes:
      x += forma.centroide.x * forma.area
      y += forma.centroide.y * forma.area 
    x = x/(self.area)
    y = y/(self.area)

    self.centroide = Ponto2D(x, y)    

  def __c_area(self) -> None:
    if not self.componentes:
      self.area = 0.0
      return
    
    self.area = 0.0
    for forma in self.componentes:
      self.area += forma.area * forma.forma_virtual


  def __c_momento(self) -> float:
    if not self.componentes:
      return 0.0, 0.0
    
    ix, iy = 0.0, 0.0
    for forma in self.componentes:
      ix += forma.forma_virtual * forma.Ix + (forma.area *forma.centroide.y)
      iy += forma.forma_virtual * forma.Iy + (forma.area *forma.centroide.y)

    return ix, iy

  def append(self, outro) -> None:
    if(isinstance(outro, Circulo)):
      self.componentes.append(outro)
      self.__c_area()
      self.__c_centroide()
      self.Ix, self.Iy = self.__c_momento()
      return
    
    if(isinstance(outro, Retangulo)):
      self.componentes.append(outro)
      self.__c_area()
      self.__c_centroide()
      self.Ix, self.Iy = self.__c_momento()
      return
    
    if(isinstance(outro, Triangulo)):
      self.componentes.append(outro)
      self.__c_area()
      self.__c_centroide
      self.Ix, self.Iy = self.__c_momento()
      return
    
    return
  
  def drop(self, outro) -> None:
    if(outro in self.componentes):
      self.componentes.remove(outro)
      self.__c_area()
      self.__c_centroide()
      self.Ix, self.Iy = self.__c_momento()
    return
  
