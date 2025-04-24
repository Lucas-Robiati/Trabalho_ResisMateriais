from .Forma import Forma
from .Ponto2D import Ponto2D


class Retangulo(Forma):
  def __init__(self, base:float = 0.0, altura:float = 0.0, centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    super().__init__(centroide, forma_virtual)
    self.base = base
    self.altura = altura
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_momento()

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
  
  
  def __c_momento(self) -> float:
    ix = self.forma_virtual * ((self.base * (self.altura * self.altura * self.altura))/12) + (self.area * (self.centroide.y * self.centroide.y))
    iy = self.forma_virtual * ((self.altura * (self.base * self.base * self.base))/12) + (self.area * (self.centroide.x * self.centroide.x))
    return ix,iy