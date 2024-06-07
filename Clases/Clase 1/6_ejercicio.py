def par_impar(numero):
    if numero % 2 == 0:
        mensaje = "el numero ingresado es par"
    else :
        mensaje = "el numero ingresado es impar"
    
    return mensaje

numero = input("ingrese su numero")
numero = int(numero)
resultado = par_impar(numero)
print(f"{resultado}")