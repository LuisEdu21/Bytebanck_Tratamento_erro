from pprint import pprint

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

cliente = Cliente('Lucas', ' 123.456.789-00', 'Dev')

pprint(cliente.__dict__, width = 40)

cliente.idade = 20

print(cliente.idade)