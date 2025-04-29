import random

def generar_numero_aleatorio():
    while True:
        # Generamos un número aleatorio entre 0 y 1
        numero = random.uniform(0, 1)

        # Si el número es 0 o 1, lo descartamos
        if numero != 0 and numero != 1:
            return numero

# Generar un número aleatorio entre 0 y 1 que no sea ni 0 ni 1
numero = generar_numero_aleatorio()
print(f"Número aleatorio generado: {numero}")
