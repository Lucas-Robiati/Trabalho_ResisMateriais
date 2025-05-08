from .ICForm import ICForm
from .ICPoint2D import ICPoint2D


class ICRectangle(ICForm):
  def __init__(self, width:float = 0.0, height:float = 0.0, centroid:ICPoint2D = ICPoint2D(), system_origin:ICPoint2D = ICPoint2D(), virtual_form:bool = False) -> None:
    self.width = width
    self.height = height
    super().__init__(centroid, virtual_form)
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_moment_of_inertia()
    self.Jo = self._c_polar_moment()
    self.Ixy = self.__c_product_of_inertia()
    return None

  @property
  def width(self) -> float:
    return self.__width
  
  @width.setter
  def width(self, width) -> None:
    self.__width = width
    return None
    
  @property
  def height(self) -> float:
    return self.__height

  @height.setter
  def height(self, height) -> None:
    self.__height = height
    return None
  
  def __c_area(self) -> float:
    return self.width * self.height
  
  def __c_moment_of_inertia(self) -> float:
    ix = self.virtual_form * ((self.width * (self.height ** 3)) / 12) + (self.area * (self.centroid.y ** 2))
    iy = self.virtual_form * ((self.height * (self.width ** 3)) / 12) + (self.area * (self.centroid.x ** 2))
    return ix,iy
  
  def __c_product_of_inertia(self) -> float:
    return (self.virtual_form * (self.area * self.centroid.x * self.centroid.y))
    