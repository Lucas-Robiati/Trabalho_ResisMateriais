from .Ponto2D import Ponto2D
from .Forma import Forma

"""
situações de orientação quarto de circulo
orientação 0: 0-90
orientação 1: 90-180
orientação 2: 180-270
orientacao 3: 270-0
"""

class QuartoDeCirculo(Forma):
  def __init__(self, orientacao:int = 0, raio:float = 0.0, origem:Ponto2D = Ponto2D(), origem_sistema:Ponto2D = Ponto2D(), forma_virtual:bool = False) -> None:
    self.raio = raio
    self.orientacao = orientacao
    self.origem = origem
    super().__init__(self.__c_centroide(), forma_virtual)
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_momento()
    self.Ixy = self.__c_produto()
    return None


  def __c_centroide(self) -> Ponto2D:
    if(self.orientacao == 0):
      centroide = Ponto2D()
      centroide.x = self.origem.x + ((4 * self.raio) / (3 * 3.14))
      centroide.y = self.origem.y + ((4 * self.raio) / (3 * 3.14))
      return centroide
    
    if(self.orientacao == 1):
      centroide = Ponto2D()
      centroide.x = self.origem.x - ((4 * self.raio) / (3 * 3.14))
      centroide.y = self.origem.y + ((4 * self.raio) / (3 * 3.14))
      return centroide
    
    if(self.orientacao == 2):
      centroide = Ponto2D()
      centroide.x = self.origem.x - ((4 * self.raio) / (3 * 3.14))
      centroide.y = self.origem.y - ((4 * self.raio) / (3 * 3.14))
      return centroide
    
    if(self.orientacao == 3):
      centroide = Ponto2D()
      centroide.x = self.origem.x + ((4 * self.raio) / (3 * 3.14))
      centroide.y = self.origem.y - ((4 * self.raio) / (3 * 3.14))
      return centroide
    return Ponto2D()
  
  def __c_area(self) -> float:
    return ((3.14 * (self.raio * self.raio)) / 4)
  
  def __c_momento(self) -> float:
    ix = self.forma_virtual * (((3.14 * (self.raio ** 4)) / 16) + (self.area * (self.centroide.y ** 2)))
    iy = self.forma_virtual * (((3.14 * (self.raio ** 4)) / 16) + (self.area * (self.centroide.x ** 2)))
    return ix, iy
  
  def __c_produto(self):
    return (self.forma_virtual * ((0.001647 * (self.raio ** 4)) + (self.area * self.centroide.x * self.centroide.y)))