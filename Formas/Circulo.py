from .Forma import Forma
from .Ponto2D import Ponto2D

class Circulo(Forma):
  def __init__(self, raio:float = 0.0, origem:Ponto2D = Ponto2D(), centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    super().__init__(origem, centroide, forma_virtual)
    self.raio = raio
    self.area = self.__c_area()
    self.Ix, self.Iy = self.momento()

  @property
  def raio(self) -> float:
    return self.__raio
  
  @raio.setter
  def raio(self, raio) -> None:
    self.__raio = raio

  def __c_area(self) -> float:
    return 2 * 3.14 * self.raio
  
  def momento(self) -> float:
    return ((3.14 * (self.raio * self.raio * self.raio * self.raio))/4), ((3.14 * (self.raio * self.raio * self.raio * self.raio))/4)
    