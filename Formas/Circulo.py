from .Forma import Forma
from .Ponto2D import Ponto2D

class Circulo(Forma):
  def __init__(self, raio:float = 0.0, centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    super().__init__(centroide, forma_virtual)
    self.raio = raio
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_momento()

  @property
  def raio(self) -> float:
    return self.__raio
  
  @raio.setter
  def raio(self, raio) -> None:
    self.__raio = raio


  def __c_area(self) -> float:
    return 3.14 * (self.raio * self.raio)

  
  def __c_momento(self) -> float:
    ix = self.forma_virtual * (((3.14 * (self.raio * self.raio * self.raio * self.raio))/4) + (self.area * (self.centroide.y * self.centroide.y)))
    iy = self.forma_virtual * (((3.14 * (self.raio * self.raio * self.raio * self.raio))/4) + (self.area * (self.centroide.x * self.centroide.x)))
    return ix, iy
 
