print("---voo--")
for tentativa in range(5):
    prefixo = input("Qual o prefixo da aeronava: ").strip()
    companhia = input("Digite a companhia: ").strip()
    cod_voo = input("Digite o codigo de voo: ").strip()
    altitude= input("Digite a altitude do cruzeiro: ").strip()
    velocidade = input("Digite a velocidade em nós: ").strip()
    email = input ("Qual o email?: ").strip()
    pista = input("Informe a pista de pouso:")
    aeroporto = input("informe o aeroporto de destino: ").strip()
    cod_transporte = input("Digite o codigo de transporte: ").strip()
    Confirmação = input("Status: ").strip()

    if companhia.isalpha() and\
    aeroporto.isalpha() and\
    prefixo.isalnum() and\
    cod_voo.isalnumt() and\
    pista.isalnum() and\
    altitude.isdigit() and\
    velocidade.isalpha() and\
    cod_transporte.isdigit() and\
    email.endswith("@aircontrol") and\
    len(cod_transporte) == 6 and \
    Confirmação == "PERMITIDO":
       print(f"\nSUCESSO: Banco {prefixo}, com o codigo terminal {cod_voo} liberado!") 
       break
    else:
        print(f"\nERRO: Dados Inválidos! {tentativa + 1} de 5.")
        print("-"*40)
else:
    print("\nBLOQUEADO: Limite e 5 tentativas excedido.")
