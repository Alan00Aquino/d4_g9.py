from os import system
import time
system ('cls')



lista_inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
                   {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
                   {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
                   {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
                   {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

def validar_inmueble(inmueble):
    if (
        inmueble['zona'] in ['A', 'B', 'C'] and
        inmueble['estado'] in ['Disponible', 'Reservado', 'Vendido'] and
        inmueble['año'] >= 2000 and
        inmueble['metros'] >= 60 and
        inmueble['habitaciones'] >= 2
    ):
        return True
    else:
        False

def agregar_inmueble(inmuebles, nuevo_inmueble):
    if validar_inmueble(nuevo_inmueble):
        inmuebles.append(nuevo_inmueble)
        print("El inmueble ha sido agregado correctamente.")
    else:
        print("El inmueble no cumple con las reglas de validación.")
    

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
                print('Bienvenido a la gestion de inmuebles')
                print('1. Lista de Inmuebles')
                print('2. Editar un Inmueble')
                print('3. Agregar un Inmueble')

                opcion = int(input('Ingrese una opcion: '))
                if opcion == 1:
                        system('cls')
                        print('Lista de Inmuebles')
                        for inc, inm in enumerate(lista_inmuebles):
                                inc += 1
                                print (f'{inc}. {inm}')
                        input('presione enter para volver al menú principal')
                        system('cls')       
        
                elif opcion == 2:
                        system('cls')
                        print('lista de inmuebles')
                        inc = 1
                        for inc, inm in enumerate(lista_inmuebles):
                                inc += 1
                                print (f'{inc}. {inm}')
                        inmueble = int(input('Ingrese la opcion del inmueble a editar: '))
                
                        if inmueble < 1 or inmueble > len(lista_inmuebles):
                                system('cls')
                                print('\"La opcion ingresada es invalida\"')
                                time.sleep(4)
                                system('cls')
                        else:
                                inmueble_edit = lista_inmuebles[inmueble - 1]
                                system('cls')
                                editar_inmueble(inmueble_edit, inmueble)


menú()


#Agregen su nombre'''
#Integrantes:
#Aquino Alan Mauricio Sebastian
