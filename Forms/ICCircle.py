from .ICForm import ICForm
from .ICPoint2D import ICPoint2D

# A classe ICCircle representa o circulo, esta que herda todos os atributos e metodos
# da classe ICForm, além disso a classe também tem os seguintes atributos:
# - radius: representa o raio do circulo
# 
# São implementados também os seguintes métodos
# - __c_area: responsavel pelo calculo da area do circulo
# - __c_moment_of_inertia: responsavel pelo calculo do momento de inercia do circulo no eixo x e y
# - __c_product_of_inertia: responsavel pelo calculo do produto de inercia do circulo
# - update função responsavel pela rotina de atualização dos valores calculados após a edição dos atributos

class ICCircle(ICForm):
  # A função __init__ é o construtor da classe ICCircle
  def __init__(self, radius:float = 0.0, centroid:ICPoint2D = ICPoint2D(), system_origin:ICPoint2D = ICPoint2D(0, 0), virtual_form:bool = False):
    self.radius = radius                                        # Atribuição do valor do raio
    super().__init__(centroid, system_origin, virtual_form)     # Construtor da classe PAI
    self.area = self.__c_area()                                 # Calculo e Atribuição do valor da área
    self.Ix, self.Iy = self.__c_moment_of_inertia()             # Calculo e atribuição do valor do momento de inércia no eixo x e y
    self.Jo = self._c_polar_moment()                            # calculo e atribuição do valor do momento polar
    self.Ixy = self.__c_product_of_inertia()                    # calculo e atribuição do valor do produto de inércia
    return None


  # Inicio dos getters e setters
  @property
  def radius(self) -> float:
    return self.__radius
  
  @radius.setter
  def radius(self, radius) -> None:
    self.__radius = radius
    return None
  
  # fim dos getters e settes

  # calculo da area do circulo
  def __c_area(self) -> float:
    return (3.14 * (self.radius * self.radius))
  
  # calculo do momento de inercia
  def __c_moment_of_inertia(self) -> float:
    ix = self.virtual_form * (((3.14 * (self.radius ** 4)) / 4) + (self.area * (self.centroid.y ** 2)))
    iy = self.virtual_form * (((3.14 * (self.radius ** 4)) / 4) + (self.area * (self.centroid.x ** 2)))
    return ix, iy
  
  # Calculo do produto de inercia 
  def __c_product_of_inertia(self) -> float:
    return (self.virtual_form * (self.area * self.centroid.x * self.centroid.y))
  
  # Função responsavel pela rotina de atualização de valores calculados
  def update(self) -> None:                         
    self.area = self.__c_area()                                 
    self.Ix, self.Iy = self.__c_moment_of_inertia()             
    self.Jo = self._c_polar_moment()                            
    self.Ixy = self.__c_product_of_inertia()
    return None
 