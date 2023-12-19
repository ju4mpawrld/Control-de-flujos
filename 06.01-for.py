numeros = [10, 7, 25, 42, 15, 30]  # hago una lista de numeros
numero_buscado = int(
    input("Ingrese un número: ")
)  # le pido al usuario que diga un numero para poder encontrarlo en base a la lista y transformar el str a int

for numeros in numeros:  # hago el bucle for
    print(
        f"{numeros}"
    )  # imprimo todos los numeros y que haga un break cuando lo encuentre.
    if numero_buscado == numeros:
        print(f"Número encontrado!: {numero_buscado}")
        break
else:
    print("no fue encontrado el número.")
