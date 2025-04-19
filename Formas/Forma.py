from .Ponto2D import Ponto2D

class Forma:
  def __init__(self, origem:Ponto2D, centroide:Ponto2D, forma_virtual:bool, area:float = 0.0) -> None:
    self.origem = origem
    self.centroide = centroide
    self.forma_virtual = forma_virtual
    self.area = area
    return

  @property
  def origem(self) -> Ponto2D:
    return self.__origem.clone()  

  @origem.setter
  def origem(self, origem:Ponto2D) -> None:
    self.__origem = origem.clone()
  
  @property
  def centroide (self) -> Ponto2D:
    return self.__centroide.clone()
  
  @centroide.setter
  def centroide(self, centroide:Ponto2D) -> None:
    self.__centroide = centroide

  @property
  def area(self) -> float:
    return self.__area
  
  @area.setter
  def area(self, area) -> None:
    self.__area = area
