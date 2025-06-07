import textwrap

def exibir_menu():
    menu = """\n
    =========================
    Bem-vindo ao Sistema Bancário
    =========================
    
    1. Depositar
    2. Sacar
    3. Exibir Extrato
    4. Cadastrar Usuário
    5. Cadastrar Conta
    6. Listar Usuários
    7. Listar Contas
    0. Sair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, extrato, /, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, extrato, valor, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Não será possível realizar o saque por saldo insuficiente.")
    elif valor > limite:
        print("O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==============================")