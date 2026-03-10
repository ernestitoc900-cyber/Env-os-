from entidades.envio import Envio

class EnvioAereo(Envio):
    def __init__(self, cliente: str, dirección: str, peso: float, distancia: float, tarifa_aeropuerto: float, impuesto_aereo: float):
        super().__init__(cliente, dirección, peso, distancia)
        self.tarifa_aeropuerto = tarifa_aeropuerto
        self.impuesto_aereo = impuesto_aereo
    
    def calcular_costo(self) -> float:
        costo_base = self.calcular_costo_base()
        total = costo_base + (self.tarifa_aeropuerto * self.impuesto_aereo)
        return total