nombre = input("Ingrese su nombre: ")  # pido el nombre al usuario
edad = int(
    input("Ingrese su edad: ")
)  # pido su edad y convierto el string a un integer

if 15 <= edad <= 20:  # se verifica si la edad está en el rango de 15 a 20 años
    print(
        f"{nombre}, Bienvenido a este programa pensado solo para personas de 15 a 20 años!"  # imprime el mensaje que quiero para este programa.
    )
else:
    print("lamentablemente no puedes ingresar :( ")
