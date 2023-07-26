def menu(): 
    menu = """[1] Sacar \n[2] Depositar \n[3] Consultar Extrato \n[4] Cadastrar novo usuário \n[5] Criar Conta \n[6] Listar Contas \n[0] Sair """
    return input((menu))


def cadastrar_usuario(cpf, nome, data_de_nascimento, endereco, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Já existe um usuário com esse CPF.")
            return
                
    novo_usuario = {
        'cpf': cpf,
        'nome': nome,
        'data_de_nascimento': data_de_nascimento,
        'endereco': endereco
    }

    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")

def criar_conta(agencia, numero_da_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Conta criada com sucesso!")
            return {"agencia": agencia, "numero_da_conta": numero_da_conta, "usuario": usuario}


def sacar(saldo, valor_do_saque, numero_de_saques, limite_de_saques, extrato):
    
    if valor_do_saque <= saldo and numero_de_saques < 3 and valor_do_saque <= limite_de_saques:
        saldo -= valor_do_saque
        numero_de_saques += 1
        extrato += f"Saque:\t\tR$ {valor_do_saque:.2f}\n"

        print("Saque realizado.")
        if numero_de_saques >= 3:
            print("Limite diário de saque excedido.")
    else:
        print("Não foi possível realizar o saque.")

    return saldo, numero_de_saques, extrato

def depositar(saldo, valor_do_deposito, numero_de_depositos, extrato):
    
    if valor_do_deposito > 0:
        saldo += valor_do_deposito
        numero_de_depositos += 1
        extrato += f"Depósito:\tR$ {valor_do_deposito:.2f}\n"
        print("Depósito realizado.")
    else:
        print("Depósito não realizado. Valor inválido.")
    return saldo, numero_de_depositos, extrato

def visualizar_extrato(saldo, numero_de_saques, numero_de_depositos, extrato):
    if numero_de_saques == 0 and numero_de_depositos == 0:
            print("Não foram realizadas operações")

    else:
            print(f"Você realizou {numero_de_saques} saques.")
            print(f"Você realizou {numero_de_depositos} depósitos.")
            print(f"Seu saldo é R$ {saldo:.2f}\n")

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_da_conta']}")
        print(f"Usuário: {conta['usuario']['nome']}")       

def main():
    saldo = 2000
    limite = 500
    numero_de_saques = 0
    numero_de_depositos = 0
    limite_de_saques = 3
    extrato = ""
    usuarios = []
    contas = []
    agencia = "0001"

    while True:
        opcao = menu()

        if opcao == "0":
            print("Obrigada por ser nosso cliente!")
            break

        elif opcao == "1":
            valor_do_saque = int(input("Informe o valor do saque: "))
            saldo, numero_de_saques, extrato = sacar(saldo, valor_do_saque, numero_de_saques, limite, extrato)

        elif opcao == "2":
            valor_do_deposito = int(input("Informe o valor do depósito: "))
            saldo, numero_de_depositos, extrato= depositar(saldo, valor_do_deposito, numero_de_depositos, extrato)

        elif opcao == "3":
            visualizar_extrato(saldo, numero_de_saques, numero_de_depositos, extrato)
        
        elif opcao == "4":
            cpf = input("Digite o CPF do usuário: ")
            nome = input("Digite o nome do usuário: ")
            data_de_nascimento = input("Digite a data de nascimento do usuário (formato DD/MM/AAAA): ")
            endereco = input("Digite o endereço do usuário: ")

            cadastrar_usuario(cpf, nome, data_de_nascimento, endereco, usuarios)
        
        elif opcao == "5":
             numero_da_conta = len(contas) + 1
             conta = criar_conta(agencia, numero_da_conta, usuarios)

             if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        else:
            print("Opção inválida. Digite um número válido.")

main()