from .Ponto2D import Ponto2D

class Forma:
  def __init__(self, centroide:Ponto2D = Ponto2D(), origem_sistema:Ponto2D = Ponto2D(0, 0), forma_virtual:bool = False) -> None:
    self.centroide = centroide
    self.forma_virtual = forma_virtual
    self.area = 0.0
    self.Ix, self.Iy = 0.0, 0.0
    self.Jo = 0.0
    self.Ixy = 0.0
    return None
  
  @property
  def centroide (self) -> Ponto2D:
    return self.__centroide.clone()
  
  @centroide.setter
  def centroide(self, centroide:Ponto2D) -> None:
    self.__centroide = centroide.clone()
    return None

  @property
  def forma_virtual(self) -> float:
    if(self.__forma_virtual):
      return -1.0
    else:
      return 1.0
  
  @forma_virtual.setter
  def forma_virtual(self, forma_virtual:bool) -> None:
    self.__forma_virtual = forma_virtual
    return None

  @property
  def area(self) -> float:
    return self.__area
  
  @area.setter
  def area(self, area:float) -> None:
    self.__area = area
    return None
  
  @property
  def Ix(self) -> float:
    return self.__Ix
  
  @Ix.setter
  def Ix(self, Ix:float) -> None:
    self.__Ix = Ix
    return None  
  
  @property
  def Iy(self) -> float:
    return self.__Iy
  
  @Iy.setter
  def Iy(self, Iy:float) -> None:
    self.__Iy = Iy
    return None

  @property
  def Ixy(self) -> float:
    return self.__Ixy
  
  @Ixy.setter
  def Ixy(self, Ixy:float) -> None:
    self.__Ixy = Ixy
    return None  

  def _c_momento_polar(self) -> float:
    return (self.Ix + self.Iy)
