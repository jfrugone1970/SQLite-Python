# Herencia: Es la posibilidad de compartir atributos y métodos 
# entre clases. Y que diferentes clases heredan 

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
