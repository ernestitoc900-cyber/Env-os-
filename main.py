from entidades.envio_terrestre import EnvioTerrestre
from entidades.envio_aereo import EnvioAereo

try:
    nombre = input("Ingrese el nombre del cliente: ")

    direccion = input("Ingrese la dirección del cliente: ")

    peso = float(input("Ingrese el peso del paquete: "))

    distancia = float(input("Ingrese la distancia a recorrer: "))

    tarifa_combustible = float(input("Ingrese la tarifa de combustible: "))

    et = EnvioTerrestre(nombre, direccion, peso, distancia, tarifa_combustible)

    total = et.calcular_costo()
    print(total)

    ea = EnvioAereo(nombre, direccion, peso, 1350, 1000, 0.16)

    total2 = ea.calcular_costo()
    print(total2)

except ValueError:
    print("El valor tiene que ser un número decimal")