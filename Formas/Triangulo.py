from .Forma import Forma
from .Ponto2D import Ponto2D

class Triangulo(Forma):
  def __init__(self, Pa:Ponto2D, Pb:Ponto2D, Pc:Ponto2D, origem_sistema:Ponto2D = Ponto2D(), forma_virtual:bool = False) -> None:
    self.Pa = Pa
    self.Pb = Pb
    self.Pc = Pc
    self.catx = 0.0
    self.caty = 0.0
    self.tang = 0.0
    self.base = 0.0
    self.altura = 0.0
    self.orientação = 0
    self.__c_orientacao_e_catetos() 
    if(not self.__valido()):
      return -1
    super().__init__(self.__c_centroide(), forma_virtual)
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_momento()
    self.Jo = self._c_momento_polar()
    self.Ixy = self.__c_produto()
    return None

  @property
  def Pa(self) -> float:
    return self.__Pa

  @Pa.setter
  def Pa(self, Pa:float) -> None:
    self.__Pa = Pa
    return None

  @property
  def Pb(self) -> float:
    return self.__Pb

  @Pb.setter
  def Pb(self, Pb:float) -> None:
    self.__Pb = Pb
    return None

  @property
  def Pc(self) -> float:
    return self.__Pc

  @Pc.setter
  def Pc(self, Pc:float) -> None:
    self.__Pc = Pc
    return None
  
  def __valido(self) -> bool:  
    if(not (self.catx < abs(self.caty + self.tang))):
      return False
    
    if(not (self.caty < abs(self.catx + self.tang))):
      return False
    
    if(not (self.tang < abs(self.catx + self.caty))):
      return False

    return True
  
  def __c_orientacao_e_catetos(self) -> None:
    if(self.Pa.y == self.Pb.y):
      self.catx = self.Pa.distancia_euclidiana(self.Pb)
      
      if(self.Pa.x == self.Pc.x):
        self.caty = self.Pa.distancia_euclidiana(self.Pc)
        self.tang = self.Pb.distancia_euclidiana(self.Pc)
        if(self.Pc.x < self.Pb.x):
          if(self.Pc.y > self.Pb.y):
            self.orientação = 0
          if(self.Pc.y < self.Pb.y):
            self.orientação = 3
        if(self.Pc.x > self.Pb.x):
          if(self.Pc.y > self.Pb.y):
            self.orientação = 1
          if(self.Pc.y < self.Pb.y):
            self.orientação = 2
      
      if(self.Pb.x == self.Pc.x):
        self.caty = self.Pb.distancia_euclidiana(self.Pc)
        self.tang = self.Pa.distancia_euclidiana(self.Pc)
        if(self.Pc.x < self.Pa.x):
          if(self.Pc.y > self.Pa.y):
            self.orientação = 0
          if(self.Pc.y < self.Pa.y):
            self.orientação = 3
        if(self.Pc.x > self.Pa.x):
          if(self.Pc.y > self.Pa.y):
            self.orientação = 1
          if(self.Pc.y < self.Pa.y):
            self.orientação = 2

    if(self.Pb.y == self.Pc.y):
      self.catx = self.Pb.distancia_euclidiana(self.Pc)
      
      if(self.Pb.x == self.Pa.x):
        self.caty = self.Pb.distancia_euclidiana(self.Pa)
        self.tang = self.Pc.distancia_euclidiana(self.Pa)
        if(self.Pa.x < self.Pc.x):
          if(self.Pa.y > self.Pc.y):
            self.orientação = 0
          if(self.Pa.y < self.Pc.y):
            self.orientação = 3
        if(self.Pa.x > self.Pc.x):
          if(self.Pa.y > self.Pc.y):
            self.orientação = 1
          if(self.Pa.y < self.Pc.y):
            self.orientação = 2

      if(self.Pc.x == self.Pa.x):
        self.caty = self.Pc.distancia_euclidiana(self.Pa)
        self.tang = self.Pb.distancia_euclidiana(self.Pa)
        if(self.Pa.x < self.Pb.x):
          if(self.Pa.y > self.Pb.y):
            self.orientação = 0
          if(self.Pa.y < self.Pb.y):
            self.orientação = 3
        if(self.Pa.x > self.Pb.x):
          if(self.Pa.y > self.Pb.y):
            self.orientação = 1
          if(self.Pa.y < self.Pb.y):
            self.orientação = 2

    if(self.Pc.y == self.Pa.y):
      self.catx = self.Pc.distancia_euclidiana(self.Pa)
      
      if(self.Pa.x == self.Pb.x):
        self.caty = self.Pa.distancia_euclidiana(self.Pb)
        self.tang = self.Pc.distancia_euclidiana(self.Pb)
        if(self.Pb.x < self.Pc.x):
          if(self.Pb.y > self.Pc.y):
            self.orientação = 0
          if(self.Pb.y < self.Pc.y):
            self.orientação = 3
        if(self.Pb.x > self.Pc.x):
          if(self.Pb.y > self.Pc.y):
            self.orientação = 1
          if(self.Pb.y < self.Pc.y):
            self.orientação = 2

      if(self.Pc.x == self.Pb.x):
        self.caty = self.Pc.distancia_euclidiana(self.Pb)
        self.tang = self.Pa.distancia_euclidiana(self.Pb)
        if(self.Pb.x < self.Pa.x):
          if(self.Pb.y > self.Pa.y):
            self.orientação = 0
          if(self.Pb.y < self.Pa.y):
            self.orientação = 3
        if(self.Pb.x > self.Pa.x):
          if(self.Pb.y > self.Pa.y):
            self.orientação = 1
          if(self.Pb.y < self.Pa.y):
            self.orientação = 2
  
    self.base = self.catx
    self.altura = self.caty
    return None

  def __c_area(self) -> float:
    return ((self.base * self.altura) / 2)
  
  def __c_centroide(self) -> Ponto2D:
    return Ponto2D(((self.Pa.x + self.Pb.x + self.Pc.x) / 3), ((self.Pa.y + self.Pb.y + self.Pc.y) / 3))
  
  def __c_momento(self) -> float:
    ix = self.forma_virtual * ((self.base * (self.altura ** 3)) / 36) + (self.area * (self.centroide.y ** 2))
    iy = self.forma_virtual * ((self.altura * (self.base ** 3)) / 36) + (self.area * (self.centroide.x ** 2))
    return ix,iy
  
  def __c_produto(self) -> float:
    if((self.orientacao == 0) or (self.orientacao == 2)):
      sinal_produto_inercia_proprio = -1
    
    if((self.orientacao == 1) or (self.orientacao == 3)):
      sinal_produto_inercia_proprio = 1
    
    return (self.forma_virtual * (sinal_produto_inercia_proprio * (((self.base ** 2) * (self.altura ** 2)) / 72)) * (self.area * self.centroide.x * self.centroide.y))
