from class_produto import Produto

class Brinquedo(Produto):

    def __init__(self,  nome: str, preco: float, quantidade_em_estoque: int, material: str, faixa_etaria: str):
        super().__init__(nome, preco, quantidade_em_estoque)
        self.material = material
        self.faixa_etaria = faixa_etaria

        