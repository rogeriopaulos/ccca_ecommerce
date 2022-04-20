class Pedido:

    def __init__(self, descricao=None, preco=None, quantidade=None):
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    @property
    def valor_total(self):
        return self.preco * self.quantidade


class Comprador:

    def __init__(self, nome=None, cpf=None):
        self.nome = nome
        self.cpf = cpf

    def is_valid_cpf(self):
        return True if self.cpf == "00799773328" else False


class Compra:

    def __init__(self, comprador: Comprador()):
        self.carrinho = []
        self.comprador = comprador

    def adicionar_pedido(self, pedido: Pedido()):
        if self.comprador.is_valid_cpf():
            self.carrinho.append(pedido)
            print("CPF inválido")
        # raise ValueError("CPF inválido")

    def valor_final(self, cupom_de_desconto=0):
        valor_total = sum([item.valor_total for item in self.carrinho])
        return valor_total - cupom_de_desconto

    def finalizar_pedido(self):
        if len(self.carrinho) == 0:
            return False
        return True
