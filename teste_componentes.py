from Formas import Ponto2D
from Formas import Forma
from Formas import Retangulo
from Formas import Triangulo
from Formas import Circulo
from Objeto import AreaComposta

ret = Retangulo("Retangulo1", 10, 10, Ponto2D(-5,-5), Ponto2D(1,1), False)
# tri = Triangulo()
cir = Circulo("Circulo1", 0.5, Ponto2D(0,0), Ponto2D(0,0), True)

Ac = AreaComposta()
Ac.append(ret)
Ac.append(cir)

print("objetos")
for forma in Ac.componentes:
  print(f"tipo: {type(forma)} nome: {forma.nome}")


print(f"Area Total: {Ac.area}")

print(f"removendo {ret.nome}")
Ac.drop(ret)


for forma in Ac.componentes:
  print(f"tipo: {type(forma)} nome: {forma.nome}")

print(f"nova area total: {Ac.area}")

