from .Ponto2D import Ponto2D

class Forma:
  def __init__(self, centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False) -> None:
    self.centroide = centroide
    self.forma_virtual = forma_virtual
    self.area = 0.0
    self.Ix, self.Iy = 0.0, 0.0
    self.Jo = 0.0
    self.Ixy = 0.0
    return
  
  @property
  def centroide (self) -> Ponto2D:
    return self.__centroide.clone()
  
  @centroide.setter
  def centroide(self, centroide:Ponto2D) -> None:
    self.__centroide = centroide.clone()

  @property
  def area(self) -> float:
    return self.__area
  
  @area.setter
  def area(self, area) -> None:
    self.__area = area

  @property
  def forma_virtual(self) -> float:
    if(self.__forma_virtual):
      return -1.0
    else:
      return 1.0
    
  @forma_virtual.setter
  def forma_virtual(self, forma_virtual:bool) -> None:
    self.__forma_virtual = forma_virtual

  def _c_momento_polar(self) -> float:
    self.Jo = self.Ix + self.Iy
    return self.Jo