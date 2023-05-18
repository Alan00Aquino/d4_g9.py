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
    print(inmueble_edit)
    inmueble_edit['año'] = input('año: ')
    inmueble_edit['metros'] = input('metros: ')
    inmueble_edit['habitaciones'] = input('habitaciones: ')
    inmueble_edit['garaje'] = input('garaje: ')
    inmueble_edit['zona'] = input('zona: ')
    inmueble_edit['estado'] = input('estado: ')
    print(inmueble_edit)
    input('Presione intro para guardar los cambios')
    lista_inmuebles[inmueble - 1] = inmueble_edit
    system('cls')
    print('\"Los cambios fueron guardados exitosamente\"')
    time.sleep(4)
    system('cls')

def menú():
    while True:
        print('Bienvenido a la gestión de inmuebles')
        print('1. Lista de Inmuebles')
        print('2. Editar un Inmueble')
        print('3. Agregar un Inmueble')
        print('4. Realizar presupuesto')
        print('6. Salir')

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
                print('\"La opción ingresada es inválida\"')
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
            
        elif opcion == 6:
            break

menú()

#Integrantes:
#Aquino Alan Mauricio Sebastian
