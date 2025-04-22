from .Forma import Forma
from .Ponto2D import Ponto2D


class Retangulo(Forma):
  def __init__(self, base:float = 0.0, altura:float = 0.0, origem:Ponto2D = Ponto2D(), centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    super().__init__(origem, centroide, forma_virtual)
    self.base = base
    self.altura = altura
    self.area = self.__c_area()
    self.Qx, self.Qy = self.momento_estatico()
    self.Ix, self.Iy = self.momento()

  @property
  def base(self) -> float:
    return self.__base
  
  @base.setter
  def base(self, base) -> None:
    self.__base = base
    #self.update_runtime()

  @property
  def altura(self) -> float:
    return self.__altura

  @altura.setter
  def altura(self, altura) -> None:
    self.__altura = altura
    #self.update_runtime()  
  
  def __c_area(self) -> float:
    return self.base * self.altura
  
  def momento(self) -> float:
    ix = (((self.base * (self.altura * self.altura * self.altura))/12))
    iy = ((self.altura * (self.base * self.base * self.base))/12)
    return ix,iy
  
  def momento_estatico(self) -> float:
    qx = self.centroide.y * self.area
    qy = self.centroide.x * self.area
    return qx, qy
  
  def update_runtime(self) -> None:
    self.area = self.__c_area()
    self.Qx, self.Qy = self.momento_estatico()
    self.Ix, self.Iy = self.momento()

