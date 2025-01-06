from class_produto import Produto

class Medicamento(Produto):

    def __init__(self,  nome: str, preco: float, quantidade_em_estoque: int, tipo: str, dosagem: str):
        super().__init__(nome, preco, quantidade_em_estoque)
        self.tipo = tipo
        self.dosagem = dosagem

    