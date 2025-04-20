from .Forma import Forma
from .Ponto2D import Ponto2D


class Retangulo(Forma):
  def __init__(self, base:float = 0.0, altura:float = 0.0, origem:Ponto2D = Ponto2D(), centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    super().__init__(origem, centroide, forma_virtual)
    self.base = base
    self.altura = altura
    self.area = self.__c_area()
    self.Ix, self.Iy = self.momento()

  @property
  def base(self) -> float:
    return self.__base
  
  @base.setter
  def base(self, base) -> None:
    self.__base = base

  @property
  def altura(self) -> float:
    return self.__altura

  @altura.setter
  def altura(self, altura) -> None:
    self.__altura = altura  

  def __c_area(self) -> float:
    return self.base * self.altura
  
  def momento(self) -> float:
    return (((self.base * (self.altura * self.altura * self.altura))/12)),((self.altura * (self.base * self.base * self.base))/12)