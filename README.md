# SQLite-Python
Descripción del manejo de base de datos en SQLite
PySQLITE
The PySQLite provides a standardized Python DBI API 2.0 compliant interface to the SQLite database. If your application needs to support not only the SQLite database but also other databases such as MySQL, PostgreSQL, and Oracle, the PySQLite is a good choice.

PySQLite is a part of the Python Standard library since Python version 2.5

Creación de una base de datos en SQLIte

When you connect to an SQLite database file that does not exist, SQLite automatically creates the new database for you.

To create a database, first, you have to create a Connection object that represents the database using the connect() function of the sqlite3 module.

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"C:\sqlite\db\pythonsqlite.db")
    
In this code:

First, we define a function called create_connection() that connects to an SQLite database specified by the database file db_file. Inside the function, we call the connect() function of the sqlite3 module.

The connect() function opens a connection to an SQLite database. It returns a Connection object that represents the database. By using the Connection object, you can perform various database operations.

In case an error occurs, we catch it within the try except block and display the error message. If everything is fine, we display the SQLite database version. 


CREATE TABLES IN SQLite Databse using Python.

To create a new table in an SQLite database from a Python program, you use the following steps:

First, create a Connection object using the connect() function of the sqlite3 module.
Second, create a Cursor object by calling the cursor() method of the Connection object.
Third, pass the CREATE TABLE statement to the execute() method of the Cursor object and execute this method.

CREATE TABLE IF NOT EXISTS projects (
	id integer PRIMARY KEY,
	name text NOT NULL,
	begin_date text,
	end_date text
);

-- tasks table
CREATE TABLE IF NOT EXISTS tasks (
	id integer PRIMARY KEY,
	name text NOT NULL,
	priority integer,
	project_id integer NOT NULL,
	status_id integer NOT NULL,
	begin_date text NOT NULL,
	end_date text NOT NULL,
	FOREIGN KEY (project_id) REFERENCES projects (id)
);

INSERT INTO TABLES IN SQLITE IN PYTHON

To insert rows into a table in SQLite database, you use the following steps:

First, connect to the SQLite database by creating a Connection object.
Second, create a Cursor object by calling the cursor method of the Connection object.
Third, execute an INSERT statement. If you want to pass arguments to the INSERT statement, you use the question mark (?) as the placeholder for each argument.

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
    
  def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid
    
To be able to apply SQLite Lightweight Python Database for the following exercise, we have created a Python file called "classes.py" in this it has 3 classes called "Person", "Informatic" and TecRedes ", the classes Informatico and TecRedes Inherit from the Persona Class, the idea is that using a separate file that defines the databases and tables with SQLIte is to save data, query data, and Delete data in SQLite3

File "clases.py"

class Persona:

    # Atributos o Propiedades de la clase persona
    nombres = "Juan Fernando"
    apellidos = "Garzon Aviles"
    altura = 1.74
    edad = 25

    # Constructor de la clase Persona
    def __init__(self, nombres, apellidos, altura, edad):
        self.nombres = nombres
        self.apellidos = apellidos
        self.altura = altura
        self.edad = edad
         
    # Métodos
    def setNombre(self, nombres):
        self.nombres = nombres

    def getNombres(self):
        return self.nombres

    def setApellido(self, apellidos):
        self.apellidos = apellidos

    def getApellidos(self):
        return self.apellidos

    def setAltura(self, altura):
        self.altura = altura

    def getAltura(self):
        return self.altura

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"


class Informatico(Persona):
    titulo = "Lcdo en Informatico"
    años_estudio = 5
    certicado = "Prog de Microcomputadoras"                                                
    universidad = "Universidad de Guayaquil"
    otros = "ESPOL"
    experiencia = 10
    lenguajes = "PHP"

       
    # Métodos de la clase Informatico

    def __init__(self, apellidos, nombres, altura, edad, titulo, años_estudio, certicado, universidad, otros, experiencia, lenguajes):
        # LLama al constructor para establecer los valores iniciales
        super().__init__(apellidos, nombres ,altura, edad)
        self.titulo = titulo 
        self.años_estudio = años_estudio
        self.certificado = certicado
        self.universidad = universidad
        self.otros = otros
        self.experiencia = experiencia
        self.lenguajes = lenguajes

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getTitulo(self):
        return self.titulo

    def setAestudios(self, aestudios):
        self.años_estudio = aestudios

    def getAñosEst(self):
        return self.años_estudio

    def setCertificado(self, certificado):
        self.certicado = certificado

    def getCertificado(self):
        return self.certicado

    def setUniversidad(self, universidad):
         self.universidad = universidad

    def getUniversidad(self):
        return self.universidad

    def setOtros(self, otros):
        self.otros = otros

    def getOtros(self):
        return self.otros

    def setExperiencia(self, experiencia):
        self.experiencia = experiencia

    def getExperiencia(self):
        return self.experiencia

    def setLenguajes(self, lenguajes):
        self.lenguajes = lenguajes

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self):
        return "He aprendido a programar es : " + self.getLenguajes()
 
    def programar(self):
        return "Estoy aprendiendo en : " + self.getLenguajes()

class TecnicoRedes(Informatico):
    # atributos
    auditarRedes = "experto"
    experienciaredes = 15

    # Constructor
    def __init__(self, nombres, apellidos, altura, edad, titulo, años_estudio, certificado, universidad, otros, experiencia, lenguajes, auditarRedes, experienciaredes):
        super().__init__(nombres, apellidos, altura, edad, titulo, años_estudio, certificado, universidad, otros, experiencia, lenguajes)
        self.auditarRedes = auditarRedes
        self.experienciaredes = experienciaredes

         

    def setAuditar(self, auditar):
        self.auditarRedes = auditar

    def getAuditarRedes(self):
        return self.auditarRedes

    def setExpRedes(self, experienciared):
        self.experienciaredes = experienciared

    def getExpRedes(self):
        return self.experienciaredes

    def auditoria(self):
        return "Estoy auditando redes !!!"

File "sqlite2.py"

# Importar modulo
import sqlite3
from sqlite3 import Error

import clases
# Crear la base de datos
def crear_base(nombre_base):
    
    conn = None
    # Crea la base de datos
    try:
        
        conn = sqlite3.connect(nombre_base)
        print(sqlite3.version)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def crear_tabla(nombre_base):

    conn = None

    try:

        conn = sqlite3.connect(nombre_base)
        # Crear los cursores
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        
        # Crea la tabla
        cursor.execute("CREATE TABLE IF NOT EXISTS persona(" +
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                    "apellidos VARCHAR(50), " +
                    "nombres VARCHAR(50), " +
                    "altura INTEGER(3), " +
                    "edad INTEGER(3) " +
                ")")
        # Guardar cambios
        conn.commit()
            
        # Crear la 2da tabla
        cursor1.execute("CREATE TABLE IF NOT EXISTS espinf(" +
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                    "apellidos VARCHAR(50), " +
                    "nombres VARCHAR(50), " +
                    "altura INTEGER(3), " +
                    "edad INTEGER(3), " +
                    "titulo VARCHAR(70), " +
                    "tiempo_estudios INTEGER(2), " +
                    "certificado VARCHAR(30), " +
                    "universidad VARCHAR(30), " +
                    "otros VARCHAR(20), " +
                    "experiencia INTEGER(2), " +
                    "lenguajes TEXT" +
            ")")

        # Guardar cambios
        conn.commit()
        # Crear la 3era. tabla para Tecnico en redes
        cursor2.execute("CREATE TABLE IF NOT EXISTS espredes(" +
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                    "apellidos VARCHAR(50), " +
                    "nombres VARCHAR(50), " +
                    "altura INTEGER(3), " +
                    "edad INTEGER(3), " +
                    "titulo VARCHAR(70), " +
                    "tiempo_estudios INTEGER(2), " +
                    "certificado VARCHAR(30), " +
                    "universidad VARCHAR(30), " +
                    "otros VARCHAR(20), " +
                    "experiencia INTEGER(2), " +
                    "lenguajes TEXT, " +
                    "auditredes VARCHAR(20), " +
                    "experienciaredes INTEGER(2) " +
                ")")
        # Guardar cambios
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()



def ingreso_persona(bases_datos,personas): 

    # Crea la conexion de la tabla
    conn = None

    try:
        conn = sqlite3.connect(bases_datos)
        cursor = conn.cursor()

        # Guarda datos
        cursor.executemany("INSERT INTO persona(id,apellidos,nombres,altura,edad) " +
        "VALUES(null,?,?,?,?)",personas)
        # Guardar cambios
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


            
def ingreso_informatico(bases_datos,informatico):

    # variable de conexion
    conn = None

    try:
        conn = sqlite3.connect(bases_datos)
        cursor = conn.cursor()
        # Guarda datos
        cursor.executemany("INSERT INTO espinf(id,apellidos,nombres,altura,edad,titulo,tiempo_estudios,certificado,universidad,otros,experiencia,lenguajes) " +
            "VALUES(null,?,?,?,?,?,?,?,?,?,?,?)",informatico)
        
        # Guardar cambios
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def Ingreso_Tecredes(Bases_datos,Tecredes):
    # Variable de conexion
    conn = None

    try:
        conn = sqlite3.connect(Bases_datos)
        cursor = conn.cursor()
        # Guarda datos
        cursor.executemany("INSERT INTO espredes(id,apellidos,nombres,altura,edad,titulo,tiempo_estudios,certificado,universidad,otros,experiencia,lenguajes,auditredes,experienciaredes)" +
            "VALUES(null,?,?,?,?,?,?,?,?,?,?,?,?,?)",Tecredes)
        # Guardar cambios
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def lista_personal_informatico(base):

    # Variable de conexion
    conn = None

    try:

        conn = sqlite3.connect(base)
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        # Consulta personal
        cursor.execute("SELECT * FROM persona;")
        cursor1.execute("SELECT * FROM espinf;")
        personas = cursor.fetchall()
        informaticos = cursor1.fetchall()
        # Listar persona y profesional
        for persona in personas:
            print("Id        :",persona[0])
            print("Apellidos :",persona[1])
            print("Nombres   :",persona[2])
            print("Altura    :",persona[3])
            print("Edad      :",persona[4])
            print("\n")

        # Profesional
        for informa in informaticos:
            print("Id              :",informa[0])
            print("Apellidos       :",informa[1])
            print("Nombres         :",informa[2])
            print("Altura          :",informa[3])
            print("Edad            :",informa[4])
            print("Titulo          :",informa[5])
            print("Tiempo_estudios :",informa[6])
            print("Certificado     :",informa[7])
            print("Universidad     :",informa[8])
            print("Otros           :",informa[9])
            print("Experiencia     :",informa[10])
            print("Lenguajes       :",informa[11])
            print("\n")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def lista_personal_redes(bases_datos):

    # crear variable de conexion
    conn = None

    try:

        conn = sqlite3.connect(bases_datos)
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        # Consulta personal
        cursor.execute("SELECT * FROM persona;")
        cursor1.execute("SELECT * FROM espredes;")
        personas = cursor.fetchall()
        redes = cursor1.fetchall()
        # Listar persona y profesional
        for persona in personas:
            print("Id        :",persona[0])
            print("Apellidos :",persona[1])
            print("Nombres   :",persona[2])
            print("Altura    :",persona[3])
            print("Edad      :",persona[4])
            print("\n")

        # Profesional
        for informa in redes:
            print("Id              :",informa[0])
            print("Apellidos       :",informa[1])
            print("Nombres         :",informa[2])
            print("Altura          :",informa[3])
            print("Edad            :",informa[4])
            print("Titulo          :",informa[5])
            print("Tiempo_estudios :",informa[6])
            print("Certificado     :",informa[7])
            print("Universidad     :",informa[8])
            print("Otros           :",informa[9])
            print("Experiencia     :",informa[10])
            print("Lenguajes       :",informa[11])
            print("Auditoria redes :",informa[12])
            print("Experiencia red :",informa[13])
            print("\n")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def elimina_personal(Base_datos):

    # Crear variable de conexion
    conn = None

    try:

        conn = sqlite3.connect(Base_datos)
        cursor = conn.cursor()

        codigo = int(input("Digite codigo : "))

        cursor.execute(f"SELECT * FROM persona WHERE id = {codigo}")
        personas = cursor.fetchall()

        # Elimina datos
        for pers1 in personas:
            if pers1[0] <= 0:
                print("No existe persona....\n",end="")
            else:
                cursor1 = conn.cursor()
                cursor1.execute(f"DELETE FROM persona WHERE id = {codigo}")
                # Guardar cambios
                conn.commit()
                print("Se elimino registro......\n",end="")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def elimina_informatica(bases_datos):

    # crear la variable
    conn = None

    try:

        conn = sqlite3.connect(bases_datos)
        # cursores
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        # consulta
        codigo = int(input("Ingrese codigo : "))
        cursor1.execute(f"SELECT * FROM espinf WHERE id = {codigo}")
        informaticos = cursor1.fetchall()

        for informa in informaticos:
            if informa[0] <= 0:
                print("No existe registro a eliminar .....\n",end="")
            else:
                cursor2.execute(f"DELETE FROM espinf WHERE id = {codigo}")
                conn.commit()
                print("Se ha eliminado registro....\n",end="")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def elimina_tec_redes(bases_datos):
    # Crea variable

    conn = None

    try:
        conn = sqlite3.connect(bases_datos)
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()

        # consulta para eliminar
        codigo = int(input("Ingrese Id : "))
        #
        cursor1.execute(f"SELECT * FROM espredes WHERE id = {codigo}")
        redesson = cursor1.fetchall()

        # verifica antes de eliminar
        for redes in redesson:
            if redes[0] <= 0:
                print("No se puede eliminar registro...\n",end="")
            else:
                cursor2.execute(f"DELETE FROM espredes WHERE id = {codigo}")
                # Guardar carmbios
                conn.commit()
                print("Se elimino registro......\n",end="")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


print("\n")
print("####### ####### INGRESO DE DATOS DE PERSONAL, INFORMATICO Y REDES\n",end="")
print("\n")
### menu de datos
verdad = True
while verdad:
    # Crea base
    crear_base("empleados.db")
    crear_tabla("empleados.db")
    ##############
    print("\n")
    print("########## Ingreso de datos Personal y profesional\n",end="")
    print("\n")
    print("1.- Ingreso de datos Personal e Informaticos\n",end="")
    print("2.- Ingreso de datos Personal y de redes\n",end="")
    print("3.- Consulta de datos Personal e Informatico\n",end="")
    print("4.- Consulta de datos Personal y redes\n",end="")
    print("5.- Elimina Datos\n",end="")
    print("6.- Salir")
    opcion = int(input("Digite su opcion 1-5 : "))
    ##
    if opcion == 1:
        persona = clases.Persona("","",170,20)
        nombres1 = input("Ingrese Nombres : ")
        persona.setApellido(nombres1)
        apellidos1 = input("Ingrese Apellidos : ")
        persona.setNombre(apellidos1)
        altura1 = int(input("Ingrese la Altura :"))
        persona.setAltura(altura1)
        edad1 = int(input("Ingrese la Edad : "))
        persona.setEdad(edad1)
        personas = [((persona.getApellidos(),persona.getNombres(),persona.getAltura(),persona.getEdad()))]
        # ingreso datos informaticos
        informatico = clases.Informatico("","",170,20,"",5,"","","",4,"")
        informatico.setNombre(nombres1)
        informatico.setApellido(apellidos1)
        informatico.setAltura(altura1)
        informatico.setEdad(edad1)
        titulo1 = input("Ingrese el Titulo : ")
        informatico.setTitulo(titulo1)
        tiempo1 = int(input("Ingrese los años de Estudio : "))
        informatico.setAestudios(tiempo1)
        certificado1 = input("Ingrese certificado : ")
        informatico.setCertificado(certificado1)
        univer1 = input("Ingrese Universidad : ")
        informatico.setUniversidad(univer1)
        otros1 = input("Ingrese otros : ")
        informatico.setOtros(otros1)
        experi1 = int(input("Ingreso los años de experiencia : "))
        informatico.setExperiencia(experi1)
        leng1 = input("Ingrese lenguajes : ")
        informatico.setLenguajes(leng1)
        datosinf = [((informatico.getApellidos(),informatico.getNombres(),informatico.getAltura(),informatico.getEdad(),informatico.getTitulo(),
            informatico.getAñosEst(),informatico.getCertificado(),informatico.getUniversidad(),informatico.getOtros(),
            informatico.getExperiencia(),informatico.getLenguajes()))]
        ## Guardar datos a la tabla
        ## Tabla Personal
        ingreso_persona("empleados.db",personas)
        ## Imgreso de la tabla informatica
        ingreso_informatico("empleados.db",datosinf)
    if opcion == 2:
        persona = clases.Persona("","",170,20)
        nombres1 = input("Ingrese Nombres : ")
        persona.setApellido(nombres1)
        apellidos1 = input("Ingrese Apellidos : ")
        persona.setNombre(apellidos1)
        altura1 = int(input("Ingrese la Altura :"))
        persona.setAltura(altura1)
        edad1 = int(input("Ingrese la Edad : "))
        persona.setEdad(edad1)
        personas = [((persona.getApellidos(),persona.getNombres(),persona.getAltura(),persona.getEdad()))]
         
        # ingreso datos informaticos
        redes = clases.TecnicoRedes("","",170,20,"",5,"","","",4,"","",5)
        redes.setNombre(nombres1)
        redes.setApellido(apellidos1)
        redes.setAltura(altura1)
        redes.setEdad(edad1)
        titulo1 = input("Ingrese el Titulo : ")
        redes.setTitulo(titulo1)
        tiempo1 = int(input("Ingrese los años de Estudio : "))
        redes.setAestudios(tiempo1)
        certificado1 = input("Ingrese certificado : ")
        redes.setCertificado(certificado1)
        univer1 = input("Ingrese Universidad : ")
        redes.setUniversidad(univer1)
        otros1 = input("Ingrese otros : ")
        redes.setOtros(otros1)
        experi1 = int(input("Ingreso los años de experiencia : "))
        redes.setExperiencia(experi1)
        leng1 = input("Ingrese lenguajes : ")
        redes.setLenguajes(leng1)
        auditarredes1 = input("Ingrese Tipo de auditar redes : ")
        redes.setAuditar(auditarredes1)
        experedes1 = int(input("Ingrese los años de Experiencia en redes : "))
        redes.setExpRedes(experedes1)
        # Variable para guardar los datos de tecnico de redes
        Tecredes = [((redes.getApellidos(),redes.getNombres(),redes.getAltura(),redes.getEdad(),redes.getTitulo(),
                 redes.getAñosEst(),redes.getCertificado(),redes.getUniversidad(),redes.getOtros(),
                 redes.getExperiencia(),redes.getLenguajes(),redes.getAuditarRedes(),redes.getExpRedes()))]
        ## Guardar datos a la tabla
        ## Tabla Personal
        ingreso_persona("empleados.db",personas)
        ## Imgreso de la tabla informatica
        Ingreso_Tecredes("empleados.db",Tecredes)
    if opcion == 3:
        lista_personal_informatico("empleados.db")
    if opcion == 4:
        lista_personal_redes("empleados.db")
    if opcion == 5:
        print("\n")
        print("###### Menu de Eliminacion ######### \n",end="")
        print("\n")
        print("1.- Eliminacion de datos de Personal\n",end="")
        print("2.- Elimacion de datos de Informatica\n",end="")
        print("3.- Elimacion de datos de Tecnico de Redes\n",end="")
        print("4.- Regresar\n",end="")
        opcion1 = int(input("Ingrese una opcion 1-4 : "))

        if opcion1 == 1:
            elimina_personal("empleados.db")
        if opcion1 == 2:
            elimina_informatica("empleados.db")
        if opcion1 == 3:
            elimina_tec_redes("empleados.db")
        if opcion1 == 4:
            exit
    if opcion == 6:
       verdad = False

