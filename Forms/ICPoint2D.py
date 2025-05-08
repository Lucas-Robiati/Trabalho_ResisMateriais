class ICPoint2D:
  def __init__(self, x:float = 0.0, y:float = 0.0) -> None:
    self.x = x
    self.y = y
    return None
  
  @property
  def x(self) -> float:
    return self.__x
  
  @x.setter
  def x(self, x) -> None:
    self.__x = x
    return None

  @property
  def y(self) -> float:
    return self.__y
  
  @y.setter
  def y(self, y) -> None:
    self.__y = y
    return None

  def clone(self) -> 'ICPoint2D':
    return ICPoint2D(self.x, self.y)
  
  def euclidean_distance(self, point:'ICPoint2D') -> float:
    return ((((point.x - self.x) ** 2)+((point.y - self.y) ** 2)) ** 0.5)