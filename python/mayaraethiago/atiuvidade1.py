print("-----Controle de Acesso-----")

for tentativa in range(5):
    nome = input ("Nome do pesquisador: ").strip()
    sobrenome = input ("Seu sobrenome: ").strip()
    reator = input ("Código do reator: ").strip()
    acesso = input ("Setor de acesso: ").strip()
    radiação = input ("Nível da radiação: ").strip()
    inspeção = input ("(DD/MM/AAAA) ").strip()
    cartão = input ("Cartão de acesso: ").strip()
    crachá = input ("ID de crachá: ").strip()
    núcleo = input ("Temperatura do núcleo: ").strip()
    cidade = input ("Qual a cidade do laboratorio: ").strip()
    email = input ("E-mail institucional: ").strip()
    status = input("Satatus institucional: ").strip()

    if nome.isalpha() and sobrenome.isalpha() and \
          reator.isalnum() and acesso.isalnum() and \
          radiação.isdigit() and inspeção == 10 and \
          cartão.isalnum() and crachá.isdigit() and \
          núcleo.isdigit() and cidade.isalpha() and \
          email.count("@") and email.endswith("gov.br") and \
          status == "APROVADO" :

        print (f"\nSUCESSO: Cadastro realizado {nome}" )
        break
    else:
        print (f"\nERRO: cadastro nao reconhecido {tentativa + 1} de 5" )
        print ("-" * 40 )
         
