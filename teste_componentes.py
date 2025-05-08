from Forms import ICPoint2D
from Forms import ICForm
from Forms import ICRectangle
from Forms import ICTriangle
from Forms import ICCircle
from Object import ICCompositeFigure


'''
ret = ICRectangle("Retangulo1", 10, 10, ICPoint2D(-5,-5), ICPoint2D(1,1), False)
# tri = Triangulo()
cir = ICCircle("Circulo1", 0.5, ICPoint2D(0,0), ICPoint2D(0,0), True)

Ac = ICCompositeFigure()
Ac.append(ret)
Ac.append(cir)

print("objetos")
for form in Ac.components:
  print(f"tipo: {type(form)} nome: {form.nome}")


print(f"Area Total: {Ac.area}")

print(f"removendo {ret.nome}")
Ac.drop(ret)


for form in Ac.componentes:
  print(f"tipo: {type(form)} nome: {form.nome}")

print(f"nova area total: {Ac.area}")




#teste figura 1 resultado esperado x =2.25 y=3.25 ix=203.58 iy=105.58
ret1 = ICRectangle("ICRectangle1", 2, 9, ICPoint2D(0.0,0.0), ICPoint2D(1.0,4.5), False)
ret2 = ICRectangle("ICRectangle2", 5, 2, ICPoint2D(2,0.0), ICPoint2D(4.5,1.0), False)

Ac = ICCompositeFigure()
Ac.append(ret1)
Ac.append(ret2)

print(Ac.area)
print(Ac.centroid.x)
print(Ac.centroid.y)
print(Ac.Ix)
print(Ac.Iy)



cir = ICCircle("circulo",5,ICPoint2D(2.5,2.5), ICPoint2D(2.5,2.5), False)
cir2 = ICCircle("circulo",4,ICPoint2D(2.5,2.5), ICPoint2D(2.5,2.5), True)

Ac = ICCompositeFigure()
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
print(Ac.centroid.x)
print(Ac.centroid.y)
print(Ac.Ix)
print(Ac.Iy)


Ac = ICCompositeFigure()
Ac.append(ICCircle(25,ICPoint2D(50,75),True))
Ac.append(ICRectangle(100, 150, ICPoint2D(50,75), False))
print(f"momento x circulo {Ac.componentes[0].Ix}")
print(f"momento y circulo {Ac.componentes[0].Iy}")
print(f"momento x retangulo {Ac.componentes[1].Ix}")
print(f"momento y retangulo {Ac.componentes[1].Iy}")
print(f"area total {Ac.area}")
print(f"centroid geral x {Ac.centroid.x}")
print(f"centroid geral y {Ac.centroid.y}")
print(f"momento geral x {Ac.Ix}")
print(f"momento geral y {Ac.Iy}")
print(f"momento polar {Ac.Jo}")
'''


trig = ICTriangle(ICPoint2D(0,0), ICPoint2D(4,0), ICPoint2D(0,3), virtual_form=False)
trig2 = ICTriangle(ICPoint2D(0,0), ICPoint2D(-4,0), ICPoint2D(0,3), virtual_form=False)
#ret = ICRectangle(5, 2, ICPoint2D(0, 0))
# ret2 = ICRectangle(50, 30, ICPoint2D(15, 25))


ac = ICCompositeFigure()
ac.append(trig)
ac.append(trig2)
# ac.append(ret2)

print("Centroide:", ac.centroid.x, ac.centroid.y)
print("Momen. Inercia x:", ac.Ix)
print("Momen. Inercia y:", ac.Iy)

print("Prod. Inercia:", trig.Ixy)
print("Prod. Inercia:", trig2.Ixy)
print(trig.orientation)
print("Prod. Inercia:", ac.Ixy)
