from .Ponto2D import Ponto2D
from .Forma import Forma

"""
situações de orientação meio_circulo
orientação 0: 0-180
orientação 1: 90-270
orientação 2: 180-0
orientacao 3: 270-90
"""

class SemiCirculo(Forma):
  def __init__(self, orientacao:int = 0, raio:float = 0.0, origem:Ponto2D = Ponto2D(), origem_sistema:Ponto2D = Ponto2D(), forma_virtual:bool = False) -> None:
    self.origem = origem
    self.orientacao = orientacao
    self.raio = raio
    super().__init__(self.__c_centroide(),forma_virtual)
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_momento()
    self.Jo = self._c_momento_polar()
    self.Ixy = self.__c_produto()
    return None
  
  def __c_centroide(self) -> Ponto2D:
    if (self.orientacao == 0):
      centroide = Ponto2D()
      centroide.x = self.origem.x
      centroide.y = self.origem.y + ((4 * self.raio) / (3 * 3.14))
      return centroide
    
    if (self.orientacao == 1):
      centroide = Ponto2D()
      centroide.x = self.origem.x - ((4 * self.raio) / (3 * 3.14))
      centroide.y = self.origem.y
      return centroide
    
    if (self.orientacao == 2):
      centroide = Ponto2D()
      centroide.x = self.origem.x
      centroide.y = self.origem.y - ((4 * self.raio) / (3 * 3.14))
      return centroide
    
    if (self.orientacao == 3):
      centroide = Ponto2D()
      centroide.x = self.origem.x + ((4 * self.raio) / (3 * 3.14))
      centroide.y = self.origem.y
      return centroide
    return Ponto2D()
  
  def __c_area(self) -> float:
    return ((3.14 * (self.raio * self.raio)) / 2)
  
  def __c_momento(self) -> float:
    ix, iy = 0.0, 0.0

    if((self.orientacao == 1) or (self.orientacao == 3)):
      ix = self.forma_virtual * (((3.14 * (self.raio ** 4)) / 8) + (self.area * (self.centroide.x * self.centroide.x)))
      iy = self.forma_virtual * (0.1098 * (self.raio ** 4))
    
    if((self.orientacao == 0) or (self.orientacao == 2)):
      ix = self.forma_virtual * (0.1098 * (self.raio * self.raio * self.raio * self.raio))
      iy = self.forma_virtual * (((3.14 * (self.raio * self.raio * self.raio * self.raio)) / 8) + (self.area * (self.centroide.x * self.centroide.x)))
    
    return ix, iy
  
  def __c_produto(self):
    return (self.forma_virtual * (self.area * self.centroide.x * self.centroide.y))
    
  
   