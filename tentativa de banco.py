# Tentaiva de criar algo com o if/eli/else e todas as estruturas de repetição + métodos de string


banco = "Banco do Nordeste"

mensagem = f""" 
    Seja Bem Vindo ao {banco},
Sua presença é nossa alegria.
        Boas ações!!
"""

print (mensagem)

sistema = int(input(""" 
================MENU==================
       O que deseja fazer ?
    [1] Depositar
    [2] Sacar  
    [3] Ver extrato
       
======================================
       
       """))
                                            # Acima é um exemplo de string multilinha para criação de menu por ex

print(sistema)

saque = 1412
extrato = 1412.00

if sistema == 1: # Escolha da 1 opção
    deposito = float(input("Insira o valor do depósito:"))
    print (f"""Seu depósito de R${deposito:.2f} foi realizado com sucesso. 
Agora você possui R${saque + deposito:.2f} em sua conta bancária.""")

elif sistema == 2: # Escolha da 2 Opção
    sacar = float(input("Insira o valor que deseja sacar:"))
    if sacar == saque or sacar < saque:
        print (f"Saque de R${sacar:.2f} realizado com sucesso. Agora você possui R${saque - sacar:.2f} em sua conta bacária.")
    elif sacar > saque:
        print("Não foi possível realizar a transação.")

else: # Escolha da 3 opção
    print (f"Seu extrato bancário atual é de R${extrato}.")

saida = f""" 

        Obrigado por ser nosso cliente!
    Volte sempre que desejar.
        Att: {banco}.

"""
print (saida)