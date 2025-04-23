from .Forma import Forma
from .Ponto2D import Ponto2D

class Circulo(Forma):
  def __init__(self, nome:str = "", raio:float = 0.0, origem:Ponto2D = Ponto2D(), centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    super().__init__(nome, origem, centroide, forma_virtual)
    self.raio = raio
    self.area = self.__c_area()
    #self.Qx, self.Qy = self.momento_estatico()
    #self.Ix, self.Iy = self.momento()

  @property
  def raio(self) -> float:
    return self.__raio
  
  @raio.setter
  def raio(self, raio) -> None:
    self.__raio = raio
    #self.update_runtime()

  def __c_area(self) -> float:
    return 2 * 3.14 * self.raio * self.raio

  '''  
  def momento(self) -> float:
    ix = ((3.14 * (self.raio * self.raio * self.raio * self.raio))/4)
    iy = ((3.14 * (self.raio * self.raio * self.raio * self.raio))/4)
    return list(ix, iy)
  
  def momento_estatico(self) -> float:
    qx = self.centroide.y * self.area
    qy = self.centroide.x * self.area
    return list(qx, qy)
    
  def update_runtime(self):
    self.area = self.__c_area()
    self.Qx, self.Qy = self.momento_estatico()
    self.Ix, self.Iy = self.momento()
  '''