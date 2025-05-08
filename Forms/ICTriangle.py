from .ICForm import ICForm
from .ICPoint2D import ICPoint2D

class ICTriangle(ICForm):
  def __init__(self, Pa:ICPoint2D, Pb:ICPoint2D, Pc:ICPoint2D, system_origin:ICPoint2D = ICPoint2D(), virtual_form:bool = False) -> None:
    self.Pa = Pa
    self.Pb = Pb
    self.Pc = Pc
    self.catx = 0.0
    self.caty = 0.0
    self.tang = 0.0
    self.length = 0.0
    self.height = 0.0
    self.orientation = 0
    self.__c_orientation_and_cathetus() 
    if(not self.__valido()):
      return -1
    super().__init__(self.__c_centroid(), virtual_form)
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_moment_of_inertia()
    self.Jo = self._c_polar_moment()
    self.Ixy = self.__c_product_of_inertia()
    return None

  @property
  def Pa(self) -> float:
    return self.__Pa

  @Pa.setter
  def Pa(self, Pa:float) -> None:
    self.__Pa = Pa
    return None

  @property
  def Pb(self) -> float:
    return self.__Pb

  @Pb.setter
  def Pb(self, Pb:float) -> None:
    self.__Pb = Pb
    return None

  @property
  def Pc(self) -> float:
    return self.__Pc

  @Pc.setter
  def Pc(self, Pc:float) -> None:
    self.__Pc = Pc
    return None
  
  def __valido(self) -> bool:  
    if(not (self.catx < abs(self.caty + self.tang))):
      return False
    
    if(not (self.caty < abs(self.catx + self.tang))):
      return False
    
    if(not (self.tang < abs(self.catx + self.caty))):
      return False

    return True
  
  def __c_orientation_and_cathetus(self) -> None:
    if(self.Pa.y == self.Pb.y):
      self.catx = self.Pa.euclidean_distance(self.Pb)
      
      if(self.Pa.x == self.Pc.x):
        self.caty = self.Pa.euclidean_distance(self.Pc)
        self.tang = self.Pb.euclidean_distance(self.Pc)
        if(self.Pc.x < self.Pb.x):
          if(self.Pc.y > self.Pb.y):
            self.orientation = 0
          if(self.Pc.y < self.Pb.y):
            self.orientation = 3
        if(self.Pc.x > self.Pb.x):
          if(self.Pc.y > self.Pb.y):
            self.orientation = 1
          if(self.Pc.y < self.Pb.y):
            self.orientation = 2
      
      if(self.Pb.x == self.Pc.x):
        self.caty = self.Pb.euclidean_distance(self.Pc)
        self.tang = self.Pa.euclidean_distance(self.Pc)
        if(self.Pc.x < self.Pa.x):
          if(self.Pc.y > self.Pa.y):
            self.orientation = 0
          if(self.Pc.y < self.Pa.y):
            self.orientation = 3
        if(self.Pc.x > self.Pa.x):
          if(self.Pc.y > self.Pa.y):
            self.orientation = 1
          if(self.Pc.y < self.Pa.y):
            self.orientation = 2

    if(self.Pb.y == self.Pc.y):
      self.catx = self.Pb.euclidean_distance(self.Pc)
      
      if(self.Pb.x == self.Pa.x):
        self.caty = self.Pb.euclidean_distance(self.Pa)
        self.tang = self.Pc.euclidean_distance(self.Pa)
        if(self.Pa.x < self.Pc.x):
          if(self.Pa.y > self.Pc.y):
            self.orientation = 0
          if(self.Pa.y < self.Pc.y):
            self.orientation = 3
        if(self.Pa.x > self.Pc.x):
          if(self.Pa.y > self.Pc.y):
            self.orientation = 1
          if(self.Pa.y < self.Pc.y):
            self.orientation = 2

      if(self.Pc.x == self.Pa.x):
        self.caty = self.Pc.euclidean_distance(self.Pa)
        self.tang = self.Pb.euclidean_distance(self.Pa)
        if(self.Pa.x < self.Pb.x):
          if(self.Pa.y > self.Pb.y):
            self.orientation = 0
          if(self.Pa.y < self.Pb.y):
            self.orientation = 3
        if(self.Pa.x > self.Pb.x):
          if(self.Pa.y > self.Pb.y):
            self.orientation = 1
          if(self.Pa.y < self.Pb.y):
            self.orientation = 2

    if(self.Pc.y == self.Pa.y):
      self.catx = self.Pc.euclidean_distance(self.Pa)
      
      if(self.Pa.x == self.Pb.x):
        self.caty = self.Pa.euclidean_distance(self.Pb)
        self.tang = self.Pc.euclidean_distance(self.Pb)
        if(self.Pb.x < self.Pc.x):
          if(self.Pb.y > self.Pc.y):
            self.orientation = 0
          if(self.Pb.y < self.Pc.y):
            self.orientation = 3
        if(self.Pb.x > self.Pc.x):
          if(self.Pb.y > self.Pc.y):
            self.orientation = 1
          if(self.Pb.y < self.Pc.y):
            self.orientation = 2

      if(self.Pc.x == self.Pb.x):
        self.caty = self.Pc.euclidean_distance(self.Pb)
        self.tang = self.Pa.euclidean_distance(self.Pb)
        if(self.Pb.x < self.Pa.x):
          if(self.Pb.y > self.Pa.y):
            self.orientation = 0
          if(self.Pb.y < self.Pa.y):
            self.orientation = 3
        if(self.Pb.x > self.Pa.x):
          if(self.Pb.y > self.Pa.y):
            self.orientation = 1
          if(self.Pb.y < self.Pa.y):
            self.orientation = 2
  
    self.length = self.catx
    self.height = self.caty
    return None

  def __c_area(self) -> float:
    return ((self.length * self.height) / 2)
  
  def __c_centroid(self) -> ICPoint2D:
    return ICPoint2D(((self.Pa.x + self.Pb.x + self.Pc.x) / 3), ((self.Pa.y + self.Pb.y + self.Pc.y) / 3))
  
  def __c_moment_of_inertia(self) -> float:
    ix = self.virtual_form * ((self.length * (self.height ** 3)) / 36) + (self.area * (self.centroid.y ** 2))
    iy = self.virtual_form * ((self.height * (self.length ** 3)) / 36) + (self.area * (self.centroid.x ** 2))
    return ix,iy
  
  def __c_product_of_inertia(self) -> float:
    if((self.orientation == 0) or (self.orientation == 2)):
      signal_self_product_of_inertia = -1
    
    if((self.orientation == 1) or (self.orientation == 3)):
      signal_self_product_of_inertia = 1
    
    return (self.virtual_form * (signal_self_product_of_inertia * (((self.length ** 2) * (self.height ** 2)) / 72)) * (self.area * self.centroid.x * self.centroid.y))
