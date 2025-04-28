from .Ponto2D import Ponto2D
from .Forma import Forma


class SemiCirculo(Forma):
  def __init__(self, orientacao:int = 0, raio:float = 0.0, centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    super().__init__(centroide,forma_virtual)
    
    self.raio = raio
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_momento()
    self.__c_produto()
    self.orientacao = orientacao

  def __c_area(self) -> float:
    return ((3.14 * (self.raio * self.raio))/2)
  
  def __c_momento(self) -> float:
    if((self.orientacao == 1) or (self.orientacao == 3)):
      ix = self.forma_virtual * (((3.14 * (self.raio * self.raio * self.raio * self.raio))/8) + (self.area * (self.centroide.x * self.centroide.x)))
      iy = self.forma_virtual * (0.1098 * (self.raio * self.raio * self.raio * self.raio))
    
    if((self.orientacao == 0) or (self.orientacao == 2)):
      ix = self.forma_virtual * (0.1098 * (self.raio * self.raio * self.raio * self.raio))
      iy = self.forma_virtual * (((3.14 * (self.raio * self.raio * self.raio * self.raio))/8) + (self.area * (self.centroide.x * self.centroide.x)))
    else:
      return 0.0, 0.0
    
    return ix, iy
  
  def __c_produto(self):
    self.Ixy = self.forma_virtual * (self.area * self.centroide.x * self.centroide.y)
    return
  
   