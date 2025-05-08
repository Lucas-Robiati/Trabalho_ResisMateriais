from .ICPoint2D import ICPoint2D

class ICForm:
  def __init__(self, centroid:ICPoint2D = ICPoint2D(), system_origin:ICPoint2D = ICPoint2D(0, 0), virtual_form:bool = False) -> None:
    self.centroid = centroid
    self.virtual_form = virtual_form
    self.area = 0.0
    self.Ix, self.Iy = 0.0, 0.0
    self.Jo = 0.0
    self.Ixy = 0.0
    return None
  
  @property
  def centroid(self) -> ICPoint2D:
    return self.__centroid.clone()
  
  @centroid.setter
  def centroid(self, centroid:ICPoint2D) -> None:
    self.__centroid = centroid.clone()
    return None

  @property
  def virtual_form(self) -> float:
    if(self.__virtual_form):
      return -1.0
    else:
      return 1.0
  
  @virtual_form.setter
  def virtual_form(self, virtual_form:bool) -> None:
    self.__virtual_form = virtual_form
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

  def _c_polar_moment(self) -> float:
    return (self.Ix + self.Iy)
