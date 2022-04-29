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
        cpf = self.clean_cpf()
        if self.is_valid_len(cpf):
            return False
        if self.is_identical_digits(cpf):
            return False
        dg1 = self.calculate_check_digits(cpf, 10)
        dg2 = self.calculate_check_digits(cpf, 11)
        check_digit = self.extract_check_digits(cpf)
        calculated_check_digit = f"{dg1}{dg2}"
        return check_digit == calculated_check_digit

    def clean_cpf(self):
        return re.sub(r"[^\d]+", "", self.cpf)

    def is_valid_len(self, clean_cpf):
        return len(clean_cpf) != 11

    def is_identical_digits(self, clean_cpf):
        first_digit = clean_cpf[0:1]
        return all([first_digit == item for item in clean_cpf])

    def calculate_check_digits(self, clean_cpf, factor):
        total = 0
        for digit in clean_cpf:
            if factor > 1:
                factor -= 1
                total += int(digit) * factor
        rest = total % 11
        return 0 if rest < 2 else 11 - rest

    def extract_check_digits(self, clean_cpf):
        return clean_cpf[-2:]


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
