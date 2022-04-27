import re


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
        if self.cpf is None:
            return False
        cpf = re.sub(r"[^\d]+", "", self.cpf)
        if len(self.cpf) != 11:
            return False
        digits_list = [digit for digit in cpf]
        first_digit = digits_list[0]
        if not len([digit for digit in digits_list if digit == first_digit]) == len(digits_list):
            try:
                d1 = 0
                d2 = 0
                dg1 = 0
                dg2 = 0
                rest = 0
                digito = None
                nDigResult = None
                for nCount in range(len(cpf)):
                    nCount += 1
                    digito = int(cpf[nCount -1:nCount])
                    d1 = d1 + (11 - nCount) * digito
                    d2 = d2 + (12 - nCount) * digito
                rest = d1 % 11
                dg1 = 0 if rest < 2 else 11 - rest
                d2 += 2 * dg1
                rest = d2 % 11
                if rest < 2:
                    dg2 = 0
                else:
                    dg2 = 11 - rest
                nDigVerific = cpf[len(cpf)-2:len(cpf)]
                nDigResult = f"{dg1}{dg2}"
                return nDigVerific == nDigResult
            except:
                return False


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
