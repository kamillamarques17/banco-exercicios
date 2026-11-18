print("--------REGISTRO DE AERONAVE EXECUIVA---------")
for tentativa in range(3): 
    Modelo = input("Digite o modelo: ").strip().upper()
    Prefixo = input("Qual o prefixo: ").strip()
    Fabricante = input("Qual o fabricante: ").strip()
    Ano = input("Digite o ano: ").strip()
    Horas = input("Digite as horas: ").strip()
    Piloto = input("Informe o nome do piloto: ").strip()
    CPF = input("Informe o cpf: ").strip()
    email = input("Informe o e-mail: ").strip().lower()
    Base = input("Informe a base: ").strip().upper()
    Cidade = input("Informe a cidade: ").strip()
    UF = input("Informe o UF: ").strip().upper()
    Carga = input("Qual a carga: ").strip()
    Tanque = input("Qual o tanque: ").strip()
    Torre = input("Informe a torre: ").strip().upper()
    Termos = input("Qual os termos: ").strip().upper()

    if Modelo.upper() and \
       Prefixo.isalnum()  and \
       Fabricante.isalpha() and Ano.isdigit() and \
       Horas.isdigit() and Piloto.isalpha() and CPF.isdigit() and email.count("@") == 1 and email.endswith(".com") and \
       Base.upper() and Cidade() and UF.upper() and Carga.isdigit() and Tanque.isdigit() and \
       Torre.isalnum() and \
       Termos =="SIM":
      
       
        print(f"SUCESSO:Seu relatório foi enviado!")
        break
    else:
        print(f"ERRO: Dados inválidos! Tentativa {tentativa + 1} de 3.")
        print("-" * 40)
else:
    print("BLOQUEADO: Muitas falhas. Procure o diretor de segurança.")
