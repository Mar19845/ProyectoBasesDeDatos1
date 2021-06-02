import psycopg2 as pg
from urllib.parse import urlparse

import admin as ad

result = urlparse("postgres://mboqptna:ywBdzyA5jXnJ1Wxyq1MpxqB1h2kU8_ii@queenie.db.elephantsql.com:5432/mboqptna")
# also in python 3+ use: urlparse("YourUrl") not urlparse.urlparse("YourUrl") 
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
port = result.port

#creamos una conexion a la base de datos
conexion = pg.connect(host=hostname, database=database, user=username, password=password)
# Creamos el cursor con el objeto conexion
cur = conexion.cursor()

def Funcion_Settings(user):
    op_settings = 0
    tipo_admin = ad.Checkadmin(user)
    if(tipo_admin == 1):
        ad.Admin_1(user)
    if(tipo_admin == 2):
        ad.Admin_2(user)
    if(tipo_admin == 3):
        ad.Admin_3(user)
    if(tipo_admin == 0):
        ad.Admin(user)
    if(tipo_admin == "Not_Admin"):
        ad.User_Normal(user)
        
    
    
def Funcion_Reproductor(user):
    op_repro=0
    consulta=[1,2,3]
    cont = 0
    while(op_repro != len(consulta)+2):
        cur.execute("SELECT id, cancion FROM canciones WHERE activa = 'true' ")
        consulta = cur.fetchall()
        print("---------------REPRODUCTOR---------------")
        for cancion in consulta:
            cont = cont + 1 
            print(cont, cancion[0], cancion[1])
        print(cont + 1, "Configuración")
        print(cont + 2, "Log Out")
        print("------------PLAYING RIGHT NOW------------")
        cur.execute("SELECT cancion FROM canciones where id='%s';" % (op_repro))
        print("------------" + str(cur.fetchall()) + "---------")
        op_repro = int(input("Qué otra canción quiere reproducir? o quiere dirigirse a Configuración?\t"))
        cont = 0
        
        if(op_repro == len(consulta)+1):
            Funcion_Settings(user)
            
        if(op_repro == len(consulta)+2):
            print("Salir")


