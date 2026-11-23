print("--- Sistema de Terminal de Autoatendimento Bancário ---")

for tentativa in range(5):
    correntista = input("Nome do Correntista: ").strip()
    conta = input("Tipo de Conta: ").strip()
    agencia = input("Número da Agência: ").strip()
    cartao = input("Número do Cartão: ").strip()
    saque = input("Valor do Saque: ").strip()
    pin = input("PIN de Segurança: ").strip()
    terminal = input("Código do Terminal: ").strip().upper()
    cidade = input("Cidade do Caixa: ").strip()
    email = input("E-mail de Notificação: ").strip().lower()
    operacao = input("Operação Final (Digite CONCLUIDO): ").strip().upper()

    if correntista.isalpha() and \
       conta.isalpha() and \
       agencia.isdigit() and \
       cartao.isdigit() and \
       saque.isdigit() and \
       pin.isdigit() and \
       terminal.isalnum() and \
       cidade.isalpha() and \
       "@" in email and \
       email.endswith("bank.com") and \
       operacao == "CONCLUIDO":

        print(f"\nSucesso: Saque realizado para o cliente {correntista}!")
        break

    else:

        print(f"\nERRO: Dados inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)

else:

    print("\nBLOQUEADO: Limite de 5 tentativas excedido.")
