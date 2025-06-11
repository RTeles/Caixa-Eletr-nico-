#criar uma classe para as contas bancárias

class Conta:
    #Atributos
    def __init__(self,nome,cpf,dt_nsc,conta,saldo,senha):
        self.nome = nome
        self.cpf = cpf
        self.dt_nsc = dt_nsc
        self.conta = conta
        self.saldo = saldo
        self.senha = senha

    def verificar_senha(self, senha_digitada):
        return self.senha == senha_digitada

    def sacar(self):
        valor = float(input('Digite o valor do saque. R$'))
        if self.saldo < valor:
            print('Transação negada, Saldo Insuficiente!')
        else:
            self.saldo -= valor
            print('Aguarde a contagem das notas.')
            print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            print(f'Seu novo saldo é de R$ {self.saldo:.2f}.')

    def depositar(self):
        print(f"Confirme os dados da sua conta para depósito:")
        print(f"Nome: {self.nome}")
        print(f"Conta: {self.conta}")
        confirmacao = int(input("Deseja confirmar o depósito nesta conta? (1) para Sim e (2) para Não.\n: "))

        if confirmacao == 1:
            valor = float(input('Digite o valor a ser depositado. R$:'))
            if valor > 0:
                self.saldo += valor
                print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        elif confirmacao == 2:
            print('Depósito cancelado. ')

    def mostrarSaldo(self): #Funções sempre devem ser um verbo
        print(f'Saldo da conta: {self.conta} R${self.saldo}')


'''lista_de_contas = [10310,10311,10312,10313]
    def buscar_conta(numero_conta):
        for conta in lista_de_contas:
            if conta.conta == numero_conta:
                return conta
        return None'''
