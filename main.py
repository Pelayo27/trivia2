# ********************CULTURA GENERAL *****************
import time
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

print('****************' + RED + 'TRIVIA DE CULTURA GENERAL' + RESET +
      '*************\n')
print('Bievenidos a mi trivia sobre CULTURA GENERAL DEL PERÚ')
print('Podremos a prueba tus conocimientos \n')

name = input('Ingrese tu nombre: ')
print(
    f" \nHola, {name}, reponde las sigientes preguntas, escribiendo la letra de la alternativa y presione Enter para enviar tu respuesta!...."
)
questions = {
    1:
    '¿Cuál es el nombre oficial del país? \na) Estados peruanos\nb) República del Perú \nc) Reino del Perú\nd) Estado del Perú',
    2:
    '¿Contra cuál país se enfrentó Perú en la Guerra del Pacífico? \na) Bolivia\nb) Argentina \nc) Ecuador \nd) Chile',
    3:
    '¿Cuál es la moneda oficial? \na) Sol\nb) Peso \nc) Dólar\nd) Inti',
    4:
    '¿En cuántos departamento se divide el país ? \na) 22\nb) 24 \nc) 26\nd) 25',
    5:
    '¿Quién fue el último soberano inca? \na) Atahualpa\nb) Huayna Cápac \nc) Huáscar\nd) Huiracoch',
    6:
    '¿Cuál científico peruano fue un pionero de la astronáutica y de la era espacial? \na) Pedro Paulet\nb) Antúnez de Mayolo \nc) Daniel Carrión\nd) Federico Villareal',
    7:
    '¿Cuándo salió a la venta El Diario de Lima? \na) 1815\nb) 1839 \nc) 1790\nd) 1707',
    8:
    '¿Cuándo se celebra el Día de la Bandera? \na) 28 de julio\nb) 7 julio \nc) 1 de mayo\nd) 9 de junio',
    9:
    '¿Cuál río se forma por la confluencia del río Marañón y el río Ucayali? \na) Cauca\nb) Paraná \nc) Orinoco\nd) Amazonas'
}
answers = ['b', 'd', 'a', 'b', 'a', 'a', 'c', 'b', 'd']


def mostrarPreguntas(val):
    pregunta = questions[val].split('\n')
    for i in range(len(pregunta)):
        print(pregunta[i])


def seleccionarRespuesta(r):
    answer = input('Elige tu respueta: ')
    if answer in ('a', 'b', 'c', 'd'):
        if answer == answers[r]:
            rep = {'success': 'Tu respuesta es correcta, Feliciadades'}
        else:
            rep = {'incorrect': 'Oups, Respuesta Incorrecta!'}

    else:
        rep = {'error': 'La opción eligido no es correcto'}
    return rep


y = 0
puntaje = 0
descuento = 0
input('Enter para continuar')
try:
    while y < len(questions):
        print(BLUE)
        mostrarPreguntas(y + 1)
        print('')
        print(RESET)
        select = seleccionarRespuesta(y)
        if select.get('success') or select.get('incorrect'):
            if select.get('success'):
                print(GREEN +select['success'])
                puntaje += 5
            else:
                print(RED+select['incorrect']+RESET)
                descuento += 1
            y += 1
        else:
            print(select['error'])
            print('\n')
            y = y
        print(f" {GREEN}Puntaje obtenido hasta el momento: {puntaje}")
        print(f" {RED}Puntaje en contra: -{descuento}\n {RESET}")
        time.sleep(2)
except:
    print(RED + 'Pasó un error inesperado')

print(f" {CYAN} Puntaje obtenido: {(puntaje-descuento)}")
print(f"Respuesta incorrectas: {descuento}")
