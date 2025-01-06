class Produto:

    def __init__(self, nome: str, preco: float, quantidade_em_estoque: int):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque
        self.limite_estoque = int(quantidade_em_estoque * 0.25)
        self.vendas = 0

    def vender(self, quantidade):
        if self.quantidade_em_estoque >= quantidade:
            self.quantidade_em_estoque -= quantidade
            self.vendas += quantidade
            self.alerta_baixa()
            return print(f"Vendido {quantidade} do produto {self.nome} com sucesso!")
        else:
            return print(f"Estoque do produto {self.nome} insuficiente!")

    def repor_estoque(self, quantidade):
        self.quantidade_em_estoque += quantidade
        self.alerta_baixa()
        return print(f"Estoque reposto com sucesso!")

    def exibir_informacoes(self):
        return print(f"Detalhes do produto\nNome: {self.nome}\nPreço: {self.preco}\nEstoque: {self.quantidade_em_estoque}")
    
    def alerta_baixa(self):
        if self.quantidade_em_estoque < self.limite_estoque:
            return print(f"Estoque do produto {self.nome} está abaixo do limite. Tem {self.quantidade_em_estoque} unidades.")