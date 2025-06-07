
import textwrap

def menu():
    menu_text = """\n
    ========== MENU ==========
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo Usuário
    [5] Nova Conta
    [6] Listar Usuários
    [7] Listar Contas
    [0] Sair
    => """
    return input(textwrap.dedent(menu_text))

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

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado. Conta não criada.")

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}, CPF: {usuario['cpf']}, Endereço: {usuario['endereco']}")

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                valor=valor,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            cadastrar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_usuarios(usuarios)

        elif opcao == "7":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
