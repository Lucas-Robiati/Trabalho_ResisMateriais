from .Forma import Forma
from .Ponto2D import Ponto2D


class Retangulo(Forma):
  def __init__(self, base:float = 0.0, altura:float = 0.0, centroide:Ponto2D = Ponto2D(), origem_sistema:Ponto2D = Ponto2D(), forma_virtual:bool = False) -> None:
    self.base = base
    self.altura = altura
    super().__init__(centroide, forma_virtual)
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_momento()
    self.Jo = self._c_momento_polar()
    self.Ixy = self.__c_produto()
    return None

  @property
  def base(self) -> float:
    return self.__base
  
  @base.setter
  def base(self, base) -> None:
    self.__base = base
    return None
    
  @property
  def altura(self) -> float:
    return self.__altura

  @altura.setter
  def altura(self, altura) -> None:
    self.__altura = altura
    return None
  
  def __c_area(self) -> float:
    return self.base * self.altura
  
  def __c_momento(self) -> float:
    ix = self.forma_virtual * ((self.base * (self.altura ** 3)) / 12) + (self.area * (self.centroide.y ** 2))
    iy = self.forma_virtual * ((self.altura * (self.base ** 3)) / 12) + (self.area * (self.centroide.x ** 2))
    return ix,iy
  
  def __c_produto(self) -> float:
    return (self.forma_virtual * (self.area * self.centroide.x * self.centroide.y))
    