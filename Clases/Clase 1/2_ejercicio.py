def solicitar_num_flotante():
    numero = input ("ingrese su numero flotante")
    numero = float(numero)
    return numero

resultado = solicitar_num_flotante()
print(f"El numero que se ingreso fue: {resultado}")