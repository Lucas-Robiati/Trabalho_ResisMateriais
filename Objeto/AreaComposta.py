from Formas import Forma
from Formas import Ponto2D
from Formas import Circulo
from Formas import Retangulo
from Formas import Triangulo

class AreaComposta(Forma):
  def __init__(self):
    self.componentes = []
    self.area = 0.0
    # self.Qx, self.Qy = self.momento_estatico()
    # self.centroide = self._c_centroide()
    # self.Ix, self.Iy = self.momento()
    return
  
  '''
  def momento_estatico(self) -> Ponto2D:
    return

  def _c_centroide(self) -> Ponto2D:
    if(not self.componentes):
      return Ponto2D()
    for forma in self.componentes:
      continue
    
    return Ponto2D()
  
  def momento(self):
    return 0.0, 0.0
  '''

  
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
      return
    if(isinstance(outro, Retangulo)):
      self.componentes.append(outro)
      self.__c_area()
      return
    if(isinstance(outro, Triangulo)):
      self.componentes.append(outro)
      self.__c_area()
      return
    return
  
  def drop(self, outro) -> None:
    if(outro in self.componentes):
      self.componentes.remove(outro)
      self.__c_area()
    return