menu = ("[1] Sacar \n[2] Depositar \n[3] Consultar Extrato \n[0] Sair ")
saldo = 2000
limite = 500
numero_de_saques = 0
numero_de_depositos = 0

limite_de_saques = 3

while True:
    opcao = input(menu)

    if opcao == "0":
        print("Obrigada por ser nosso cliente!")
        break
    elif opcao == "1": 
        valor_do_saque = int(input("Informe o valor do saque: "))

        if valor_do_saque <= saldo and valor_do_saque <= limite:
            saldo -= valor_do_saque
            numero_de_saques += 1  # Incrementa a quantidade de saques realizados
            print("Saque realizado.")
            if numero_de_saques >=3:
               print("Limite diário de saque excedido.")
        else:
            print("Não foi possível realizar o saque.")
                        
    elif opcao == "2":
        valor_do_deposito = int(input("Informe o valor do depósito: "))

        if valor_do_deposito > 0:
            saldo += valor_do_deposito
            numero_de_depositos +=1
            print("Depósito realizado.")
        else:
            print("Depósito não realizado. Valor inválido.")
    
    elif opcao == "3":
        if numero_de_saques ==0 and numero_de_depositos == 0:
            print("Não foram realizadas operações")
            print(f"Seu saldo é {saldo}")

        else:
          print(f"Você realizou {numero_de_saques} saques.")
          print(f"Você realizou {numero_de_depositos} depósitos.")
          print(f"Seu saldo é {saldo}")
        
    else:
        print("Opção inválida. Digite um número válido.")
