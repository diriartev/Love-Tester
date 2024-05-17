'''
» Date: 15/05/2024
» Version: 2.5
» Author: @diriartev

'''

import random
import time
import sys
import os
from colorama import init, Fore, Style

# Init de Colorama para que funcione
init(autoreset=True)

# Función main()
def main():
    while True:
        os.system('cls')
        print(Fore.LIGHTRED_EX + '\n—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————')
        print(Fore.LIGHTRED_EX + '\n❤️  LOVE TESTER' + Style.DIM + Fore.BLACK + ' | ' + Style.RESET_ALL + Fore.WHITE + 'Versión 2.5 ❤️' + '\n')
        print(Fore.LIGHTRED_EX + '—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n')
        print(Fore.LIGHTRED_EX + '⫸  ' + Fore.WHITE + 'Introduzca los nombres de las personas a continuación por favor:' + '\n')
        nombre1 = input(Fore.LIGHTRED_EX + '   → ' + Style.RESET_ALL + Fore.WHITE)
        nombre2 = input(Fore.LIGHTRED_EX + '   → ' + Style.RESET_ALL + Fore.WHITE)
        lovetester(nombre1 , nombre2)
        print(Fore.LIGHTRED_EX + '—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n')
        time.sleep(3)
        while True:
            print(Fore.LIGHTRED_EX + '❤️  ¿Desea realizar otro Love Test?')
            continuar = input(Fore.LIGHTRED_EX + '   → ' + Style.RESET_ALL + Fore.WHITE)
            if continuar.lower() == "si":
                break
            elif continuar.lower() == "no":
                os.system('cls')
                print(Fore.LIGHTRED_EX + '\n💫 ¡Adiós, ten un lindo día! \n')
                exit()
            else:
                print(Fore.YELLOW + '\n    ☢️  ERROR | Ingrese una respuesta de "si" o "no" por favor \n')

# Función lovetester()
def lovetester(n1 , n2):

    # Titulo ejecución programa
    print('\n' + Fore.LIGHTRED_EX + '◷  LOVE TESTER' + Style.DIM + Fore.BLACK + ' | ' + Style.RESET_ALL + Fore.WHITE + 'Calculando...' + '\n')

    # Barra de carga
    bar_length = 30
    for i in range(1, bar_length + 1):
        time.sleep(0.05) 
        progress = (i / bar_length) * 100
        bar = '❤️' * i + '-' * (bar_length - i)
        sys.stdout.write(Fore.WHITE + f'\r[{bar} ] {int(progress)}%')
        sys.stdout.flush()

    # Porcentaje random para el Love Tester
    resultado = random.randint(0, 101)

    # Listas de posibles Mensajes
    mensajes0 = [
    'El amor entre ustedes dos los persigue, pero ustedes son más rapidos' ,
    'Ehm, ¿Se los digo o mejor hacemos como que esto no pasó?' ,
    'Ehm bueno, ¿Quién tiene hambre?'
    ]
    mensajes1a29 = [
    "'No' , 'hacen' , 'linda' , 'pareja'." , 
    'Mejor ni lo intenten, quizás deberían probar con un reality show de relaciones :(' , 
    'Jajaja pobrecitos, no van a llegar ni a la esquina...'
    ]
    mensajes30a49 = [
    'Los amaban más sus ex jajaja',
    'Bueno, al menos hay salud, ¿no?',
    'Mejor queden como amigos, les irá mejor jajaja'
    ]
    mensajes50 = [
    'Ni tan mal, podría ser peor... supongo.',
    'Sapo, mejor lo dejo con la duda',
    'Ni el love test sabe decir si sí o si no JAJAJA.'
    ]
    mensajes51a79 = [
    '¡Nada mal! Tienen un buen potencial, ¿qué están esperando?',
    'El amor está en el aire... o tal vez solo son los gérmenes.',
    'No tengan miedo al éxito, solo intentenlo y veremos qué pasa...'
    ]
    mensajes80a99 = [
    '¡Wow! Eso es lo que llamo química de verdad.',
    'Solo les falta un poco más para alcanzar la perfección, ¡sigamos así!',
    'Ustedes dos son la envidia del Tinder, ¡mantengan esa llama encendida!'
    ]
    mensajes100 = [
    'Como Fiona y Shrek, esto es el amor verdadero.',
    'No necesitan un love tester para saberlo, ¡son la pareja perfecta!',
    '¿Esto es legal? ¡Tan perfectos que parecen una conspiración del destino!'
    ]

    # Mensajes según el resultado random
    if resultado == 0:
        mensaje = random.choice(mensajes0)
        print(Fore.WHITE + f'\n \n💔 ¡El amor entre {n1} y {n2} es del {resultado}%! {mensaje} \n')
    elif resultado > 0 and resultado < 30:
        mensaje = random.choice(mensajes1a29)
        print(Fore.WHITE + f'\n \n❤️‍🩹  ¡El amor entre {n1} y {n2} es del {resultado}%! {mensaje} \n')
    elif resultado >= 30 and resultado < 50:
        mensaje = random.choice(mensajes30a49)
        print(Fore.WHITE + f'\n \n💕 ¡El amor entre {n1} y {n2} es del {resultado}%! {mensaje} \n')
    elif resultado == 50:
        mensaje = random.choice(mensajes50)
        print(Fore.WHITE + f'\n \n💓 ¡El amor entre {n1} y {n2} es del {resultado}%! {mensaje} \n')
    elif resultado > 50 and resultado < 80:
        mensaje = random.choice(mensajes51a79)
        print(Fore.WHITE + f'\n \n💞 ¡El amor entre {n1} y {n2} es del {resultado}%! {mensaje} \n')
    elif resultado >= 80 and resultado < 100:
        mensaje = random.choice(mensajes80a99)
        print(Fore.WHITE + f'\n \n❤️  ¡El amor entre {n1} y {n2} es del {resultado}%! {mensaje} \n')
    elif resultado == 100:
        mensaje = random.choice(mensajes100)
        print(Fore.WHITE + f'\n \n💘 ¡El amor entre {n1} y {n2} es del {resultado}%! {mensaje} \n')
    else:
        print(Fore.RED + "     ⨻  No se supone que debas leer este mensaje, ¡Ha ocurrido un error! \n")

# Llamado a la función main() al ejecutar el programa
if __name__ == "__main__":
    main()