from Formas import Forma
from Formas import Ponto2D

class AreaComposta(Forma):
  def __init__(self):
    self.componentes = []
    self.centroide = self._c_centroide()
    self.Ix, self.Iy = self.momento()
    return
  

  def _c_centroide(self) -> Ponto2D:
    if(not self.componentes):
      
      return Ponto2D()
    
    return Ponto2D()
  
  def momento(self):
    return 0.0, 0.0