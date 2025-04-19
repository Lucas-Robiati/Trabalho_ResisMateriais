from .Forma import Forma
from .Ponto2D import Ponto2D

class Triangulo(Forma):
  def __init__(self, lado1:float = 0.0, lado2:float = 0.0, lado3:float = 0.0, origem:Ponto2D = Ponto2D(), centroide:Ponto2D = Ponto2D(), forma_virtual:bool = False):
    super().__init__(origem, centroide, forma_virtual)
    self.lado1 = lado1
    self.lado2 = lado2
    self.lado3 = lado3
    