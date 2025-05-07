from .Forma import Forma
from .Ponto2D import Ponto2D

class Circulo(Forma):
  def __init__(self, raio:float = 0.0, centroide:Ponto2D = Ponto2D(), origem_sistema:Ponto2D = Ponto2D(0, 0), forma_virtual:bool = False):
    self.raio = raio
    super().__init__(centroide, origem_sistema, forma_virtual)
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_momento()
    self.Jo = self._c_momento_polar()
    self.Ixy = self.__c_produto()
    return None

  @property
  def raio(self) -> float:
    return self.__raio
  
  @raio.setter
  def raio(self, raio) -> None:
    self.__raio = raio
    return None

  def __c_area(self) -> float:
    return (3.14 * (self.raio * self.raio))

  def __c_momento(self) -> float:
    ix = self.forma_virtual * (((3.14 * (self.raio ** 4)) / 4) + (self.area * (self.centroide.y ** 2)))
    iy = self.forma_virtual * (((3.14 * (self.raio ** 4)) / 4) + (self.area * (self.centroide.x ** 2)))
    return ix, iy
  
  def __c_produto(self) -> float:
    return (self.forma_virtual * (self.area * self.centroide.x * self.centroide.y))
 