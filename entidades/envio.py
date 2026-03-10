class Envio:
    def __init__(self, cliente: str, dirección: str, peso: float, distancia:float):
        self.cliente = cliente
        self.dirección = dirección
        self .peso = peso
        self.distancia = distancia
    
    def calcular_costo_base(self) -> float:
        costo = (self.peso * 2) + (self.distancia * 0.3)
        return costo