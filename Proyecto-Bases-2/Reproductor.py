import psycopg2 as pg
from urllib.parse import urlparse

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
    consulta = [1, 2, 3]
    cur.execute("SELECT administrador FROM usuarios WHERE usuario = '%s';" %(user))
    consulta = cur.fetchall()
    
    if (str(consulta[0]) == "(True,)"):
        while(op_settings != 9):
            print("--------------CONFIGURACIÓN--------------")
            print("1. Suscribirse\n")
            print("2. Ser Artista\n")
            print("3. Ser Manager\n")
            print("4. Inactivar\n")
            print("5. Modificar\n")
            print("6. Eliminar\n")
            print("7. Subir Canción\n")
            print("8. Reproductor")
            op_settings = int(input("Ingrese opción a realizar\t"))
            
            if (op_settings == 1):
                print("Consulta")
                
            elif (op_settings == 2):
                print("Consulta")
                
            elif (op_settings == 3):
                print("Consulta")
                
            elif (op_settings == 4):
                print("Consulta")
                
            elif (op_settings == 5):
                print("Consulta")
                
            elif (op_settings == 6):
                print("Consulta")
                
            elif (op_settings == 7):
                print("Consulta")
                
            elif (op_settings == 8):
                Funcion_Reproductor()        
    if (str(consulta[0]) == "(False,)"):
        while(op_settings != 5):
            print("--------------CONFIGURACIÓN--------------")
            print("1. Suscribirse\n")
            print("2. Ser Artista\n")
            print("3. Ser Manager\n")
            print("4. Reproductor")
            op_settings = int(input("Ingrese opción a realizar\t"))
            
            if (op_settings == 1):
                print("Consulta")
                
            elif (op_settings == 2):
                print("Consulta")
                
            elif (op_settings == 3):
                print("Consulta")
                
            elif (op_settings == 4):
                print("Consulta")
                
            elif (op_settings == 5):
                Funcion_Reproductor() 
def Funcion_Reproductor(user):
    op_repro=0
    consulta=[1,2,3]
    cont = 0
    while(op_repro != len(consulta)+2):
        cur.execute("SELECT cancion FROM canciones")
        consulta = cur.fetchall()
        print("---------------REPRODUCTOR---------------")
        for cancion in consulta:
            cont = cont + 1 
            print(cont, cancion)
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
            print("puto")
    
