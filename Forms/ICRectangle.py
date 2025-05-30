from .ICForm import ICForm
from .ICPoint2D import ICPoint2D


# A classe ICRetangle representa a forma geometrica do retangulo, esta que por sua vez
# herda todos os atributos e metodos da classe ICForm. Além disso ela também tem
# os seguintes atributos:
# - length: Atributo que representa o comprimento do retangulo
# - height: Atributo que representa a altura do retangulo
# Também são implementados os seguintes métodos:
# - __c_area: Método privado responsável pelo calculo da área do retangulo
# - __c_moment_of_inertia: Método privado responsável pelo calculo do momento de inércia nos eixos x e y
# - __c_product_of_inertia: Método privado responsável pelo calculo do produto de inércia
# - update função responsavel pela rotina de atualização dos valores calculados após a edição dos atributos



class ICRectangle(ICForm):
  # A função __init__ é o construtor da classe ICRectangle
  def __init__(self, width:float = 0.0, height:float = 0.0, centroid:ICPoint2D = ICPoint2D(), system_origin:ICPoint2D = ICPoint2D(), virtual_form:bool = False) -> None:
    self.width = width                                  # Atributo que representa o comprimento
    self.height = height                                  # Atributo que representa a altura
    super().__init__(centroid, system_origin, virtual_form)              # Construtor da classe PAI
    self.area = self.__c_area()                           # Atribuição de valor a área atravéz do retorno da função __c_area
    self.Ix, self.Iy = self.__c_moment_of_inertia()       # Atribuição do valor do momento de inercia atravéz do retorno da função __c_moment_of_inertia
    self.Jo = self._c_polar_moment()                      # Atribuição do valor do momento polar atravéz do retorno da função _c_polar_moment
    self.Ixy = self.__c_product_of_inertia()              # Atribuição do valor do produto de incercia atravéz do retorno da função __c_product_of_inertia
    return None

  # inicio dos getters e setters
  @property
  def width(self) -> float:
    return self.__width
  
  @width.setter
  def width(self, width) -> None:
    self.__width = width
    return None
    
  @property
  def height(self) -> float:
    return self.__height

  @height.setter
  def height(self, height) -> None:
    self.__height = height
    return None
  
  def bottom_left(self):
    return (self.centroid.x - self.width/2, self.centroid.y - self.height/2)

  def __c_area(self) -> float:
    return self.width * self.height

  # fim dos getters e setters


  # função de calculo de momento de inercia
  def __c_moment_of_inertia(self) -> float:
    ix = self.virtual_form * ((self.width * (self.height ** 3)) / 12) + (self.area * ((self.centroid.y - self.system_origin.y) ** 2))
    iy = self.virtual_form * ((self.height * (self.width ** 3)) / 12) + (self.area * ((self.centroid.x - self.system_origin.x) ** 2))
    return ix, iy
  
  # função de calculo de produto de inercia
  def __c_product_of_inertia(self) -> float:
    return (self.virtual_form * (self.area * (self.centroid.x - self.system_origin.x) * (self.centroid.y - self.system_origin.y)))
  
  # Função responsavel pela rotina de atualização de valores calculados
  def update(self) -> None:                         
    self.area = self.__c_area()                                 
    self.Ix, self.Iy = self.__c_moment_of_inertia()             
    self.Jo = self._c_polar_moment()                            
    self.Ixy = self.__c_product_of_inertia()
    return None
    