from Formas import Forma
from Formas import Ponto2D
from Formas import Circulo
from Formas import Retangulo
from Formas import Triangulo

class AreaComposta(Forma):
  def __init__(self):
    self.componentes = []
    self.Qx, self.Qy = self.momento_estatico()
    self.centroide = self._c_centroide()
    self.Ix, self.Iy = self.momento()
    return
  
  def momento_estatico(self) -> Ponto2D:
    return

  def _c_centroide(self) -> Ponto2D:
    if(not self.componentes):
      return Ponto2D()
    for forma in self.componentes:
      continue
    
    return Ponto2D()
  
  def momento(self):
    return 0.0, 0.0
  
  def append(self, outro) -> None:
    if(isinstance(outro, Circulo)):
      self.componentes.append(outro)
      return
    if(isinstance(outro, Retangulo)):
      self.componentes.append(outro)
      return
    if(isinstance(outro, Triangulo)):
      self.componentes.append(outro)
      return
    return