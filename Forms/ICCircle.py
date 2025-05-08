from .ICForm import ICForm
from .ICPoint2D import ICPoint2D

class ICCircle(ICForm):
  def __init__(self, radius:float = 0.0, centroid:ICPoint2D = ICPoint2D(), system_origin:ICPoint2D = ICPoint2D(0, 0), virtual_form:bool = False):
    self.radius = radius
    super().__init__(centroid, system_origin, virtual_form)
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_moment_of_inertia()
    self.Jo = self._c_polar_moment()
    self.Ixy = self.__c_product_of_inertia()
    return None

  @property
  def radius(self) -> float:
    return self.__radius
  
  @radius.setter
  def radius(self, radius) -> None:
    self.__radius = radius
    return None

  def __c_area(self) -> float:
    return (3.14 * (self.radius * self.radius))

  def __c_moment_of_inertia(self) -> float:
    ix = self.virtual_form * (((3.14 * (self.radius ** 4)) / 4) + (self.area * (self.centroid.y ** 2)))
    iy = self.virtual_form * (((3.14 * (self.radius ** 4)) / 4) + (self.area * (self.centroid.x ** 2)))
    return ix, iy
  
  def __c_product_of_inertia(self) -> float:
    return (self.virtual_form * (self.area * self.centroid.x * self.centroid.y))
 