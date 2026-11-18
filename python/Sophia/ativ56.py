print("---------PAINEL DE CONTROLE DE UM FOQUETE ESPACIAL---------")
for tentativa in range(3): 
    Nome_missão = input("Informe o nome da missão: ").strip() 
    Código_foquete = input("Informe o código do foquete: ").strip() 
    Data_lançamento = input("(DD/MM/AAAA): ").strip() 
    ID_digital = input("Id digital do Astronauta: ").strip() 
    email_base = input("Digite o e-mail da base: ").strip() 
    Combustível = input("Informe o combústivel: ").strip() 
    Carga_espacial = input("Digite a carga espacial: ").strip().upper() 
    Status_sistema = input("Digite o status: ").strip() 
    
    if Código_foquete.isalnum() and Carga_espacial.isalnum() and ID_digital.isdigit() and \
       Combustível.isdigit() and Data_lançamento.count("/") == 2 and email_base.count("@") and email_base.endswith(".com") and \
       Status_sistema == "APROVADO":
        
        print(f"Cadastro realizado!")
        break
    else:
         print(f"ERRO: Tente novamente!.")
         print("-" * 40)
else:
    print("BLOQUEADO: Muitas falhas.")