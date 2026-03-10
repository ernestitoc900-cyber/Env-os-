from entidades.envio import Envio

class EnvioTerrestre(Envio):
    def __init__(self, cliente: str, dirección: str, peso: float, distancia: float, tarifa_combustible: float):
        super().__init__(cliente, dirección, peso, distancia)
        self.tarifa_conbustible = tarifa_combustible

    def calcular_costo(self) -> float:
        costo_base = self.calcular_costo_base()
        total = costo_base + self.tarifa_conbustible
        return total