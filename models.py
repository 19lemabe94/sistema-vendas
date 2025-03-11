class Produto:
    def __init__(self, id, nome, preco, estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def atualizar_estoque(self, quantidade):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            return True
        return False
