from .ICPoint2D import ICPoint2D
from .ICForm import ICForm

"""
situações de orientation meio_circulo
orientation 0: 0-180
orientation 1: 90-270
orientation 2: 180-0
orientation 3: 270-90
"""

class ICSemicircle(ICForm):
  def __init__(self, orientation:int = 0, radius:float = 0.0, origin:ICPoint2D = ICPoint2D(), system_origin:ICPoint2D = ICPoint2D(), virtual_form:bool = False) -> None:
    self.origin = origin
    self.orientation = orientation
    self.radius = radius
    super().__init__(self.__c_centroid(),virtual_form)
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_moment_of_inertia()
    self.Jo = self._c_polar_moment()
    self.Ixy = self.__c_product_of_inertia()
    return None
  
  def __c_centroid(self) -> ICPoint2D:
    if (self.orientation == 0):
      centroid = ICPoint2D()
      centroid.x = self.origin.x
      centroid.y = self.origin.y + ((4 * self.radius) / (3 * 3.14))
      return centroid
    
    if (self.orientation == 1):
      centroid = ICPoint2D()
      centroid.x = self.origin.x - ((4 * self.radius) / (3 * 3.14))
      centroid.y = self.origin.y
      return centroid
    
    if (self.orientation == 2):
      centroid = ICPoint2D()
      centroid.x = self.origin.x
      centroid.y = self.origin.y - ((4 * self.radius) / (3 * 3.14))
      return centroid
    
    if (self.orientation == 3):
      centroid = ICPoint2D()
      centroid.x = self.origin.x + ((4 * self.radius) / (3 * 3.14))
      centroid.y = self.origin.y
      return centroid
    return ICPoint2D()
  
  def __c_area(self) -> float:
    return ((3.14 * (self.radius * self.radius)) / 2)
  
  def __c_moment_of_inertia(self) -> float:
    ix, iy = 0.0, 0.0

    if((self.orientation == 1) or (self.orientation == 3)):
      ix = self.virtual_form * (((3.14 * (self.radius ** 4)) / 8) + (self.area * (self.centroid.x * self.centroid.x)))
      iy = self.virtual_form * (0.1098 * (self.radius ** 4))
    
    if((self.orientation == 0) or (self.orientation == 2)):
      ix = self.virtual_form * (0.1098 * (self.radius * self.radius * self.radius * self.radius))
      iy = self.virtual_form * (((3.14 * (self.radius * self.radius * self.radius * self.radius)) / 8) + (self.area * (self.centroid.x * self.centroid.x)))
    
    return ix, iy
  
  def __c_product_of_inertia(self):
    return (self.virtual_form * (self.area * self.centroid.x * self.centroid.y))
    
  
   