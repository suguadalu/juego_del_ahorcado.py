import random
intentos0 = '''
      +---+
      |   |
          |
          |
          |
          |
    ========= '''
intentos1=    '''
        +---+
      |   |
      O   |
          |
          |
          |
    ========='''
intentos2=    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    ========='''
intentos3=   '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    ========='''
intentos4=    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
     ========'''
intentos5=    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    ========='''
intentos6=    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========='''

letras_erroneas = ""
letras = ""
palabras = ["juguete", "limpieza", "recreo", "almanaque", "voraz", "capacitado", "recepcion"]
intentos = 0

def comenzar():
    palabra_aleatoria = random.choice(palabras)    
    
    
    print(f"La palabara secreta  contiene {len(palabra_aleatoria)} letras")
#    print(mostrar_palabra(palabra_aleatoria,letras_adivinadas))
    
    return palabra_aleatoria
# Esta Función sirve para mostrar la palabra oculta con las letras adivinadas
def mostrar_palabra(palabra, letras_adivinadas):
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    return palabra_mostrada


def juego_ahorcado(palabra_escondida):
    print(mostrar_palabra(palabra_escondida,letras_adivinadas))    
    intentos = 6
    print()
    while True:
        letra = input("Por favor, ingresa una sola letra:\n->").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print()
            print("Por favor, ingresa una sola letra.")
            continue

        if (letra in letras_adivinadas) or (letra in letras_erroneas):
            print()
            print("Esa letra ya la has elegido antes, por favor elige otra letra.")
            continue
           
        if letra in palabra_escondida:
            print("¡Excelente! La letra está en la palabra secreta.")
            letras_adivinadas.append(letra)
        else:
            print("Incorrecto, la letra no está en la palabra secreta.")
            intentos -= 1
            letras_erroneas.append(letra) 
            print()
            print(f"¡Cuidado! te quedan {intentos} intentos")
            # mostrar_ahorcado(intentos)

        palabra_mostrada = mostrar_palabra(palabra_escondida, letras_adivinadas)
        print(palabra_mostrada)
        
        if palabra_mostrada.replace(" ", "") == palabra_escondida:
            break
        if intentos == 0:

            break

    return intentos

if intentos == 0:
    print (intentos0)
elif intentos ==1:
    print (intentos1)
elif intentos ==2:
    print (intentos2)
elif intentos ==3:
    print (intentos3)
elif intentos ==4:
    print (intentos4)
elif intentos ==5:
    print (intentos5)
else:
    print (intentos6)    


if letras not in palabras:
    intentos+=1
        


    

# Esta Función  muestra el resultado  del juego
def final(exito):
    if exito > 0:
        print("¡Te Felicito, ganaste el juego!: '" + palabra_escondida + "'")
    else:
        print("Has perdido el juego, no te queda mas intentos. La palabra secreta era: '" + palabra_escondida + "'")

    print("Letras adivinadas: ", letras_adivinadas)
    print(f"Letras erroneas: {letras_erroneas}")


letras_adivinadas = []
letras_erroneas = []
palabra_escondida = comenzar()
exito = juego_ahorcado(palabra_escondida)
final(exito)

