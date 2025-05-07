class Ponto2D:
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

  def clone(self) -> 'Ponto2D':
    return Ponto2D(self.x, self.y)
  
  def distancia_euclidiana(self, ponto:'Ponto2D') -> float:
    return ((((ponto.x - self.x) ** 2)+((ponto.y - self.y) ** 2)) ** 0.5)