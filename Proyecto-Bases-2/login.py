import psycopg2 as pg

#creamos una conexion a la base de datos
conexion = pg.connect(host="localhost", database="Lab11", user="postgres", password="1234")
# Creamos el cursor con el objeto conexion
cur = conexion.cursor()

def login(user,contra):
    cur.execute("SELECT * FROM PC WHERE modelo = '%s' " % (user))
    checkUser = cur.fetchall()
    if  checkUser == []:
        print("El usuario: %s no existe\n" %(user))
        return False
    else:
        cur.execute("SELECT * FROM PC WHERE modelo = '%s' " % (user))
        checkPass = cur.fetchall()
        if checkPass == []:
            print("Contraseña incorrecta usuario: %s \n" %(user))
            return False
        else:
            return True
