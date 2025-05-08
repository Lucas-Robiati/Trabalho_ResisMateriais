from Forms import ICForm
from Forms import ICPoint2D
from Forms import ICCircle
from Forms import ICRectangle
from Forms import ICTriangle

class ICCompositeFigure(ICForm):
  def __init__(self) -> None:
    super().__init__()
    self.components = []   
    return None
  

  def __c_centroid(self) -> ICPoint2D:
    if(not self.components):
      return None
    
    x = 0.0
    y = 0.0
    for form in self.components:
      x += (form.virtual_form * (form.centroid.x * form.area))
      y += (form.virtual_form * (form.centroid.y * form.area)) 
    x = x / (self.area)
    y = y / (self.area)

    self.centroid = ICPoint2D(x, y)    

  def __c_area(self) -> None:
    if not self.components:
      self.area = 0.0
      return None
    
    self.area = 0.0
    for form in self.components:
      self.area += form.area * form.virtual_form
    return None

  def __c_moment_of_inertia(self) -> float:
    if not self.components:
      return 0.0, 0.0
    
    ix, iy = 0.0, 0.0
    for form in self.components:
      ix += form.Ix
      iy += form.Iy

    return ix, iy

  def __c_product_of_inertia(self) -> float:
    if not self.components:
      return 0.0, 0.0
    
    ixy = 0.0
    for form in self.components:
      ixy += form.Ixy

    return ixy
  
  def __c_polar_moment(self) -> None:
    self.Jo = self.Ix + self.Iy
    
  def append(self, other) -> None:
    if((isinstance(other, ICCircle) or (isinstance(other, ICRectangle) or isinstance(other, ICTriangle))) ):
      self.components.append(other)
      self.__c_area()
      self.__c_centroid()
      self.Ix, self.Iy = self.__c_moment_of_inertia()
      self.Ixy = self.__c_product_of_inertia()
      self._c_polar_moment()
      return 
    return
  
  def drop(self, other) -> None:
    if(other in self.components):
      self.components.remove(other)
      self.__c_area()
      self.__c_centroid()
      self.Ix, self.Iy = self.__c_moment_of_inertia()
      self.Ixy = self.__c_product_of_inertia()
      self._c_polar_moment()
    return
  
