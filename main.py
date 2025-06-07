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

