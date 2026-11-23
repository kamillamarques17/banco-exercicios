print("---PAGAMENTO CORPORATIVO--")
for tentativa in range(5):
    nome_con = input("Nome do conrrentista: ").strip()
    tipo_conta = input("Digite tipo e conta: ").strip()
    num_agência = input("Digite o numero da agencia: ").strip()
    num_cartao= input("Digite o numero do cartao: ").strip()
    valor = input("Digite  o valor do saque: ").strip()
    email = input ("Qual o email?: ").strip()
    PIN = input("Informe seu PIN de segurança:")
    cod_terminal = input("informe o codigo terminal: ").strip()
    cid_caixa = input("Digite a cidade do caixa: ").strip()
    Confirmação = input("Status: ").strip()

    if nome_con.isalpha() and\
    cid_caixa.isalpha() and\
    cod_terminal.isalnum() and\
    num_agência.isdigit() and\
    num_cartao.isdigit() and\
    valor.isdigit() and\
    PIN.isalpha() and\
    email.endswith(".bank.com") and\
    len(PIN) == 4 and \
    Confirmação == "CONCLUIDO":
      print(f"\nSUCESSO: Banco {nome_con}, com o codigo terminal {cod_terminal} liberado!") 
      break
    else:
       print("\nERRO: Dados Inválidos! {tentativa + 1} de 5.")
       print("-"*40)
else:
   print("\nBLOQUEADO: Limite e 5 tentativas excedido.")

   