import psycopg2 as pg
from urllib.parse import urlparse
#import Reproductor as rp

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

def Checkadmin(user):
    consulta = [1, 2, 3]
    cur.execute("SELECT administrador FROM usuario WHERE usuario = '%s';" %(user))
    consulta = cur.fetchall()
    
    if (str(consulta[0]) == "(True,)"):
        consulta1 = [1, 2, 3]
        cur.execute("select id_tipo_admin from usuario where usuario = '%s';" %(user))
        consulta1=cur.fetchall()
        #para comprobar que tipo de admin es
        if (str(consulta1[0]) == "(1,)"):
            return 1
        if (str(consulta1[0]) == "(2,)"):
            return 2
        if (str(consulta1[0]) == "(3,)"):
            return 3
        if (str(consulta1[0]) == "(0,)"):
            return 0
    if (str(consulta[0]) == "(False,)"):
        return "Not_Admin"
        
def Admin_1(user):
    print("Soy un admin tipo 1")
    
def Admin_2(user):
    print("Soy un admin tipo 2")
    
def Admin_3(user):
    print("Soy un admin tipo 3")
    
def Admin(user):
    op_settings = 0
    while(op_settings != 10):
            print("--------------CONFIGURACIÓN--------------")
            print("1. Suscribirse\n")
            print("2. Ser Artista\n")
            print("3. Ser Manager\n")
            print("4. Inactivar\n")
            print("5. Modificar\n")
            print("6. Eliminar\n")
            print("7. Subir Canción\n")
            print("8. Crear Usuario Monitor\n")
            print("9. Reporte\n")
            print("10. Reproductor")
            op_settings = int(input("Ingrese opción a realizar\t"))
            
            if (op_settings == 1):
                cur.execute("UPDATE usuario SET suscripcion='true' WHERE usuario = '%s';" % (user))
                conexion.commit()
                
            elif (op_settings == 2):
                nom = input("Ingrese nombre artistico: ")
                cur.execute("INSERT INTO artistas values ('%s', '%s');" % (nom, user))
                conexion.commit()
                
            elif (op_settings == 3):
                nom = input("Ingrese nombre de Manager: ")
                nom2 = input("De que artista sera Manager? ")
                cur.execute("INSERT INTO managers values ('%s', '%s');" % (nom, nom2))
                conexion.commit()
                
            elif (op_settings == 4):
                print("1. Inactivar Usuario")
                print("2. Inactivar Album")
                print("3. Inactivar Cancion")
                
                ina = int(input("Qué desea inactivar? \t"))
                
                if (ina == 1):
                    usu = input("Que usuario desea desactivar? \t")
                    cur.execute("UPDATE usuario SET activado='false' WHERE usuario = '%s';" % (usu))
                    conexion.commit()
                    
                elif (ina == 2):
                    alb = input("Que album desea desactivar? \t")
                    cur.execute("UPDATE albumes SET activo='false' WHERE nombre = '%s';" % (alb))
                    conexion.commit()
                    
                elif (ina == 3):
                    can = input("Que cancion desea desactivar? \t")
                    cur.execute("UPDATE canciones SET activa='false' WHERE cancion = '%s';" % (can))
                    conexion.commit()
                
            elif (op_settings == 5):
                print("1. Modificar cancion")
                print("2. Modificar album")
                
                mod = int(input("Qué desea modificar? \t"))
                
                if (mod == 1):
                    can = input("Que cancion desea modificar? \t")
                    nom = input("Nombre de la cancion: \t")
                    link = input("Adjunte link de la canción: \t")
                    artista = input("Ingrese artista principal: \t")
                    act = input("Indique el estado de la canción(activada, desactivada): \t")
                    
                    cur.execute("UPDATE canciones SET cancion = '%s', link = '%s', artista = '%s', activa = '%s' WHERE cancion = '%s';" % (nom, link, artista, act, can))
                    conexion.commit()
                    
                elif (ina == 2):
                    alb = input("Que album desea modificarr? \t")
                    cur.execute("UPDATE albumes SET activo='false' WHERE nombre = '%s';" % (alb))
                    conexion.commit()
                
            elif (op_settings == 6):
                print("Consulta")
                
            elif (op_settings == 7):
                print("Consulta")
                
            elif (op_settings == 8):
                print("Consulta")
                
            elif (op_settings == 9):
                print("Consulta")
                
            elif (op_settings == 10):
                pass  
    
def User_Normal(user):
    op_settings = 0
    while(op_settings != 4):
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
                pass
                
            