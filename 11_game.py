import random

armas = ["piedra", "papel", "tijera"]


def solicitar_datos():
    usuario = input("Escriba con que va a jugar: ")
    option_pc = random.randint(1, len(armas))

    for arma in armas:
        if arma == usuario.lower():
            option_pc = armas[option_pc - 1]
            return usuario.lower(), option_pc

    else:
        raise "Opción invalida, intente de nuevo"


def juego():
    print(":::::::::::::::Piedra Papel o Tijera:::::::::::::::\n")

    numero_victorias = None
    while numero_victorias is None:
        try:
            entrada = input("Escriba el numero de juegos: ")
            numero_victorias = int(entrada)
            if numero_victorias <= 0:
                print("Debe ser un número mayor que 0.")
                numero_victorias = None
            else:
                print(f"Que gane el mejor de {numero_victorias} juegos.")
        except ValueError:
            print("Intente de nuevo. Debe ingresar un número válido.")

    name_user = input("Nombre: ")

    victorias_user = 0
    victorias_pc = 0
    rounds = 0
    while True:
        try:
            resultado = solicitar_datos()
            print(resultado)
            match resultado:
                case ("piedra", "piedra") | ("papel", "papel") | ("tijera", "tijera"):
                    print("Empate")
                    rounds += 1
                case ("piedra", "tijera") | ("papel", "piedra") | ("tijera", "papel"):
                    print("Usuario Gana.")
                    victorias_user += 1
                    rounds += 1
                    if victorias_user > numero_victorias:
                        print(f"Felicidades el usuario {name_user} a ganado.")
                        break
                case _:
                    print("La computadora Gana")
                    victorias_pc += 1
                    rounds += 1
                    if victorias_pc > numero_victorias:
                        print("La computadora te ha derrotado.")
                        break
            print(
                f"Rounds: {rounds}, Victorias de {name_user}: {victorias_user}, Victorias PC: {victorias_pc}, "
            )

        except Exception as e:
            print(e)


juego()
