from .ICPoint2D import ICPoint2D
from .ICForm import ICForm

"""
situações de orientation meio_circulo
orientation 0: 0°-180°
orientation 1: 90°-270°
orientation 2: 180°-0°
orientation 3: 270°-90°
"""

# A classe ICSemicircle é resposavel por representar o semicirculo, esta que contem os seguintes atributos:
# - origim: representa a origem do semi circulo
# - orientation: representa a orientação do semicirculo conforme as orientações descritas acima
# - radius: representa o raio do semicirculo
# 
# A classe também implementa os seguiintes métodos:
# __c_centroid: função responsavel pelo calculo do centroide do quadrante de circulo
# __c_moment_of_inertia: função responsavel pelo calculo do momento de inercia dos eixos x e y
# __c_product_of_inertia: função resposavel pelo calculo do produto de inercia
# - update função responsavel pela rotina de atualização dos valores calculados após a edição dos atributos

class ICSemicircle(ICForm):
  def __init__(self, orientation:int = 0, radius:float = 0.0, origin:ICPoint2D = ICPoint2D(), system_origin:ICPoint2D = ICPoint2D(), virtual_form:bool = False) -> None:
    self.origin = origin                                                        # atribuição da origem do semicirculo
    self.orientation = orientation                                              # atribuição da orientação da figura
    self.radius = radius                                                        # atribuição do valor do raio          
    super().__init__(self.__c_centroid(), system_origin, virtual_form)          # inicialização da classe PAI
    self.area = self.__c_area()                                                 # calculo da area
    self.Ix, self.Iy = self.__c_moment_of_inertia()                             # calculo do momento de inercia
    self.Jo = self._c_polar_moment()                                            # calculo do momento polar
    self.Ixy = self.__c_product_of_inertia()                                    # calculo do produto de inercia
    return None
  
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

  # função do calculo de centroide levando em consideração a orientação do semicirculo
  def __c_centroid(self) -> ICPoint2D:
    if (self.orientation == 0):
      centroid = ICPoint2D()
      centroid.x = self.origin.x
      centroid.y = self.origin.y + ((4 * self.radius) / (3 * 3.14))
      return centroid
    
    if (self.orientation == 1):
      centroid = ICPoint2D()
      centroid.x = self.origin.x - ((4 * self.radius) / (3 * 3.14))
      centroid.y = self.origin.y
      return centroid
    
    if (self.orientation == 2):
      centroid = ICPoint2D()
      centroid.x = self.origin.x
      centroid.y = self.origin.y - ((4 * self.radius) / (3 * 3.14))
      return centroid
    
    if (self.orientation == 3):
      centroid = ICPoint2D()
      centroid.x = self.origin.x + ((4 * self.radius) / (3 * 3.14))
      centroid.y = self.origin.y
      return centroid
    return ICPoint2D()
  
  # calculo da area
  def __c_area(self) -> float:
    return ((3.14 * (self.radius * self.radius)) / 2)
  # calculo do momento de inerca
  def __c_moment_of_inertia(self) -> float:
    ix, iy = 0.0, 0.0

    if((self.orientation == 1) or (self.orientation == 3)):
      ix = self.virtual_form * (((3.14 * (self.radius ** 4)) / 8) + (self.area * ((self.centroid.y - self.system_origin.y) ** 2)))
      iy = self.virtual_form * (0.1098 * (self.radius ** 4))
    
    if((self.orientation == 0) or (self.orientation == 2)):
      ix = self.virtual_form * (0.1098 * (self.radius * self.radius * self.radius * self.radius))
      iy = self.virtual_form * (((3.14 * (self.radius * self.radius * self.radius * self.radius)) / 8) + (self.area * ((self.centroid.x - self.system_origin.x) ** 2)))
    
    return ix, iy
  
  # calculo do produto de inercia
  def __c_product_of_inertia(self):
    return (self.virtual_form * (self.area * (self.centroid.x - self.system_origin.x) * (self.centroid.y - self.system_origin.y)))
  
  # função responsavel pela atualização de valores calculados
  def update(self) -> None:
    self.centroid = self.__c_centroid()                         
    self.area = self.__c_area()                                 
    self.Ix, self.Iy = self.__c_moment_of_inertia()             
    self.Jo = self._c_polar_moment()                            
    self.Ixy = self.__c_product_of_inertia()
    return None
    
  
   