equipos =[]
def agregar():
    nombre=input('NAME TEAM:')
    ciudad=input('NAME CITY:')

    equipo ={
        'nombre': nombre,
        'ciudad': ciudad
    }
    equipos.append(equipo)


def actualiar():
    buscar = input('Ingresa el nombre')
    for e in equipos:
        if e['nombre'] == buscar:
            print(f'Se encontro {e}')
            nuevo_nomb = input('NOMBRE NEW: ')
            nuevo_city = input('CITY')
            if nuevo_nomb:
               e['nombre']= nuevo_nomb
            if nuevo_city:
                e['ciudad']= nuevo_city
            print('producto actualiado')
def leer():
    if not equipos:
        print('NO HAY EQUIPOS')
        return
    print(f'{"nombre":<15}{"ciudad":<15}'.title())
    for e in equipos:
     print(f'{e["nombre"]:<15}{e["ciudad"]:<15}'.title())

def eliminar():
    for e in equipos:
        buscar = input('Ingresa nombre: ')
        if e['nombre'] == buscar:
           print(f" SE ENCONTRO {e}")
        respuesta = input('DESEA ELIMINARLO SI/ NO: ')
        if respuesta == 'si':
                equipos.remove(e)
        if respuesta == 'no':
              print('Operación cancelada')
    


