
# A classe ICPoint2D é responsavel por armazenar coordenadas no plano cartesiano,
# esta classe tem os seguintes atributos:
# 
#  - x: representa uma coordenada no eixo x
# 
#  - y: representa uma coordenada no eixo y
# 
# A classe também tem os seguintes métodos:
# 
# - clone: retorna um objeto igual a si mesmo
# 
# - euclidean_distance: calcula a distancia euclidiana entre o ponto e um outro
#passado por parametro


class ICPoint2D:
  # A função __init__ é o construtor da classe, aqui instanciamos e atrtibuimos o valor
  # aos atributos da classe
  def __init__(self, x:float = 0.0, y:float = 0.0) -> None:
    self.y = y    # Atributo que representa a coordenada y de um ponto
    self.x = x    # Atributo que representa a coordenada X de um ponto
    return None
  

  # Inicio dos getters e setters de cada atributo
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
  # Fim dos getters e setters

  # Metodo Clone
  def clone(self) -> 'ICPoint2D':
    return ICPoint2D(self.x, self.y)

  
  # Calculo da distancia euclidiana
  def euclidean_distance(self, point:'ICPoint2D') -> float:
    return ((((point.x - self.x) ** 2)+((point.y - self.y) ** 2)) ** 0.5)
  
  