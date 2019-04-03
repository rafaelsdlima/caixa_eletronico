
__alunos__ = ["rafael.lima@aluno.faculdadeimpacta.com.br",
              "wagner.oliveira@aluno.faculdadeimpacta.com.br"]


class Cliente():
    def __init__(self, nome, telefone, email):
        self._nome = nome
        self._telefone = telefone
        self._email = email

    def telefoneget(self):
        return self._telefone

    def telefoneset(self, value):
        if type(value) == int:
            self._telefone = value
        else:
            print('insira seu telefone corretamente')

    def emailget(self):
        return self._email

    def emailset(self, value):
        if '@' in value:
            self._email = value
        else:
            print('email invalido')


class Banco():
    def __init__(self, nome_banco):
        self._nome = nome_banco
        self._lista_contas = []


class Conta():
    def __init__(self, lista_clientes, numero_conta, saldo_inicial):
        self._numero = numero_conta
        self._saldo = saldo_inicial
        self._clientes = lista_clientes
        self._registro = []
        self._registro.append({'inicial': saldo_inicial})

    def saque(self, valor):
        self._saldo -= valor
        self._registro.append({'saque': valor})

    def deposito(self, valor):
        self._saldo += valor
        self._registro.append({'deposito': valor})

    def extrato(self):
        for i in self._registro:
            print("Extrato CC N° %s\n" % self._numero)
        print("%10s %10.2f" % (i[0], i[1]))
        return ("\n Saldo: %10.2f\n" % self._saldo)

    def resumo(self):
        print("CC N°%s Saldo: %10.2f" % (self._numero, self._saldo))
