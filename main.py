from pprint import pprint

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

# cliente = Cliente('Lucas', ' 123.456.789-00', 'Dev')

# pprint(cliente.__dict__, width = 40)

# cliente.idade = 20

# print(cliente.idade)

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia
    
    
    def __set_agencia(self, value):
        if not isinstance(value,int):
            raise ValueError('O valor da agencia não é um inteiro!')
        
        if value <= 0:
            raise ValueError('O valor da agencia é menor que zero')
         
        
        self.__agencia = value
        
    @property
    def numero(self):
        return self.__numero
    
    
    def __set_numero(self, value):
        if not isinstance(value,int):
            raise ValueError('O valor da numero não é um inteiro!')
        
        if value <= 0:
            raise ValueError('O valor do numero tem que ser maior que 0!')
            
        
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, value):
        if not isinstance(value,int):
            raise ValueError('O valor da saldo não é um inteiro!')
            
        if value <= 0:
            raise ValueError('O valor da saldo precisa ser maior que 0!')
        
        self.__saldo = value

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

conta_corrente = ContaCorrente(None,'agencia falsa',101)
conta_corrente.agencia = 0 
print(conta_corrente.agencia)