def exibir_menu():
    print("\n--- Menu Bancário ---")
    print("1. Depósito")
    print("2. Saque")
    print("3. Saldo")  # Opção de Saldo (Extrato)
    print("0. Sair")

def obter_opcao():
    while True:
        try:
            opcao = int(input("Digite a opção: "))
            if opcao < 0 or opcao > 3:
                raise ValueError
            return opcao
        except ValueError:
            print("Opção inválida. Digite um número entre 0 e 3.")

def realizar_deposito(saldo):
    while True:
        try:
            valor = float(input("Digite o valor do deposito: "))
            if valor <= 0:
                print("O valor do depósito deve ser positivo. Tente novamente.")
            else:
                saldo += valor
                print("Depósito realizado com sucesso.")
                return saldo, valor  # Retorna o valor do depósito
        except ValueError:
            print("Entrada inválida. Digite um número.")

def realizar_saque(saldo, saque_diario):
    if saque_diario >= 3:
        print("Você excedeu o limite de saques diários.")
        return saldo, saque_diario, None

    while True:
        try:
            valor = float(input("Digite o valor do saque: "))
            if valor <= 0:
                print("O valor do saque deve ser positivo. Tente novamente.")
            elif valor > 500:
                print("O valor máximo por saque é de R$ 500,00.")
            elif valor > saldo:
                print("Saldo insuficiente para realizar o saque.")
            else:
                saldo -= valor
                saque_diario += 1
                print("Saque realizado com sucesso.")
                return saldo, saque_diario, valor  # Retorna o valor do saque
        except ValueError:
            print("Entrada inválida. Digite um número.")

def exibir_extrato(saldo, movimentacoes):
    print("\n--- Extrato Bancário ---")
    print("-" * 30)  # Linha superior da tabela
    print("{:<15} {:>15}".format("Tipo", "Valor"))  # Cabeçalho da tabela
    print("-" * 30)  # Linha separadora

    if movimentacoes:
        for tipo, valor in movimentacoes:
            print("{:<15} R$ {:>12.2f}".format(tipo, valor))  # Linhas de dados
    else:
        print("{:^30}".format("Não foram realizadas movimentações."))  # Mensagem centralizada

    print("-" * 30)  # Linha inferior da tabela
    print("Saldo atual: R$ {:>12.2f}".format(saldo))  # Saldo formatado

saldo = 0  # Saldo inicial
saques_diarios = 0
movimentacoes = []

while True:
    exibir_menu()
    opcao = obter_opcao()

    if opcao == 1:
        saldo, valor_deposito = realizar_deposito(saldo)
        movimentacoes.append(("Depósito", valor_deposito))  # Registra o depósito
    elif opcao == 2:
        saldo, saques_diarios, valor_saque = realizar_saque(saldo, saques_diarios)
        if valor_saque:  # Verifica se o saque foi realizado
            movimentacoes.append(("Saque", valor_saque))  # Registra o saque
    elif opcao == 3:
        exibir_extrato(saldo, movimentacoes)
    elif opcao == 0:
        print("Saindo do sistema. Até logo!")
        break