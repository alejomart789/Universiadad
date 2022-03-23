from Programador import Programador
from Arquitecto import Arquitecto
from Director import Director

pr1 = Programador('Alejandro', 1006858288, 20, 'Soltero', 1000000, 20, 'Python')
pr2 = Programador('Obando', 2543567896, 30, 'Casado', 1000000, 30, 'Java')

dr1 = Director('Perez', 2412533564, 25, 'Casado', 3000000, 10)

ar1 = Arquitecto('Camilo', 6438465832, 30, 'Soltero', 2500000, 25)

print('Programador del equipo:',pr1.nombre)
print('Director del equipo:',dr1.nombre)
print('Arquitecto del equipo:',ar1.nombre)
