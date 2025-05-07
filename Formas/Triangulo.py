from .Forma import Forma
from .Ponto2D import Ponto2D

"""
triangulo retangulo
vertice a -> ponto2d
vertice b -> ponto2d
vertice c -> ponto2d

"""

class Triangulo(Forma):
  def __init__(self, a:Ponto2D, b:Ponto2D, c:Ponto2D, forma_virtual:bool = False):
    self.Pa = a
    self.Pb = b
    self.Pc = c
    self.catx = 0.0
    self.caty = 0.0
    self.tang = 0.0
    self.base = 0.0
    self.altura = 0.0
    self.orientação = 0
    #self.semiperimetro = 0.0

    self.__c_orientacao_e_catetos() 

    if(not self.__valido()):
      return -1

    super().__init__(self.__c_centroide(), forma_virtual)
    self.area = self.__c_area()
    self.Ix, self.Iy = self.__c_momento()
    self.__c_produto()

    return

  @property
  def Pa(self) -> float:
    return self.__Pa

  @Pa.setter
  def Pa(self, Pa:float) -> None:
    self.__Pa = Pa 

  @property
  def Pb(self) -> float:
    return self.__Pb

  @Pb.setter
  def Pb(self, Pb:float) -> None:
    self.__Pb = Pb

  @property
  def Pc(self) -> float:
    return self.__Pc

  @Pc.setter
  def Pc(self, Pc:float) -> None:
    self.__Pc = Pc
  
  def __valido(self) -> bool:  
    if(not (self.catx < abs(self.caty + self.tang))):
      return False
    
    if(not (self.caty < abs(self.catx + self.tang))):
      return False
    
    if(not (self.tang < abs(self.catx + self.caty))):
      return False
    
    return True

  # Migrar para ponto2D faria mais sentido por se tratar da distancia entre dois
  # pontos no plano
  def __distancia_p2p(self, p1:Ponto2D, p2:Ponto2D) -> float:
    medida = ((((p2.x - p1.x)*(p2.x - p1.x))+((p2.y - p1.y)*(p2.y - p1.y))) ** 0.5)
    return medida
  
  def __c_orientacao_e_catetos(self) -> None:
    if(self.Pa.y == self.Pb.y):
      self.catx = self.__distancia_p2p(self.Pa, self.Pb)
      
      if(self.Pa.x == self.Pc.x):
        self.caty = self.__distancia_p2p(self.Pa, self.Pc)
        self.tang = self.__distancia_p2p(self.Pb, self.Pc)
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
        self.caty = self.__distancia_p2p(self.Pb, self.Pc)
        self.tang = self.__distancia_p2p(self.Pa, self.Pc)
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
      self.catx = self.__distancia_p2p(self.Pb, self.Pc)
      
      if(self.Pb.x == self.Pa.x):
        self.caty = self.__distancia_p2p(self.Pb, self.Pa)
        self.tang = self.__distancia_p2p(self.Pc, self.Pa)
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
        self.caty = self.__distancia_p2p(self.Pc, self.Pa)
        self.tang = self.__distancia_p2p(self.Pb, self.Pa)
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
      self.catx = self.__distancia_p2p(self.Pc, self.Pa)
      
      if(self.Pa.x == self.Pb.x):
        self.caty = self.__distancia_p2p(self.Pa, self.Pb)
        self.tang = self.__distancia_p2p(self.Pc, self.Pb)
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
        self.caty = self.__distancia_p2p(self.Pc, self.Pb)
        self.tang = self.__distancia_p2p(self.Pa, self.Pb)
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
    #self.__c_semiperimetro()
    
    return

  def __c_area(self) -> float:
    return ((self.base * self.altura) / 2)
  
  def __c_centroide(self) -> Ponto2D:
    return Ponto2D(((self.Pa.x + self.Pb.x + self.Pc.x) / 3), ((self.Pa.y + self.Pb.y + self.Pc.y) / 3))
  
  
  def __c_momento(self) -> float:
    ix = self.forma_virtual * ((self.base * (self.altura * self.altura * self.altura))/36) + (self.area * (self.centroide.y * self.centroide.y))
    iy = self.forma_virtual * ((self.altura * (self.base * self.base * self.base))/36) + (self.area * (self.centroide.x * self.centroide.x))
    return ix,iy
  
  def __c_produto(self):
    sinal_produto_inercia_proprio = 1
    if((self.orientação % 1) == 0):
      sinal_produto_inercia_proprio *= -1
      
    self.Ixy = self.forma_virtual * (sinal_produto_inercia_proprio * (((self.base ** 2) * (self.altura ** 2))/72)) * (self.area * self.centroide.x * self.centroide.y)
    return
  
