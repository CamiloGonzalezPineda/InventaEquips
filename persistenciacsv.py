import csv



ARCHIVO = 'usuario.csv'

def guardar(lista):
    with open(ARCHIVO, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f,fieldnames=["USUARI","PASWORD"] )
        escritor.writeheader()
        escritor.writerows(lista)
        print(f'INVENTARIO GUARDADO EN LA RUTA: {ARCHIVO}')

lista = [
    {'USUARI' :'camilo', 'PASWORD' : '12345'},
    {'USUARI' : 'maria', 'PASWORD' :'hola'},
    {'USUARI' : 'andres', 'PASWORD' :'1234'},
    {'USUARI' : 'juanes', 'PASWORD' :'holi'}
    ]
guardar(lista)



