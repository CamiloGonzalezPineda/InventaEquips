from app import menu
import csv
print('-------------------BIENVENIDO---------------------------')
ARCHIVO = 'usuario.csv'
intentos = 0
logeado = False
while intentos < 3 and not logeado:
    usuario = input('USUARI: ')
    pasword = input('PASWOR: ')
    intentos+=1

    with open(ARCHIVO, 'r', newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f)

            for use in lector:
                if use['USUARI'] == usuario and  use['PASWORD']== pasword:
                    print('WELCOME')
                    menu()
                    logeado = True
                    break
            else:
             print('TRY AGAIN')    

if intentos == 3:
    print('Demasiados intentos putos')





