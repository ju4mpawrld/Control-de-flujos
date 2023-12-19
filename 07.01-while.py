import random

numero_secreto = random.randint(1, 10)
adivinanza = 0

print("Bienvenido al juego de adivinanzas")
print("Ingresa un numero para adivinar, este está entre el 0 y 10: ")

while adivinanza != numero_secreto:
    adivinanza = int(input("Ingresa tu adivinanza: "))

    if adivinanza == numero_secreto:
        print("¡Correcto! ¡Has adivinado el número secreto!")

    elif adivinanza < numero_secreto:
        print("El número es mayor. ¡Inténtalo de nuevo!")
    else:
        print("El número es menor. ¡Inténtalo de nuevo!")
