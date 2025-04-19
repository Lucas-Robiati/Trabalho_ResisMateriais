from .Forma import Forma
from .Ponto2D import Ponto2D

class Circulo(Forma):
  def __init__(self, raio:float = 0.0, origem:Ponto2D = Ponto2D(), centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    super().__init__(origem, centroide, forma_virtual)
    self.raio = raio
    