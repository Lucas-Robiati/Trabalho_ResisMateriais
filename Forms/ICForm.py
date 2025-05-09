from .ICPoint2D import ICPoint2D

# A base do projeto se encontra nesta classe ICForm, aqui se encontrão as informações basicas
# de cada forma geometrica. A partir destas informações basicas, nossa classe tem os
# seguintes atriibutos:
# 
# - centroid: Atributo que representa o centroide da forma geometrica no plano cartesiano, este que é um objeto 
#da classe Point2D, onde sao armazenadas as coordenadas x e y do centroide.
# 
# - virtual_form: Atributo que representa se a forma é real ou virtual(forma subtraida da Área composta).
# 
# - area: Atributo que representa a area da forma.
# 
# - Ix: Atributo que representa o momento de inércia da forma em x.
# 
# - Iy: Atributo que representa o momento de inércia da forma em y.
# 
# - Jo: Atributo que representa o momento polar da forma.
# 
# - Ixy: Atributo que representa o produto de inércia da forma.
# 
# Alem dos atributos temos também um método responsável pelo calculo do momento polar, por ser um calculo igual
# para todos as fomas optamos por ele ser parte da classe base.
# 
# É importante lembrar que a classe forma é uma classe ABSTRATA que nao será instanciada de fato, esta
# será usada como classe pai das outras classes, ou seja todas as classes que representam formas geometricas
# e também a área composta sao classes derivadas da classe ICForm 

class ICForm:
  # A função __init__ é o construtor da classe ICForm, aqui todos os atributos são instanciados
  # e inicialmente seus valores são 0.0, a ideia é que cada classe derivada que representa as outras formas
  # grometricas calcule e de valor a estes atributos, usando funções membro de cada respectiva classe
  # ja que para cada forma geometrica temos uma forma de calculo destes atributos 
  def __init__(self, centroid:ICPoint2D = ICPoint2D(), system_origin:ICPoint2D = ICPoint2D(0, 0), virtual_form:bool = False) -> None:
    self.centroid = centroid                # Atributo que representa o centroide da forma
    self.virtual_form = virtual_form        # Atributo que representa a área real ou virtual
    self.area = 0.0                         # Atributo que representa a área da figura
    self.system_origin = system_origin      # Atributo que representa a origem do sistema para os calculos
    self.Ix, self.Iy = 0.0, 0.0             # Atributos que representam o Momento de inércia nos eixos x e y
    self.Jo = 0.0                           # Atributo que representa o Momento Polar
    self.Ixy = 0.0                          # Atributo que representa o Produto de inércia
    return None
  
  # Para cada Atributo da classe, temos os getters e setters, basicamente é uma maneira de acessar atributos
  # privados da classe, e facilitar o tratamento do valor dos atributos abaixo seguem os getters e setters de cada atributo
  
  
  # Início dos getters e setters
  @property
  def centroid(self) -> ICPoint2D:
    return self.__centroid.clone()
  
  @centroid.setter
  def centroid(self, centroid:ICPoint2D) -> None:
    self.__centroid = centroid.clone()
    return None
  
  @property
  def system_origin(self) -> ICPoint2D:
    return self.__system_origin.clone()

  @system_origin.setter
  def system_origin(self, new:ICPoint2D) -> None:
    self.__system_origin = new
    return None
  
   
  @property
  def virtual_form(self) -> float:
    if(self.__virtual_form):
      return -1.0
    else:
      return 1.0
  
  @virtual_form.setter
  def virtual_form(self, virtual_form:bool) -> None:
    self.__virtual_form = virtual_form
    return None

  @property
  def area(self) -> float:
    return self.__area
  
  @area.setter
  def area(self, area:float) -> None:
    self.__area = area
    return None
  
  @property
  def Ix(self) -> float:
    return self.__Ix
  
  @Ix.setter
  def Ix(self, Ix:float) -> None:
    self.__Ix = Ix
    return None  
  
  @property
  def Iy(self) -> float:
    return self.__Iy
  
  @Iy.setter
  def Iy(self, Iy:float) -> None:
    self.__Iy = Iy
    return None

  @property
  def Ixy(self) -> float:
    return self.__Ixy
  
  @Ixy.setter
  def Ixy(self, Ixy:float) -> None:
    self.__Ixy = Ixy
    return None  

  # Fim dos getters e setters

  # Calculo do momento polar
  def _c_polar_moment(self) -> float:
    return (self.Ix + self.Iy)
