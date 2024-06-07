def calcular_potencia(base , exponente):
    resultado = 1
    while exponente > 0:
        resultado *= base
        exponente -= 1
    return resultado

base = 4
exponente = 2
resultado = calcular_potencia (base , exponente)
print(f"el resultado de {base} elevado a {exponente} es {resultado}")