"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
binario = ""
# Entradas
entrada = int(input("Introduzca un número: "))

# Proceso
for digito in entrada:
    division = entrada // 2
    cociente = division // (entrada % 2)
    cociente0 = (entrada % cociente == 0)
    binario += cociente

# Salidas
print(f"El número {entrada} en binario es {binario}")
