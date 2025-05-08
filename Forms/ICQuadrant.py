from .ICPoint2D import ICPoint2D
from .ICForm import ICForm

"""
situações de orientation quarto de circulo
orientation 0: 0-90
orientation 1: 90-180
orientation 2: 180-270
orientation 3: 270-0
"""

class ICQuadrant(ICForm):
  def __init__(self, orientation:int = 0, radius:float = 0.0, origin:ICPoint2D = ICPoint2D(), system_origin:ICPoint2D = ICPoint2D(), virtual_form:bool = False) -> None:
    self.radius = radius
    self.orientation = orientation
    self.origin = origin
    super().__init__(self.__c_centroid(), virtual_form)
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_moment_of_inertia()
    self.Jo = self._c_polar_moment()
    self.Ixy = self.__c_product_of_inertia()
    return None


  def __c_centroid(self) -> ICPoint2D:
    if(self.orientation == 0):
      centroid = ICPoint2D()
      centroid.x = self.origin.x + ((4 * self.radius) / (3 * 3.14))
      centroid.y = self.origin.y + ((4 * self.radius) / (3 * 3.14))
      return centroid
    
    if(self.orientation == 1):
      centroid = ICPoint2D()
      centroid.x = self.origin.x - ((4 * self.radius) / (3 * 3.14))
      centroid.y = self.origin.y + ((4 * self.radius) / (3 * 3.14))
      return centroid
    
    if(self.orientation == 2):
      centroid = ICPoint2D()
      centroid.x = self.origin.x - ((4 * self.radius) / (3 * 3.14))
      centroid.y = self.origin.y - ((4 * self.radius) / (3 * 3.14))
      return centroid
    
    if(self.orientation == 3):
      centroid = ICPoint2D()
      centroid.x = self.origin.x + ((4 * self.radius) / (3 * 3.14))
      centroid.y = self.origin.y - ((4 * self.radius) / (3 * 3.14))
      return centroid
    return ICPoint2D()
  
  def __c_area(self) -> float:
    return ((3.14 * (self.radius * self.radius)) / 4)
  
  def __c_moment_of_inertia(self) -> float:
    ix = self.virtual_form * (((3.14 * (self.radius ** 4)) / 16) + (self.area * (self.centroid.y ** 2)))
    iy = self.virtual_form * (((3.14 * (self.radius ** 4)) / 16) + (self.area * (self.centroid.x ** 2)))
    return ix, iy
  
  def __c_product_of_inertia(self):
    if((self.orientation == 0) or (self.orientation == 2)):
      signal_self_product_of_inertia = -1
    
    if((self.orientation == 1) or (self.orientation == 3)):
      signal_self_product_of_inertia = 1
    
    return (self.virtual_form * (signal_self_product_of_inertia * ((0.001647 * (self.radius ** 4))) + (self.area * self.centroid.x * self.centroid.y)))