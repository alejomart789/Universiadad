from Empleado import Empleado

class Programador(Empleado):
    __numeroDeLineasPorHora__ = 0
    __lenguajeProgramacion__ = ''
    
    def __init__(self, nombre, identificacion, edad, estadoCivil, salario, numeroDeLineasPorHora, lenguajeProgramacion):
        super().__init__(nombre, identificacion, edad, estadoCivil, salario)
        self.numeroDeLineasPorHora = numeroDeLineasPorHora
        self.lenguajeProgramacion = lenguajeProgramacion
        
    def getNumeroDeLineasPorHora(self):
        return self.numeroDeLineasPorHora
    def setNumeroDeLineasPorHora(self, numeroDeLineasPorHora):
        self.numeroDeLineasPorHora = numeroDeLineasPorHora
    
    def getLenguajeProgramacion(self):
        return self.lenguajeProgramacion
    def setLenguajeProgramacion(self, lenguajeProgramacion):
        self.lenguajeProgramacion = lenguajeProgramacion
    