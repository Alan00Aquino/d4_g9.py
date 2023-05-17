from os import system
system ('cls')



lista_inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
                   {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
                   {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
                   {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
                   {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]


'''Agregar, editar y eliminar inmuebles a la lista.
Las funciones deben ajustarse al formato de lista y reglas de validación'''
def editar_inmuble(inmueble):
        inmueble_editado = lista_inmuebles[inmueble]
        disponible_editado = input('Disponible: ')
        disponible_editado['Disponible'] = disponible_editado






while True:
        '''Menú'''
        print('Bienvenido a la gestion de inmuebles')
        print('1. Lista de Inmuebles')
        print('2. Editar un Inmueble')
        print('3. Agregar un Inmueble')

        opcion = int(input('Ingrese una opcion: '))
        if opcion == 1:
                system('cls')
                print('Lista de Inmuebles')
                for i in lista_inmuebles:
                        print(f'-{i}')
                input('presione enter para volver al menú principal')
                system('cls')       
        
        elif opcion == 2:
                system('cls')
                print('lista de inmuebles')
                
                for y in lista_inmuebles:
                        print(y)

'''Agregen su nombre'''
#Integrantes:
#Aquino Alan Mauricio Sebastian
