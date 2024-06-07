import math
def calcular_area(radio):
    area = math.pi * radio ** 2      
    return area

radio = 5
area = calcular_area(radio)
print(f"el area del circulo es {area} y su radio es {radio}")