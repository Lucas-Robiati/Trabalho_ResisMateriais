from Formas import Forma
from Formas import Ponto2D
from Formas import Circulo
from Formas import Retangulo
from Formas import Triangulo

class AreaComposta(Forma):
  def __init__(self):
    super().__init__()
    self.componentes = []   
    return
  

  def __c_centroide(self) -> Ponto2D:
    if(not self.componentes):
      return
    
    x = 0.0
    y = 0.0
    for forma in self.componentes:
      x += (forma.forma_virtual * (forma.centroide.x * forma.area))
      y += (forma.forma_virtual * (forma.centroide.y * forma.area)) 
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
      ix += forma.Ix
      iy += forma.Iy

    return ix, iy

  def __c_produto_inercia(self) -> float:
    if not self.componentes:
      return 0.0, 0.0
    
    ixy = 0.0
    for forma in self.componentes:
      ixy += forma.Ixy

    return ixy
  
  def __c_momento_polar(self) -> None:
    self.Jo = self.Ix + self.Iy
    
  def append(self, outro) -> None:
    if((isinstance(outro, Circulo) or (isinstance(outro, Retangulo) or isinstance(outro, Triangulo))) ):
      self.componentes.append(outro)
      self.__c_area()
      self.__c_centroide()
      self.Ix, self.Iy = self.__c_momento()
      self.Ixy = self.__c_produto_inercia()
      self._c_momento_polar()
      return 
    return
  
  def drop(self, outro) -> None:
    if(outro in self.componentes):
      self.componentes.remove(outro)
      self.__c_area()
      self.__c_centroide()
      self.Ix, self.Iy = self.__c_momento()
      self.Ixy = self.__c_produto_inercia()
      self._c_momento_polar()
    return
  
