from class_produto import Produto

class Racao(Produto):

    def __init__(self,  nome: str, preco: float, quantidade_em_estoque: int, tipo_animal: str, peso: float):
        super().__init__(nome, preco, quantidade_em_estoque)
        self.tipo_animal = tipo_animal
        self.peso = peso

    