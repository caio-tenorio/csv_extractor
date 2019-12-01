

class Remuneracao():
    vereador = None
    total_vantagens = None
    descontos_totais = None
    valor_liquido = None
    data = None

    def __init__(self, vereador, total_vantagens, descontos_totais, valor_liquido, data):
        self.vereador = vereador
        self.total_vantagens = total_vantagens
        self.descontos_totais = descontos_totais
        self.valor_liquido = valor_liquido
        self.data = data
