from entidades.envio_terrestre import EnvioTerrestre
from entidades.envio_aereo import EnvioAereo

e1 = EnvioTerrestre("Juanito Hernández", "Calle 10 colonia centro", 12.5, 1393, 1450)

total = e1.calcular_costo()
print(total)

ea = EnvioAereo("José Torres", "Calle 13 colonia moderna", 15, 1321, 1600, 300)

total2 = ea.calcular_costo()
print(total2)