from Empleado import Empleado

class Director(Empleado):
    __añosExperiencia__ = 0
    
    def __init__(self, nombre, identificacion, edad, estadoCivil, salario, añosExperiencia):
        super().__init__(nombre, identificacion, edad, estadoCivil, salario)
        self.añosExperiencia = añosExperiencia
    
    def getAñosExperiencia(self):
        return self.añosExperiencia
    def setAñosExperiencia(self, añosExperiencia):
        self.añosExperiencia = añosExperiencia