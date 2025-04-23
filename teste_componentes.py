from Formas import Ponto2D
from Formas import Forma
from Formas import Retangulo
from Formas import Triangulo
from Formas import Circulo
from Objeto import AreaComposta


"""
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

"""

"""
#teste figura 1 resultado esperado x =2.25 y=3.25 ix=203.58 iy=105.58
ret1 = Retangulo("Retangulo1", 2, 9, Ponto2D(0.0,0.0), Ponto2D(1.0,4.5), False)
ret2 = Retangulo("Retangulo2", 5, 2, Ponto2D(2,0.0), Ponto2D(4.5,1.0), False)

Ac = AreaComposta()
Ac.append(ret1)
Ac.append(ret2)

print(Ac.area)
print(Ac.centroide.x)
print(Ac.centroide.y)
print(Ac.Ix)
print(Ac.Iy)
"""


"""
cir = Circulo("circulo",5,Ponto2D(2.5,2.5), Ponto2D(2.5,2.5), False)
cir2 = Circulo("circulo",4,Ponto2D(2.5,2.5), Ponto2D(2.5,2.5), True)

Ac = AreaComposta()
Ac.append(cir)
Ac.append(cir2)
print("circulo1")
print(cir.area)
print(cir.Ix)
print(cir.Iy)
print("circulo2")
print(cir2.area)
print(cir2.Ix)
print(cir2.Iy)

print("geral")
print(Ac.area)
print(Ac.centroide.x)
print(Ac.centroide.y)
print(Ac.Ix)
print(Ac.Iy)
"""


Ac = AreaComposta()
Ac.append(Circulo("",2.5,Ponto2D(5,7.5),Ponto2D(5,7.5),True))
Ac.append(Retangulo("", 1, 1.5))
print(Ac.area)
print(Ac.centroide.x)
print(Ac.centroide.y)
print(Ac.Ix)
print(Ac.Iy)