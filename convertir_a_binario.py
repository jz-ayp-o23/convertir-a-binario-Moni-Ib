"""
Inserta el encabezado aquí y escribe tu código abajo
"""
#Declaraciones
binario = ""

#Entradas
entrada = int(input("Introduzca un número: "))

# Proceso
while entrada > 0:
    residuo = entrada % 2
    binario = str(residuo) + binario
    entrada = entrada // 2

# Salida
print(f"El número en binario es: {binario}")