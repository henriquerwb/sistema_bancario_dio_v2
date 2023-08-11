def menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [q] Sair

=> """
    return input(menu)

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("Operação não concluída. Valor inválido.")
        return saldo, extrato

    if valor > saldo:
        print("Operação não concluída. Saldo indisponível.")
    elif valor > limite:
        print("Operação não concluída. Limite de saque indisponível.")
    elif numero_saques >= limite_saques:
        print("Operação não concluída. Quantidade de saques excedida.")
    else:
        saldo -= valor
        extrato.append(f'SAQUE: {valor} R$')
        numero_saques += 1
        print("Saque realizado com sucesso.")
    
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato):
    if valor <= 0:
        print("Operação não concluída. Valor inválido.")
        return saldo, extrato
    
    saldo += valor
    extrato.append(f'DEPÓSITO: {valor} R$')
    print("Depósito realizado com sucesso.")
    
    return saldo, extrato

def gerar_extrato(saldo, extrato):
    print("Extrato")
    for transacao in extrato:
        print(transacao)
    print(f'Saldo atual: {saldo} R$')

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado.")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    numero_saques = 0
    usuarios = []
    contas = []
    extrato = []

    while True:
        opcao = menu()

        if opcao.lower() == "d":
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao.lower() == "s":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao.lower() == "e":
            gerar_extrato(saldo, extrato)

        elif opcao.lower() == "nu":
            criar_usuario(usuarios)

        elif opcao.lower() == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao.lower() == "q":
            break

        else:
            print("Operação inválida")

if __name__ == "__main__":
    main()
