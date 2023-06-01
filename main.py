import random

options = ('piedra', 'papel', 'tijera')
countUserWin=0
countPcWin=0
round=1

def inputUser():
    user = input("Ya sabes jugarlo, ahora elige: piedra, papel ó tijera: ")
    user = user.lower()
    return user   

while True:
    #Visualización de los rounds
    print(f"Round: {round}")

    #Elección random de la PC
    pc = random.choice(options)

    # Entrada de la elección del user y minuscula a la elección
    user = inputUser()

    #Figth
    if user == pc:
        print(f"la pc eligió {pc}, tú elegiste {user}, esto es un ¡Empate!")
    elif ((user == "piedra" and pc == "tijera") or (user == "papel" and pc == "piedra") or (user == "tijera" and pc == "papel")):
        print(f"la pc eligió {pc}, tú elegiste {user}, ¡Felicidades, Ganaste esta ronda!")
        countUserWin+=1
    elif not user in options:
        print("Elegiste mal, recuerda que solo debes escribir la opción que deseas sin espacios, guiones, comas o cualquier caracter especial, ya sea piedra, papel o tijera")
        continue
    else:
        print(f"la pc eligió {pc}, tú elegiste {user}, El ganador es la pc")
        countPcWin+=1

    #Rounds
    round+=1

    #Contadores
    if countUserWin == 2:
        ganador = ("¡Felicidades, ganaste este juego!")
        print(f"La PC ganó: {countPcWin} veces, tú ganaste: {countUserWin} veces, ", ganador)
        break
    elif countPcWin == 2:
        ganador = ("El ganador es la PC")
        print(f"La PC ganó: {countPcWin} veces, tú ganaste: {countUserWin} veces, ", ganador)
        break

    

    

