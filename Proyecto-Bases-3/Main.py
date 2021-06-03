'''
Proyecto 2
Bases de Datos
Iniversidad del Valle de Guatemala 

Juan Marroquin 19845
Javier Cotto
Javier Hernadez
'''

import psycopg2 as pg
import login as log
import Reproductor as rp
from urllib.parse import urlparse

#result = urlparse("postgres://mboqptna:ywBdzyA5jXnJ1Wxyq1MpxqB1h2kU8_ii@queenie.db.elephantsql.com:5432/mboqptna")
## also in python 3+ use: urlparse("YourUrl") not urlparse.urlparse("YourUrl") 
#username = result.username
#password = result.password
#database = result.path[1:]
#hostname = result.hostname
#port = result.port
#
#
##creamos una conexion a la base de datos
#conexion = pg.connect(host=hostname, database=database, user=username, password=password)
## Creamos el cursor con el objeto conexion
#cur = conexion.cursor()

kill = False
while kill != True:
    print("Bienvenido a tu servicio de musica\n")
    print("A continuacion escoge una opcion:")
    print("   1) Iniciar Sesion")
    print("   2) Crear un Usuario")
    print("   3) Salir")
    opcion = input()
    if opcion == "1":
        user = input("Ingresa tu nombre de Ususario:  ")
        contra = input("Ingresa tu contraseña:  ")
        print("")
        #se pide la informacion al usuario, y se checkea con esta funcion
        LogCheck=log.login(user,contra)
        if LogCheck == True:
            #si el login es valido, nos dirigimos a la seccion de reproduccion y configuracion
            rp.Funcion_Reproductor(user)
        if LogCheck == False:
            print("f)")
    if opcion == "2":
        print("Creando Usuario")
        user1 = input("Ingresa tu nombre de Usuario:  ")
        contra1 = input("Ingresa tu contraseña:  ")
        log.create(user1,contra1)
    if opcion == "3":
        kill = True
        
#conexion.close()