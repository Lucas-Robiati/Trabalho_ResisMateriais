from .Forma import Forma
from .Ponto2D import Ponto2D


class Retangulo(Forma):
  def __init__(self, base:float = 0.0, altura:float = 0.0, origem:Ponto2D = Ponto2D(), centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    super().__init__(origem, centroide, forma_virtual)
    self.base = base
    self.altura = altura