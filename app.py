# Importamos las funciones que vamos a necesitar para ejecutar el inventario
from crud import agregar,actualiar,leer,eliminar
def menu(): # Imprimos el menu 
    while True:
        print('1.REGISTER INVENTARY: ')
        print('2.UPDATE INVENTARY: ')
        print('3.LOOK INVENTARY: ')
        print('4.DELETE PRODUCT: ')
        print('5. GO OUT')
        while True:
            try:
                opcion = int(input('ENTER OPTION: '))
                break
            except ValueError:
                print('error')
        """
        Se llaman todas las funsiónes para poder
        ejecutar los procesos del inventario
        hacemos las alidaciones respectivas para evitar numeros negativos y mayores a 9
        """
        if opcion > 9 and opcion < 0:
            print('invalid option')
        elif opcion == 1:
            agregar()
        elif opcion == 2:
            actualiar()
        elif opcion == 3:
            leer()
        elif opcion == 4:
            eliminar()
        elif opcion == 5:
             print('---------HASTA LA PROXIMA--------')
             break    
        else:      
            print('OPCION NO VALIDAD')
 
if __name__ == "__main__": # Evita que se ejecute la función en otras partes del codigo cuando se es imporatada
 menu()


