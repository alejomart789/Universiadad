from Empleado import Empleado


class Arquitecto(Empleado):
    __cantidadProyectos__ = 0
    
    def __init__(self, nombre, identificacion, edad, estadoCivil, salario, cantidadProyectos):
        super().__init__(nombre, identificacion, edad, estadoCivil, salario)
        self.cantidadProyectos = cantidadProyectos
    
    def getCantidadProyectos(self):
        return self.cantidadProyectos
    def setCantidadProyectos(self, cantidadProyectos):
        self.cantidadProyectos = cantidadProyectos