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

def login(user,contra):
    cur.execute("select usuario from usuario where usuario = '%s' " % (user))
    checkUser = cur.fetchall()
    if  checkUser == []:
        print("El usuario: %s no existe\n" %(user))
        return False
    else:
        cur.execute("select usuario from usuario where usuario = '%s' and contrasenia = '%s' " % (user,contra))
        checkPass = cur.fetchall()
        if checkPass == []:
            print("Contraseña incorrecta usuario: %s \n" %(user))
            return False
        else:
            print("Bienvenido: %s\n" %(user))
            return True
    #conexion.close()

def create(user,contra):
    #cur.execute("insert into usuarios values('%s','%s','%s','%s','%s','%s')" %(user, contra, 0,"false", "false", "false"))
    checkInsert = cur.execute("insert into usuario values('%s','%s','%s','%s','%s','%s','%s')" %(user, contra, 0,"false", "false",4,"false"))
    conexion.commit()
    if checkInsert != []:
        print("Bienvenido: %s\n" %(user))
    else:
        print("Hubo un error intente de nuevo")
    #conexion.close()


