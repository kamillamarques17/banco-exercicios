print("--------REGISTRO DE SOFTWARE EM NUVEM---------")
for tentativa in range(3): 
    App = input("Qual o App: ").strip() 
    Versão = input("Qual a versão: ").strip() 
    Linguagem = input("Qual a linguagem: ").strip() 
    Servidor = input("Digite o servidor: ").strip() 
    IP = input("Digite o IP: ").strip()
    Porta = input("Informe a pota: ").strip() 
    Desenvolvedor = input("Informe o desenvolvedor: ").strip()
    CPF = input("Informe o CPF: ").strip() 
    Email = input("Informe o e-mail: ").strip()
    Empresa = input("Informe a empresa: ").strip() 
    CNPJ = input("Informe o CNPJ: ").strip() 
    País = input("Qual o país? ").strip() 
    Licença = input("lincença: ").strip() 
    Data = input("Data: (DD/MM/AAAA) ").strip()
    Status = input("Qual os status: ").strip().upper() 

    if Linguagem.isalpha() and País.isalpha() and\
       Porta.isdigit() and CPF.isdigit() and CNPJ.isdigit() and Licença.isdigit() and\
       App.upper() and Servidor.upper() and Empresa.upper() and Status.upper() and \
       Versão.isalnum() and Email.endswith(".com") and  Data.count("/") == 2 and  \
       Status == "ATIVO": 
     
       print(f"SUCESSO: Registrado!")
       break
    else:
        print(f"ERRO: Dados inválidos! Tentativa {tentativa + 1} de 3.")
        print("-" * 40)
else:
    print("BLOQUEADO: Muitas falhas.")

