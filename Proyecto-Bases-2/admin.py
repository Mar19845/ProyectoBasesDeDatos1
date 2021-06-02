import psycopg2 as pg
from urllib.parse import urlparse
from pymongo import *
import random
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
    op_settings = 0
    while(op_settings != 7):
            print("--------------CONFIGURACIÓN--------------")
            print("1. Suscribirse\n")
            print("2. Ser Artista\n")
            print("3. Ser Manager\n")
            print("4. Inactivar\n")
            print("5. Modificar\n")
            print("6. Subir Canción\n")
            print("7. Reproductor")
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
                print("---Inactivar Subscripcion de Usuario---\n")
                usu = input("Que usuario desea desactivar? \t")
                cur.execute("UPDATE usuario SET suscripcion='false' WHERE usuario = '%s';" % (usu))
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
                check = ChekArtista(user)
                if(check == True):
                    nomCan = input("Ingrese nombre de la Cancion: ")
                    link = input("Ingrese link de la cancion: ")
                    nomArt = GetArtista(user)
                    activa = "true"
                    cur.execute("insert into canciones values ('%s', '%s', '%s', '%s');" % (nomCan, link,nomArt,activa))
                    conexion.commit()
                elif(check == False):
                    print("Uste no es un Artista registrado")
                
            elif (op_settings == 7):
                pass
                
    
def Admin_2(user):
    op_settings = 0
    while(op_settings != 6):
            print("--------------CONFIGURACIÓN--------------")
            print("1. Suscribirse\n")
            print("2. Ser Artista\n")
            print("3. Ser Manager\n")
            print("4. Inactivar\n")
            print("5. Subir Cancion\n")
            print("6. Reproductor")
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
                print("1. Inactivar Usuario como Artista")
                print("2. Inactivar Album")
                print("3. Inactivar Cancion")
                print("4. Eliminar usuario sin subscriocion")
                
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
                elif (ina == 4):
                    can = input("Ingrese el Nombre del Usuario \t")
                    cur.execute("delete from usuario where suscripcion ='false' and usuario ='%s';" % (can))
                    conexion.commit()
                
            
                
            elif (op_settings == 5):
                check = ChekArtista(user)
                if(check == True):
                    nomCan = input("Ingrese nombre de la Cancion: ")
                    link = input("Ingrese link de la cancion: ")
                    nomArt = GetArtista(user)
                    activa = "true"
                    cur.execute("insert into canciones values ('%s', '%s', '%s', '%s');" % (nomCan, link,nomArt,activa))
                    conexion.commit()
                elif(check == False):
                    print("Uste no es un Artista registrado")
            elif (op_settings == 6):
                pass
                
    
    
def Admin_3(user):
    op_settings = 0
    while(op_settings != 7):
            print("--------------CONFIGURACIÓN--------------")
            print("1. Suscribirse\n")
            print("2. Ser Artista\n")
            print("3. Ser Manager\n")
            print("4. Subir Canción\n")
            print("5. Crear Usuario Monitor\n")
            print("6. Generar Reportes\n")
            print("7. Reproductor")
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
                check = ChekArtista(user)
                if(check == True):
                    nomCan = input("Ingrese nombre de la Cancion: ")
                    link = input("Ingrese link de la cancion: ")
                    nomArt = GetArtista(user)
                    activa = "true"
                    cur.execute("insert into canciones values ('%s', '%s', '%s', '%s');" % (nomCan, link,nomArt,activa))
                    conexion.commit()
                elif(check == False):
                    print("Uste no es un Artista registrado")
                
            elif (op_settings == 5):
                usu = input("Escoje usuario para convertir en monitor: \t")
                moni = int(input("Qué tipo de monitor quiere que sea? \t"))
                cur.execute("UPDATE usuario SET administrador = 'true', id_tipo_admin = '%s' WHERE usuario = '%s'" % (moni, usu))
                conexion.commit()
                
            elif (op_settings == 9):
               print("----------REPORTERÍA----------")
               print("1. Albumes más recientes de la última semana")
               print("2. Artistas con popularidad creciente en los ultimos tres meses")
               print("3. Artistas con mayor produccion musical")
               print("4. Usuarios más activos en la plataforma")
               print("5. Cancion con mas reproducciones de un Artista")
               print("6. Generos mas Reproducidas entre un rango de fechas")
               print("7. Artistas mas Reproducidos en un rango de Fechas")
               print("8. Cancion con mas reproducciones de un Artista")
               
               op_report = int(input("Qué reporte quisiera ver? \t"))
               if op_report == 1:
                   cur.execute("SELECT a.nombre FROM albumes a WHERE a.fecha_salida > (SELECT CAST(NOW() AS DATE) - 7);")
                   consulta = cur.fetchall()
                   print("------ALBUMES MÁS RECIENTES DE LA ULTIMA SEMANA------")
                   for a.nombre in consulta:
                       print(a.nombre)
                        
               if op_report == 2:
                   cur.execute("SELECT al.creador, count(r) FROM album_cancion ac INNER JOIN canciones c on ac.id_cancion = c.id INNER JOIN albumes al on ac.id_album = al.nombre INNER JOIN reproducciones r on r.id_cancion = c.id WHERE r.fecha > (SELECT CAST(NOW() AS DATE) - 90) GROUP BY al.creador ORDER BY count(r) desc;")
                   consulta = cur.fetchall()
                   print("------ARTISTAS CON POPULARIDAD CRECIENTE EN LOS ULTIMOS TRES MESES------")
                   for al.creador in consulta:
                       print(al.creador, count(r))
                        
               if op_report == 3:
                   cur.execute("SELECT ar.nombre, count(r) FROM artistas ar INNER JOIN albumes al on ar.nombre = al.creador INNER JOIN canciones c on c.cancion = c.cancion INNER JOIN reproducciones r on r.id_cancion = c.id GROUP BY ar.nombre ORDER BY count(r) desc;")
                   consulta = cur.fetchall()
                   print("------ARTISTAS CON MAYOR PRODUCCION MUSICAL------")
                   for ar.nombre in consulta:
                       print(ar.nombre, count(r))
                        
               if op_report == 4:
                   cur.execute("SELECT usuario, logins FROM usuario ORDER BY logins DESC LIMIT 5;")
                   consulta = cur.fetchall()
                   print("------USUARIOS MÁS ACTIVOS EN LA PLATAFORMA------")
                   for usuario,logins in consulta:
                       print(usuario, logins)
               if op_report == 5:
                    artista = input("Ingrese el Artista")
                    cur.execute("select canciones_repro_unArtista('%s');"% (artista))
                    consulta = cur.fetchall()
                    
                    print("------Cancion con mas reproducciones------")
                    print("------"+ artista +"------")
                    for i in consulta:
                        print(i[0])
               if op_report == 6:
                   fecha1 = input("Ingrese la fecha de la forma Año-Mes-Dia")
                   fecha2 = input("Ingrese la fecha de la forma Año-Mes-Dia")
                   cur.execute("select repro_genero('%s', '%s');"% (fecha1,fecha2))
                   consulta = cur.fetchall()
                   print("------Generos repoducidos------")
                   for i in consulta:
                       print(i)
               if op_report == 7:
                   fecha1 = input("Ingrese la fecha de la forma Año-Mes-Dia")
                   fecha2 = input("Ingrese la fecha de la forma Año-Mes-Dia")
                   cur.execute("select artistas_repro('%s', '%s', 5);"% (fecha1,fecha2))
                   consulta = cur.fetchall()
                   print("------Generos repoducidos------")
                   for i in consulta:
                       print(i) 
            elif (op_settings == 7):
                pass
            
    
def Admin(user):
    op_settings = 0
    while(op_settings != 14):
            print("--------------CONFIGURACIÓN--------------")
            print("1. Suscribirse\n")
            print("2. Ser Artista\n")
            print("3. Ser Manager\n")
            print("4. Inactivar\n")
            print("5. Modificar\n")
            print("6. Eliminar suscripcion de usuario\n")
            print("7. Subir Canción\n")
            print("8. Crear Usuario Monitor\n")
            print("9. Reporte\n")
            print("10. Bitacora\n")
            print("11. Comisiones\n")
            print("12. Simulación\n")
            print("13. Perfilamiento\n")
            print("14. Reproductor")
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
                cur.execute("UPDATE usuario SET suscripcion='false' WHERE usuario = '%s';" % (user))
                conexion.commit()
                
            elif (op_settings == 7):
                check = ChekArtista(user)
                if(check == True):
                    nomCan = input("Ingrese nombre de la Cancion: ")
                    link = input("Ingrese link de la cancion: ")
                    nomArt = GetArtista(user)
                    activa = "true"
                    cur.execute("insert into canciones values ('%s', '%s', '%s', '%s');" % (nomCan, link,nomArt,activa))
                    conexion.commit()
                elif(check == False):
                    print("Usted no es un Artista registrado")
                
            elif (op_settings == 8):
                usu = input("Escoje usuario para convertir en monitor: \t")
                moni = int(input("Qué tipo de monitor quiere que sea? \t"))
                cur.execute("UPDATE usuario SET administrador = 'true', id_tipo_admin = '%s' WHERE usuario = '%s'" % (moni, usu))
                conexion.commit()
                
            elif (op_settings == 9):
                print("----------REPORTERÍA----------")
                print("1. Albumes más recientes de la última semana")
                print("2. Artistas con popularidad creciente en los ultimos tres meses")
                print("3. Artistas con mayor produccion musical")
                print("4. Usuarios más activos en la plataforma")
                print("5. Cancion con mas reproducciones de un Artista")
                print("6. Generos mas Reproducidas entre un rango de fechas")
                print("7. Artistas mas Reproducidos en un rango de Fechas")
                op_report = int(input("Qué reporte quisiera ver? \t"))
                
                if op_report == 1:
                    cur.execute("SELECT a.nombre FROM albumes a WHERE a.fecha_salida > (SELECT CAST(NOW() AS DATE) - 7);")
                    consulta = cur.fetchall()
                    print("------ALBUMES MÁS RECIENTES DE LA ULTIMA SEMANA------")
                    for a.nombre in consulta:
                        print(a.nombre)
                        
                if op_report == 2:
                    cur.execute("SELECT al.creador, count(r) FROM album_cancion ac INNER JOIN canciones c on ac.id_cancion = c.id INNER JOIN albumes al on ac.id_album = al.nombre INNER JOIN reproducciones r on r.id_cancion = c.id WHERE r.fecha > (SELECT CAST(NOW() AS DATE) - 90) GROUP BY al.creador ORDER BY count(r) desc;")
                    consulta = cur.fetchall()
                    
                    print("------ARTISTAS CON POPULARIDAD CRECIENTE EN LOS ULTIMOS TRES MESES------")
                    for al.creador in consulta:
                        print(al.creador, count(r))
                        
                if op_report == 3:
                    cur.execute("SELECT ar.nombre, count(r) FROM artistas ar INNER JOIN albumes al on ar.nombre = al.creador INNER JOIN canciones c on c.cancion = c.cancion INNER JOIN reproducciones r on r.id_cancion = c.id GROUP BY ar.nombre ORDER BY count(r) desc;")
                    consulta = cur.fetchall()
                    
                    print("------ARTISTAS CON MAYOR PRODUCCION MUSICAL------")
                    for ar.nombre in consulta:
                        print(ar.nombre, count(r))
                        
                if op_report == 4:
                    cur.execute("SELECT usuario, logins FROM usuario ORDER BY logins DESC LIMIT 5;")
                    consulta = cur.fetchall()
                    
                    print("------USUARIOS MÁS ACTIVOS EN LA PLATAFORMA------")
                    for usuario,logins in consulta:
                        print(usuario, logins)
                if op_report == 5:
                    artista = input("Ingrese el Artista")
                    cur.execute("select canciones_repro_unArtista('%s');"% (artista))
                    consulta = cur.fetchall()
                    
                    print("------Cancion con mas reproducciones------")
                    print("------"+ artista +"------")
                    for i in consulta:
                        print(i[0])
                if op_report == 6:
                    fecha1 = input("Ingrese la fecha de la forma Año-Mes-Dia")
                    fecha2 = input("Ingrese la fecha de la forma Año-Mes-Dia")
                    cur.execute("select repro_genero('%s', '%s');"% (fecha1,fecha2))
                    consulta = cur.fetchall()
                    print("------Generos repoducidos------")
                    for i in consulta:
                        print(i)
                if op_report == 7:
                    fecha1 = input("Ingrese la fecha de la forma Año-Mes-Dia")
                    fecha2 = input("Ingrese la fecha de la forma Año-Mes-Dia")
                    cur.execute("select artistas_repro('%s', '%s', 5);"% (fecha1,fecha2))
                    consulta = cur.fetchall()
                    print("------Generos repoducidos------")
                    for i in consulta:
                        print(i)
            elif (op_settings == 10):
                cur.execute("select * from bitacora;")
                consulta = cur.fetchall()
                print("------Bitacora Operaciones------")
                for i in consulta:
                    print(i[0]+" "+i[1]+" "+i[2]+" "+str(i[3]))
        
            elif (op_settings == 11):
                cur.execute("select c.artista, (count(r))*(1/1000.0) as comision_en_dolares from canciones c inner join reproducciones r on r.id_cancion = c.id inner join artistas a on c.artista = a.nombre group by c.artista;")
                consulta = cur.fetchall()
                print("------Comisiones Por Artista------")
                for i in consulta:
                    print(i[0]+" $"+str(i[1]))
                    
            elif (op_settings == 12):
                artistas = ["SadJ", "Drake", "Alan Walker", "J Balvin", "AC/DC", "Daddy Yankee"]
                albumes = ["Colores", "Back In Black", "Dura", "Alone", "Toosie Slide"]
                usuarios = ["user2", "user3", "user4", "user5", "user1"]
                canciones = []
                
                fecha = input("Ingrese fecha a simular (YYYY-MMM-DDD)\t")
                tracks = int(input("Ingrese cantidad de tracks a generar\t"))
                repos = int(input("Ingrese cantidad de reproducciones a simular\t"))
                
                #cur.execute('DELETE FROM "public"."canciones"')
                conexion.commit()
                
                for i in range(1,tracks+1):
                    cur.execute("INSERT INTO  canciones(cancion, link, artista, activa) VALUES ('-----', 'http-', '%s', 'true')" % (random.choice(artistas)))
                    conexion.commit()
                    
                    cur.execute("INSERT INTO album_cancion (id_cancion, id_album) VALUES ('%s', '%s')" % (i, random.choice(albumes)))
                    conexion.commit()
                    
                    #canciones.append(i)
                cur.execute("select id from canciones")
                ids = cur.fetchall()
                conexion.commit()
                for i in ids:
                    t = ' '.join([str(x) for x in i])
                    canciones.append(int(t))
                    
                for i in range(1,repos+1):
                    cur.execute("INSERT INTO reproducciones (id_cancion, fecha, usuario ) VALUES ('%s', '%s', '%s')" % (random.choice(canciones), fecha,random.choice(usuarios)))
                    conexion.commit()
                    
                print("Simulación Completada")
            
            elif (op_settings == 13):
                client = MongoClient('localhost')
                db = client['Perfilamiento']
                db.drop_collection('usuarios')
                col = db['usuarios']
                
                users = ["user2", "user3", "user4", "user5", "user1"]
    
                fecha = input("Ingrese fecha a perfilar (YYYY-MMM-DDD)\t")
                
                cur.execute("select c.id, x.usuario, x.fecha from canciones c inner join (select u.usuario, r.id_cancion, r.fecha from usuario u inner join reproducciones r on u.usuario = r.usuario where r.fecha = '%s' group by u.usuario, r.id_cancion, r.fecha) as x on c.id = x.id_cancion;" % (fecha))
                usuarios = cur.fetchall()
                
                for i in users:
                    col.insert_one({
                        'Usuario':i,
                        'Id_Cancion Reproducida':[]
                    })
                   
                for i in usuarios:              
                    col.find_one_and_update({'Usuario':i[1]},
                                      {'$push' : {'Id_Cancion Reproducida':i[0]}})
                
                for documento in col.find({}):
                    print(documento)
                
#2021-01-01             
            
            elif (op_settings == 14):
                pass  
    
def User_Normal(user):
    op_settings = 0
    while(op_settings != 5):
            print("--------------CONFIGURACIÓN--------------")
            print("1. Suscribirse\n")
            print("2. Ser Artista\n")
            print("3. Ser Manager\n")
            print("4. Subir Cancion\n")
            print("5. Reproductor")
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
                check = ChekArtista(user)
                if(check == True):
                    nomCan = input("Ingrese nombre de la Cancion: ")
                    link = input("Ingrese link de la cancion: ")
                    nomArt = GetArtista(user)
                    activa = "true"
                    cur.execute("insert into canciones values ('%s', '%s', '%s', '%s');" % (nomCan, link,nomArt,activa))
                    conexion.commit()
                elif(check == False):
                    print("Uste no es un Artista registrado")
            elif (op_settings == 5):
                pass
                



def ChekArtista(user):
    consulta = [1, 2, 3]
    cur.execute("select usuario from artistas where usuario = '%s';" % (user))
    consulta = cur.fetchall()
    if(consulta == []):
        return False
    elif(consulta != []):
        return True

def GetArtista(user):
    consulta = [1, 2, 3]
    cur.execute("select nombre from artistas where usuario = '%s';" % (user))
    consulta = cur.fetchone()
    for i in consulta:
        return i
    
 