from contas import Conta
contas_cadastradas ={}

#contas exemplos
conta1 = Conta('Lazara', 41451803250, '05/05/1990', 10310, 10000, 1234)
contas_cadastradas[conta1.conta] = conta1
conta2 = Conta('Emerson', 31391202170, '02/09/1985', 10311, 1500, 2509)
contas_cadastradas[conta2.conta] = conta2
conta3 = Conta ('Gilberto', 41403356612, '13/01/1980', 10312, 3700, 1301)
contas_cadastradas[conta3.conta] = conta3
conta4 = Conta('Adriana', 21208891112, '07/12/1990', 10313 , 1000, 1290)
contas_cadastradas[conta4.conta] = conta4
conta5 = Conta('Renato', 41755830840, '25/09/1995', 10314 , 25000, 4031)
contas_cadastradas[conta5.conta] = conta5
conta6 = Conta('Maria', 51402238812, '28/03/2001', 10315 , 750, 2803)
contas_cadastradas[conta6.conta] = conta6

def depositar_conta():
    deposito = int(input (f'Digite o número da conta para Depósito: '))
    if deposito in contas_cadastradas:
        conta_alvo = contas_cadastradas.get(deposito)

        if conta_alvo:
            while True:
                opcao = int(input('Digite: \n (1) para Confirmar \n (2) para Cancelar \n '))
                if opcao == 1:
                    conta_alvo.depositar()
                if opcao == 2:
                    print('Obrigado por usar nossos serviços!')
                    break





def acessar_conta():
    escolha = input('Digite o numero da sua conta: ')
    if int(escolha) in contas_cadastradas:
        conta_ativa = contas_cadastradas.get(int(escolha))  # O método .get() é seguro, retorna None se a chave não existir

        if conta_ativa:
            print(f'Conta {conta_ativa.conta} encontrada.')
            senha = int(input('Digite sua senha: '))
            if conta_ativa.verificar_senha(senha):
                print((f'Bem Vindo(a), {conta_ativa.nome}!\n Qual opção Deseja?'))

                while True:
                    opcao = int(input(
                        'Digite: \n (1) para Saque \n (2) para Depósito \n (3) para Saldo \n (4) para Cancelar \n :'))

                    if opcao == 1:  # Saque
                        senha = int(input('Digite sua senha: '))
                        if conta_ativa.verificar_senha(senha):
                            conta_ativa.sacar()
                        else:
                            print('Senha incorreta. Saque cancelado')
                    elif opcao == 2:  # Depósito
                        conta_ativa.depositar()
                    elif opcao == 3:  # Saldo
                        senha = int(input('Digite sua senha: '))
                        if conta_ativa.verificar_senha(senha):
                            conta_ativa.mostrarSaldo()
                    elif opcao == 4:
                        print('Obrigado por usar nossos serviços!')
                        break
                    else:
                        print('Opção inválida.')
            else:
                print('Senha incorreta!')
        else:
            print('Opção Inválida!')
    else:
        print('Conta não encontrada.')

def cadastrar_conta():
    quantidade = int(input('Quantas contas deseja cadastrar? \n: '))
    # i é uma variavel que ira percorrer todos os indices ou posições
    # do intervalo de valores entre 0 e quantidade -1
    # range é uma funcao que retorna um intervalo de valores de 0 ate qnt-1
    for i in range(quantidade):
        print(f'-----Cadastrando conta {i} -----')
        nome = input('Nome do Titular: ')
        cpf = input('CPF: ')
        dt_nsc = input('Data de nascimento (DD/MM/AAAA): ')
        numero_conta = input('Número da conta: ')
        saldo = float(input('Saldo Inicial: R$'))

        # criar um objeto
        nova_conta = Conta(nome, cpf, dt_nsc, numero_conta, saldo)
        # .append() -> Adiciona o item na ultima posição da lista
        contas_cadastradas.append(nova_conta)
        # fim do loop

    print('-----Contas Cadastradas-----')
    for conta in contas_cadastradas:
        print(f'Cliente {conta.nome} -- Conta {conta.conta}')
        print(f'CPF {conta.cpf}')
        print(f'Saldo: R$ {conta.saldo}')
        print('-----*****-----')

    # criando um arquivo .txt para gardar nossas informações
    # comando para criar e/ou abrir um arquivo
    with open('contas.txt', 'w', encoding='utf-8') as arq:
        for conta in contas_cadastradas:
            arq.write(f'Cliente: {conta.nome} \n')
            arq.write(f'CPF: {conta.cpf} \n')
            arq.write(f'Data de Nasc.: {conta.dt_nsc} \n')
            arq.write(f'Número da conta: {conta.conta} \n')
            arq.write(f'Saldo: R${conta.saldo} \n')
            arq.write('-------------------------\n')
        print('Contas salvas.')


# Menu principal
while True:
    print('\n----- Senai Bank -----')
    print('(1) Cadastrar Nova Conta')
    print('(2) Acessar Conta Existente')
    print('(3) Realizar Depósito')
    print('(4) Sair')

    try:
        escolha_principal = int(input('Escolha uma opção: '))
    except ValueError:
        print('Opção inválida. Digite apenas números.')
        continue

    if escolha_principal == 1:
        cadastrar_conta()
    elif escolha_principal == 2:
        acessar_conta()
    elif escolha_principal == 3:
        depositar_conta()
    elif escolha_principal == 4:
        print('Encerrando o programa. Até mais!')
        break
    else:
        print('Opção inválida. Por favor, tente novamente.')