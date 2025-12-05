import math

class Ponto:
    # método construtor
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y
        
    # método para calcular e retornar a distância entre dois pontos
    def calcular_distancia(self, p : "Ponto") -> float:
        return math.hypot(self.x - p.x, self.y - p.y)
    
    # método para calcular e retornar a distância de um ponto até a origem
    def calcular_distancia_ate_origem(self) -> float:
        return math.hypot(self.x, self.y)
    
    # sobreposição de método ou override
    def __str__(self):
        return f'({self.x}, {self.y})'