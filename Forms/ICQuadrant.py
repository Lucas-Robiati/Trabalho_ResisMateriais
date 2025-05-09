from .ICPoint2D import ICPoint2D
from .ICForm import ICForm

"""
situações de orientation quadrante de circulo
orientation 0: 0°-90°
orientation 1: 90°-180°
orientation 2: 180°-270°
orientation 3: 270°-0°
"""
# A classe ICQuadrant é uma representação do quadrante de circulo, a classe tem os seguintes atributos:
# - radius: raio do quarto de circulo
# - orientation: representa a orientação do quarto de circulo conforme a descrito acima
# - origem: representa a origem do quadrante de circulo
# A classe também implementa os seguiintes métodos:
# - c_centroid: função responsavel pelo calculo do centroide do quadrante de circulo
# - __c_moment_of_inertia: função responsavel pelo calculo do momento de inercia dos eixos x e y
# - __c_product_of_inertia: função resposavel pelo calculo do produto de inercia
# - update função responsavel pela rotina de atualização dos valores calculados após a edição dos atributos



class ICQuadrant(ICForm):
  # a função __init__ é o construtor da classe
  def __init__(self, orientation:int = 0, radius:float = 0.0, origin:ICPoint2D = ICPoint2D(), system_origin:ICPoint2D = ICPoint2D(), virtual_form:bool = False) -> None:
    self.radius = radius                                        # atribuição do valor do raio          
    self.orientation = orientation                              # atribuição da orientação da figura
    self.origin = origin                                        # atribuição da origem do quadrante de circulo
    super().__init__(self.c_centroid(), system_origin, virtual_form)         # inicialização da classe PAI
    self.area = self.__c_area()                                 # atribuição do valor da area atraves do retorno da função __c_area
    self.Ix, self.Iy = self.__c_moment_of_inertia()             # atribuição do valor do momento de inercia atraves do retorno da função __c_moment_of_inertia
    self.Jo = self._c_polar_moment()                            # atribuição do valor do momento polar atraves do retorno da função __c_polar_moment
    self.Ixy = self.__c_product_of_inertia()                    # atribuição do valor do produto de inercia atraves do retor5no da função __c_product_inertia    return None

  # Inicio dos getters e setters
  @property
  def radius(self) -> float:
    return self.__radius

  @radius.setter
  def radius(self, new:float) -> None:
    self.__radius = new
    return None

  @property
  def orientation(self) -> int:
    return self.__orientation

  @orientation.setter
  def orientation(self, new:int) -> None:
    self.__orientation = new
    return None

  @property
  def origin(self) -> ICPoint2D:
    return self.__origin.clone()
  
  @origin.setter
  def origin(self, new:ICPoint2D) -> None:
    self.__origin = new.clone()
    return None

  # fim dos getters e setters

  # Função de calculo do centroide
  def c_centroid(self) -> ICPoint2D:

    # cada if representa uma orientação do quadrante de circulo
    # esta estrutura foi definida devido ao fato que dependendo da orintação 
    # todos os calculos serão diretamente afetados
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
  
  # função de calculo de area
  def __c_area(self) -> float:
    return ((3.14 * (self.radius * self.radius)) / 4)
  
  # função do calculo de momento de inercia
  def __c_moment_of_inertia(self) -> float:
    ix = self.virtual_form * (((3.14 * (self.radius ** 4)) / 16) + (self.area * ((self.centroid.y - self.system_origin.y) ** 2)))
    iy = self.virtual_form * (((3.14 * (self.radius ** 4)) / 16) + (self.area * ((self.centroid.x - self.system_origin.x) ** 2)))
    return ix, iy
  
  # função de calculo de produto de inercia
  def __c_product_of_inertia(self):
    # assim como no calculo do centroide, o produto de inercia também é afetado pela orientação
    # tomando o centroide como origem da figura, a parte negativa contribui mais no produto entao
    # o sinal pode ser invertido devido a isso
    if((self.orientation == 0) or (self.orientation == 2)):
      signal_self_product_of_inertia = -1
    
    if((self.orientation == 1) or (self.orientation == 3)):
      signal_self_product_of_inertia = 1
    
    return (self.virtual_form * (signal_self_product_of_inertia * ((0.001647 * (self.radius ** 4))) + (self.area * (self.centroid.x - self.system_origin.x) * (self.centroid.y - self.system_origin.y ))))
  
  
  # Função responsavel pela rotina de atualização de valores calculados
  def update(self) -> None:
    self.centroid = self.c_centroid()                         
    self.area = self.__c_area()                                 
    self.Ix, self.Iy = self.__c_moment_of_inertia()             
    self.Jo = self._c_polar_moment()                            
    self.Ixy = self.__c_product_of_inertia()
    return None