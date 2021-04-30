import psycopg2 as pg

conexion = pg.connect(host="localhost", database="LAB10", user="postgres", password="J@vier5201")

# Creamos el cursor con el objeto conexion
cur = conexion.cursor()

def Funcion_Settings():
    op_settings = 0
    consulta = [1, 2, 3]
    usu = "user4"
    cur.execute("SELECT administrador FROM Usuarios WHERE usuario = '%s';" % (usu))
    consulta = cur.fetchall()
    print(consulta[0])
    
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
        
def Funcion_Reproductor():
    op_repro=0
    consulta=[1,2,3]
    while(op_repro != len(consulta)+1):
        cur.execute("SELECT cancion FROM canciones")
        consulta = cur.fetchall()
        print("---------------REPRODUCTOR---------------")
        for cancion in consulta:
            print(cancion)
        print("Configuración")
        print("------------PLAYING RIGHT NOW------------")
        cur.execute("SELECT cancion FROM canciones where id='%s';" % (op_repro))
        print("------------" + str(cur.fetchall()) + "---------")
        op_repro = int(input("Qué otra canción quiere reproducir? o quiere dirigirse a Configuración?\t"))
        
        if(op_repro == len(consulta)+1):
            Funcion_Settings()
            
        if(op_repro == len(consulta) + 2):
            break
    
Funcion_Reproductor()
conexion.close()