class Ponto2D:
  def __init__(self, x:float = 0.0, y:float = 0.0) -> None:
    self.x = x
    self.y = y
  
  @property
  def x(self) -> float:
    return self.__x
  
  @x.setter
  def x(self, x) -> None:
    self.__x = x

  @property
  def y(self) -> float:
    return self.__y
  
  @y.setter
  def y(self, y) -> None:
    self.__y = y

  def clone(self) -> 'Ponto2D':
    return Ponto2D(self.x, self.y)