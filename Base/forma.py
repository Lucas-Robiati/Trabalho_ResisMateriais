from .ponto2d import Ponto2D
class Forma:
  def __init__(self, origem:Ponto2D, centroide:Ponto2D, forma_virtual:bool) -> None:
    self.origem = origem
    self.centroide = centroide
    self.forma_virtual = forma_virtual
    self.area = 0
    return

  @property
  def origem(self) -> Ponto2D:
    return self.__origem.clone()  

  @origem.setter
  def origem(self, origem:Ponto2D) -> None:
    self.__origem = origem.clone()
  
  @origem.setter
  def origem(self, x:float, y:float) -> None:
    self.__origem = Ponto2D(x,y)
  
  @property
  def centroide (self) -> 'Ponto2D':
    return self.__centroide.clone()
  
  @centroide.setter
  def centroide(self, centroide:Ponto2D) -> None:
    self.__centroide = centroide

  @centroide.setter
  def centroide(self, x:float = 0.0, y:float = 0.0) -> None:
    self.__centroide = Ponto2D(x, y)
  

  