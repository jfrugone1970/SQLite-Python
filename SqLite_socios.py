# Impotamos la base de datos
import sqlite3
from sqlite3 import Error

# crear la base de datos
def crear_base(base_datos):

    # variable para conexion
    conn = None
    try:
        conn = sqlite3.connect(base_datos)
        print(sqlite3.version)
        print(sqlite3.version_info)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def crear_tabla(base_datos):

    # variable para conexion
    # y para crear tabla
    conn = None
    try:
        conn = sqlite3.connect(base_datos)
        cursor = conn.cursor()
        # Crea tabla
        cursor.execute("CREATE TABLE IF NOT EXISTS socios(" +
                   "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   "apellidos VARCHAR(50), " +
                   "nombres VARCHAR(50), " +
                   "direccion VARCHAR(100), " +
                   "telefono TEXT " +
              ")")
        # Guardar cambios
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def ingreso_socios(base_datos,socios):

     # variabla para conexion
     conn = None

     try:
         conn = sqlite3.connect(base_datos)
         cursor = conn.cursor()
         # ingresar datos
         cursor.executemany("INSERT INTO socios(id,apellidos,nombres,direccion,telefono) " +
          "VALUES(null,?,?,?,?)",socios)
         # guardar cambios
         conn.commit()
         print("Se ha registrado socio.....\n",end="")
     except Error as e:
         print(e)
     finally:
         if conn:
             conn.close()

def consulta_socio(base_datos):
    # crear variable de conexion
    conn = None

    try:
        conn = sqlite3.connect(base_datos)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM socios;")
        sociostodos = cursor.fetchall()
        # Muestra los socios
        print("\n")
        print("###### Se va a proceder a consultar socio ####### \n",end="")
        print("\n")
        for socio in sociostodos:
            print("Id           : ",socio[0])
            print("Apellidos    : ",socio[1])
            print("Nombres      : ",socio[2])
            print("Direccion    : ",socio[3])
            print("Telefono     : ",socio[4])
            print("\n")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def elimina_socio(base_datos):

    #variabla para manejo de base de datos
    conn = None

    try:
        conn = sqlite3.connect(base_datos)
        cursor = conn.cursor()
        # Elimina datos
        codigo = int(input("Ingrese id : "))
        cursor1 = conn.cursor()
        cursor.execute(f"SELECT * FROM socios WHERE id = {codigo};")
        sociostodos = cursor.fetchall()

        # verifica si existe antes de eliminar
        for socio in sociostodos:
            if socio[0] <= 0:
                print("No existe socio a eliminar...\n",end="")
            else:
                cursor1.execute(f"DELETE FROM socios WHERE id = {codigo};")
                # guardar cambios
                conn.commit()
                print("Se elimino socio......\n",end="")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

print("\n")
print("######## Programa para manejo de socios en un club ########### \n",end="")
print("\n")
seguir = True
while seguir:
    crear_base("club.db")
    crear_tabla("club.db")
    print("\n")
    print("##########  MENU PRINCIPAL ###########\n",end="")
    print("\n")
    print("1.- Ingreso de datos de socios\n",end="")
    print("2.- Consulta de datos de socios\n",end="")
    print("3.- Eliminacion de registro de socios\n",end="")
    print("4.- Salir\n",end="")
    opcion=int(input("Digite una opcion 1-4 : "))
    if opcion == 1:
        ape = input("Ingrese Apellidos   :")
        nom = input("Ingrese Nombres     :")
        direc = input("Ingrese direccion :")
        telef = input("Ingrese telefono  :")
        # crear variable de arreglo para guardar datos
        socios1 = [(ape,nom,direc,telef)]
        ingreso_socios("club.db",socios1)
    if opcion == 2:
         consulta_socio("club.db")
    if opcion == 3:
         elimina_socio("club.db")
    if opcion == 4:
         seguir = False

