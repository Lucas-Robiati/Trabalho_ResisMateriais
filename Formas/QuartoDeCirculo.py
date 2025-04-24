from .Ponto2D import Ponto2D
from .Forma import Forma


class QuartoDeCirculo(Forma):
  def __init__(self, raio:float = 0.0, centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    super().__init__(centroide, forma_virtual)
    self.raio = raio
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_momento()

  def __c_area(self) -> float:
    return ((3.14 * (self.raio * self.raio))/4)
  
  def __c_momento(self) -> float:
    ix = self.forma_virtual * (((3.14 * (self.raio * self.raio * self.raio * self.raio))/16) + (self.area * (self.centroide.y * self.centroide.y)))
    iy = self.forma_virtual * (((3.14 * (self.raio * self.raio * self.raio * self.raio))/16) + (self.area * (self.centroide.x * self.centroide.x)))
    return ix, iy