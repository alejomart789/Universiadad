class Empleado:
    __nombre__ = ''
    __identificacion__ = 0
    __edad__ = 0
    __estadoCivil__ = ''
    __salario__ = ''
    
    def __init__(self, nombre, identificacion, edad, estadoCivil, salario):
        self.nombre = nombre
        self.identificacion = identificacion
        self.edad = edad
        self.estadoCivil = estadoCivil
        self.salario = salario
        
    def getNombre(self):
        return self.__nombre__
    def setNombre(self, nombre):
        self.__nombre__ = nombre
        
    def getIdentificacion(self):
        return self.__identificacion__
    def setIdentificacion(self, identificacion):
        self.__identificacion__ = identificacion
        
    def getEstadoCivil(self):
        return self.__estadoCivil__
    def setEstadoCivil(self, estadoCivil):
        self.__estadoCivil__ = estadoCivil
    
    def getSalario(self):
        return self.__salario__
    def setSalario(self, salario):
        self.__salario__ = salario