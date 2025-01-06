from class_produto import Produto

class Acessorio(Produto):

    def __init__(self,  nome: str, preco: float, quantidade_em_estoque: int, categoria: str, tamanho: str):
        super().__init__(nome, preco, quantidade_em_estoque)
        self.categoria = categoria
        self.tamanho = tamanho

        