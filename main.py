score, vidas, bonus = 0, 3, 2

nombre1 = input("\nIngrese el nombre del participante: ")
nombre1 = nombre1.lower()
nombre1 = nombre1.title()
user_redes = input("\nIngrese su usuario de Twitter o Instagram (deje en blanco para saltar): ")
user_redes = user_redes.lower()
user_redes = (f"({user_redes})")
print(user_redes)

print("\n \n *** Bienvenido al 'Preguntados' de Python,", nombre1,"*** \n")

print("""El juego consiste en responder una serie de preguntas para sumar el mayor puntaje posible sin quedarse sin vidas.
Por cada respuesta correcta sumaremos puntos y por cada error, perderemos vidas. Al comenzar la partida tendremos 3 vidas.
El puntaje obtenido nos servirá para comprar nuevas vidas o 'saltadores', que nos permitirán pasar preguntas difíciles.
Para utilizar los "saltadores" simplemente tenés que contestar 'Saltar'.

¿Sencillo, no? Buenos, las preguntas no lo van a ser...\n""")

#Estadísticas
def estadisticas():
    print("\n--- Estadísticas de", nombre1)
    print("Puntaje actual: ", score)
    print("Vidas actuales: ", vidas)
    print("Saltadores disponibles: ", bonus,"\n")
    return estadisticas

def lista_de_resultados():
    import time
    anotador = ("\n" + f"{score}" + " puntos" + " - " + nombre1 + " - " + user_redes + " --- " + time.strftime("%d/%m/%y"))
    scores = open("scoreboard.txt", "a")
    scores.write(anotador)
    scores.close()

    scores = open("scoreboard.txt", "r")
    print(scores.read())
    scores.close()

inicio1 = input(str(nombre1) + " ¿Estás listo para empezar a jugar? (si/no)?: ")
inicio1 = inicio1.lower()

if inicio1 == "si" or inicio1 == "siii" or inicio1 == "se" or inicio1 == "dale" or inicio1 == "sí" or inicio1 == "s":
    print("Allá vamos... \n")
else:
    print("Contestaste", inicio1, "¿No querés empezar?")
    inicio1 = input("A ver, vamos de vuelta, ¿estás listo para empezar? (Si / Siii): ")
    inicio1 = inicio2.lower()
    if inicio1 == "si" or inicio1 == "siii" or inicio1 == "se" or inicio1 == "dale" or inicio1 == "sí":
        print("Ahora si, allá vamos... \n \n")
    else:
        print("Contestaste",inicio1,". Pero viejo, colaborá un poco, decía Si / Siii. En fin, si no querés...")
        estadisticas()
        exit()

#pregunta1
pregunta1 = input("Primera pregunta: ¿Cuál es la capital de Portugal?: ")
pregunta1 = pregunta1.lower()
pregunta1 = pregunta1.title()

print("\n Tu respuesta fue", pregunta1, "\n")

if pregunta1 == "Lisboa" or pregunta1 == "Lisbon":
    score += 1
    print("¡¡Correcto!!")
    print("Tu puntaje actual es: ", score, "\n")
    print("Empezaste de la mejor manera, pero ¿podrás seguir así? ¡Vamos a la segunda pregunta! \n")
elif pregunta1 == "Saltar":
    bonus -= 1
    print("Has utilizado un saltador. Saltadores disponibles:",bonus)
    print("Pasemos a la siguiente pregunta.")
else:
    score -= 1
    vidas -= 1
    print("Incorrecto. La Capital de Portugal es Lisboa")
    print("Perdiste una vida, actualmente te quedan",vidas,"vidas")
    print("Por otro lado, tu puntaje actual es: ", score,"\n")
    print("No es la mejor manera de empezar, pero no te preocupes, esto recién arranca. Ahora vamos a la pasemos a la segunda pregunta \n")

pregunta2 = input("Pregunta N° 2: ¿Cuál es el actual campeón de la Serie A de Italia?: ")
pregunta2 = pregunta2.lower()
pregunta2 = pregunta2.title()

print("\n Tu respuesta fue", pregunta2, "\n")

#pregunta2
if pregunta2 == "Juventus" or pregunta2 == "Juve":
    score += 1
    print("¡¡Correcto!!")
    print("Tu puntaje actual es:",score,"\n")
elif pregunta1 == "Saltar" or pregunta1 == "Saltador":
    bonus -= 1
    print("Has utilizado un saltador. Saltadores disponibles:",bonus)
    print("Pasemos a la siguiente pregunta.")
else:
    score -= 1
    print("Incorrecto. El actual campeón de la Serie A es Juventus")
    print("Perdiste una vida, actualmente te quedan",vidas,"vidas")
    print("Tu puntaje actual es: ", score,"\n")

estadisticas()

#tienda2
if score > 1:
    print("Cómo tenés",score,"puntos podés entrar a la tienda a comprar 'suministros'.")
    print("""1) Comprar una vida --- coste: 2 puntos --- constestar 1
2) Comprar un saltador --- coste: 5 puntos --- contestar 2
Salir de la tienda --- escriba cualquier cosa \n""")
    tienda2 = input("¿Qué deseas hacer hacer?: ")
    if tienda2 == "1" or tienda2 == "vida" and score >= 2:
        score -= 2
        vidas += 1
        print("Has comprado una vida.")
        print("Vidas restantes:",vidas,". Saltadores disponibles:",bonus,"Puntaje actual:",score)
        print("\n Pasemos a la siguiente pregunta...")
    elif tienda2 == "1" or tienda2 == "vida" and score < 2:
        print("No tenés suficientes puntos para esta acción")
        print("\n Pasemos a la siguiente pregunta...")
    elif tienda2 == "2" or tienda2 == "saltador" and score >= 5:
        score -= 5
        bonus += 1
        print("Has comprado un saltador.")
        print("Vidas restantes:",vidas,"\n""Saltadores disponibles:",bonus,"\n""Puntaje actual:",score)
        print("Pasemos a la siguiente pregunta...")
    elif tienda2 == "2" or tienda2 == "saltador" and score < 5:
        print("No tenés suficientes puntos para esta acción")
        print("Pasemos a la siguiente pregunta...")
    else:
        print("Bien. Pasemos a la siguiente pregunta... \n")
        
else:
    print("Siguiente pregunta...")

#pregunta3
print("""\n Pregunta N° 3: ¿En qué año Ferro ganó su último título de Primera División?
Opciones:
- 1980
- 1984
- 1995\n""")
pregunta3 = input("Respuesta: ")
pregunta3 = pregunta3.lower()
pregunta3 = pregunta3.title()
if pregunta3 == "1984" or pregunta3 == "84" or pregunta3 == "2":
    score += 1
    print("¡¡Correcto!!")
    print("Tu puntaje actual es:",score,"\n")
elif pregunta3 == "saltar":
    bonus -= 1
    print("Has utilizado un saltador. Saltadores disponibles:",bonus)
    print("Pasemos a la siguiente pregunta.")
else:
    vidas -= 1
    score -= 1
    print("Respondiste",pregunta3,". Es Incorrecto. Ferro salió campeón por última vez en 1984.")
    print("Perdiste una vida, actualmente te quedan",vidas,"vidas")
    if vidas < 0:
        print("¡Te quedaste sin vidas, perdiste! Volvé a intentarlo.")
        exit()
    else:
        print("Tu puntaje actual es: ", score,"\n")

estadisticas()

#pregunta4
print("\n Pregunta N° 4: ¿Cuántos goles convirtió Messi en toda su carrera (contando a clubes y Selección)?")
pregunta4 = input("Respuesta: ")
pregunta4 = pregunta4.lower()
if pregunta4 == "saltador" or pregunta4 == "saltar" and bonus >= 1:
    bonus -= 1
    print("Has utilizado un saltador. Saltadores restantes:",bonus)
    print("Pasemos a la siguiente pregunta.")
else: 
    print("¡¡Naaa, mira si alguien va a saber eso!!")
    print("Te hice guglear al pedo. Menos mal que no gastaste un saltador.")
    print("Pasemos a la siguiente pregunta...")

estadisticas()

lista_de_resultados()


#pregunta5
exit()