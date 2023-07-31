menu= """"

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo=0
limite=500
extrato="Esse é o seu extrato:\n"
numero_de_saques=0
LIMITE_SAQUES=3
while True:
    opcao=input(menu)
    if opcao=="d":
        deposito=float(input("Insira um valor para depósito:"))
        saldo+=deposito
        extrato+=("Valor depositado: ${:.2f}. Saldo final={:.2f}\n".format(deposito,saldo))
        print("Seu depósito foi realizado!")
    elif opcao=="s":
        if saldo<500:
            print("Seu saldo é menor que a quantidade miníma permitida para saque.Você irá retornar para a tela de menu.")
        elif numero_de_saques>=LIMITE_SAQUES:
            print("Você atingiu o limite de saques diários. Tente novamente no dia seguinte.")
        else:
            saque=float(input("Insira um valor para saque:"))
            if saque>limite:
                print("O valor digitado é maior que o limite de $500.00, tentar novamente com valor menor.")
            else:
                saldo-=saque
                extrato+=("Valor sacado: ${:.2f}. Saldo final={:.2f}\n".format(saque,saldo))
                numero_de_saques+=1
                print("Seu saque foi realizado!")
    elif opcao=="e":
        if extrato=="Esse é o seu extrato:\n":
            print("Não foram realizadas movimentações")
        else:
            print(extrato)
    elif opcao=="q":
        break