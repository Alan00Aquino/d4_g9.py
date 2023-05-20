from os import system
import time

lista_inmuebles = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]

def validar_inmueble(**nuevo_inmueble):
    if (
        nuevo_inmueble['zona'] in ['A', 'B', 'C'] and
        nuevo_inmueble['estado'] in ['Disponible', 'Reservado', 'Vendido'] and
        nuevo_inmueble['año'] >= 2000 and
        nuevo_inmueble['metros'] >= 60 and
        nuevo_inmueble['habitaciones'] >= 2
    ):
        return True
    else:
        False

def agregar_inmueble(lista_inmuebles, nuevo_inmueble):
    if validar_inmueble(**nuevo_inmueble):
        lista_inmuebles.append(nuevo_inmueble)
        system('cls')
        print("El inmueble ha sido agregado correctamente.")
        time.sleep(4)
        system('cls')
    else:
        system('cls')
        print("El inmueble no cumple con las reglas de validación.")
        time.sleep(4)
        system('cls')

def editar_inmueble(inmueble_edit, inmueble):
    print('Estado actual')
    print(inmueble_edit)
    inmueble_edit['año'] = int(input('Año: '))
    inmueble_edit['metros'] = int(input('Metros: '))
    inmueble_edit['habitaciones'] = int(input('Habitaciones: '))
    inmueble_edit['garaje'] = input('Garaje (Sí/No): ').lower() == 'sí'
    inmueble_edit['zona'] = input('Zona (A/B/C): ').upper()
    inmueble_edit['estado'] = input('Estado (Disponible/Reservado/Vendido): ').capitalize()
    system('cls')
    print('Cambio realizado')
    print(inmueble_edit)
    input('Presione intro para guardar los cambios')
    lista_inmuebles[inmueble - 1] = inmueble_edit
    system('cls')
    print('\"Los cambios fueron guardados exitosamente\"')
    time.sleep(4)
    system('cls')

def cambio_estado(inmueble,inm_cambio_estado):
    print('Estado actual')
    print(inm_cambio_estado)
    inm_cambio_estado['estado'] = input('Estado (Disponible/Reservado/Vendido): ').capitalize()
    system('cls')
    print('Cambio realizado')
    print(inm_cambio_estado)
    input('Presione intro para guardar los cambios')
    system('cls')
    lista_inmuebles[inmueble - 1] = inm_cambio_estado
    print('\"El estado fue cambiado exitosamente\"')
    time.sleep(4)
    system('cls')


def mostrar_inmuebles(lista, precio=False):
    i = 1
    for inmueble in lista:
        print(f'inmueble {i}: ')
        print('Año:', inmueble['año'])
        print('Metros:', inmueble['metros'])
        print('Habitaciones: ', inmueble['habitaciones'])
        print('Garaje:', 'Sí' if inmueble['garaje'] else 'No')
        print('Zona:', inmueble['zona'])
        print('Estado:', inmueble['estado'])
        if precio:
            print('Precio: $',inmueble['precio'])
        print('')
        print('***********************')
        print('')
        i += 1
    input('Precione enter para salir')

def inmueble_presupuesto(lista):
    system('cls')
    presupuesto = float(input('Ingrese el presupuesto máximo: $'))
    system('cls')
    print(f'Lista de Inmuebles segun presupuesto ${presupuesto}')
    print('')
    inmuebles_segun_presupuesto = []

    for inmueble in lista:
        precio = calcular_precio(inmueble)
        if precio <= presupuesto and inmueble['estado'] in ['Reservado', 'Disponible', 'Vendido']:
            inmueble_precio = inmueble.copy()
            inmueble_precio['precio'] = precio
            inmuebles_segun_presupuesto.append(inmueble_precio)

    mostrar_inmuebles(inmuebles_segun_presupuesto, True)
    return inmuebles_segun_presupuesto


def calcular_precio(inmueble):
    zona = inmueble['zona']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = inmueble['garaje']
    antiguedad = 2023 - inmueble['año']

    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 +
                  garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 +
                  garaje * 1500) * (1 - antiguedad / 100) * 1.5
    elif zona == 'C':
        precio = (metros * 100 + habitaciones * 500 +
                  garaje * 1500) * (1 - antiguedad / 100) * 2

    return precio

def menú():
    while True:
        system('cls')
        print('Bienvenido a la gestión de inmuebles')
        print('1. Lista de Inmuebles')
        print('2. Editar un Inmueble')
        print('3. Agregar un Inmueble')
        print('4. Eliminar un Inmueble')
        print('5. Cambiar el estado de un Inmueble')
        print('6. Realizar presupuesto')
        print('7. Salir')

        opcion = int(input('Ingrese una opción: '))

        if opcion == 1:
            system('cls')
            print('Lista de Inmuebles')
            for inc, inm in enumerate(lista_inmuebles):
                inc += 1
                print(f'{inc}. {inm}')
            input('Presione enter para volver al menú principal')
            system('cls')
        
        elif opcion == 2:
            system('cls')
            print('Lista de inmuebles')
            inc = 1
            for inc, inm in enumerate(lista_inmuebles):
                inc += 1
                print(f'{inc}. {inm}')
            inmueble = int(input('Ingrese la opción del inmueble a editar: '))
            
            if inmueble < 1 or inmueble > len(lista_inmuebles):
                system('cls')
                print('\"La opción ingresada no se encuentra en la lista\"')
                time.sleep(4)
                system('cls')
            else:
                inmueble_edit = lista_inmuebles[inmueble - 1]
                system('cls')
                editar_inmueble(inmueble_edit, inmueble)
                
        elif opcion == 3:
            system('cls')
            print('Complete los datos del inmueble nuevo')
            nuevo_inmueble = {}
            nuevo_inmueble['año'] = int(input('Año: '))
            nuevo_inmueble['metros'] = int(input('Metros: '))
            nuevo_inmueble['habitaciones'] = int(input('Habitaciones: '))
            nuevo_inmueble['garaje'] = input('Garaje (Sí/No): ').lower() == 'sí'
            nuevo_inmueble['zona'] = input('Zona (A/B/C): ').upper()
            nuevo_inmueble['estado'] = input('Estado (Disponible/Reservado/Vendido): ').capitalize()
            agregar_inmueble(lista_inmuebles, nuevo_inmueble)
        
        elif opcion == 5:
            system('cls')
            print('Lista de inmuebles')
            inc = 1
            for inc, inm in enumerate(lista_inmuebles):
                inc += 1
                print(f'{inc}. {inm}')
            inmueble = int(input('Ingrese la opción del inmueble que desea cambiar su estado: '))
            
            if inmueble < 1 or inmueble > len(lista_inmuebles):
                system('cls')
                print('\"La opción ingresada no se encuentra en la lista\"')
                time.sleep(4)
                system('cls')
            else:
                inm_cambio_estado = lista_inmuebles[inmueble - 1]
                system('cls')
                cambio_estado(inmueble,inm_cambio_estado)

        elif opcion == 6:
            inmueble_presupuesto(lista_inmuebles)    


        elif opcion == 7:
            system('cls')
            break

menú()

#Integrantes:
#Aquino Alan Mauricio Sebastian
#Leonel Risso Patrón
#Innocente Iván