print("----------------MODELO DE AERONAVE--------------")
for tentativa in range(3):
    modelo = input("Qual o modelo:").strip()
    prefixo = input("Informe o prefixo:").strip()
    fabricante = input ("Qual o fabricante:").strip()
    ano = input ("Digite o ano:").strip()
    horas = input("Digite as horas:").strip()
    piloto = input("Informe o nome do piloto:").strip()
    CPF = input("Digite seu CPF:").strip()
    email = input("Digite o email:").strip()
    base = input("Informe a base: ").strip()
    cidade = input("Informe a  cidade:").strip()
    UF = input("Informe o UF:").strip()
    carga = input("Qual a carga:: ").strip()
    tanque = input("Infome o tanque:").strip()
    torre = input("Informe a torre:").strip()
    termos = input("Infome os termos: ").strip().upper()

    if modelo.upper() and \
    prefixo.isalnum() and\
    fabricante.isalpha() and ano.isdigit() and \
    horas.isdigit() and piloto.isalpha() and CPF.isdigit() and email.count("@") == 1 and email.endswith(".com") and\
    base.upper() and cidade.upper() and UF.upper() and carga.isdigit() and tanque.isdigit() and\
    torre.isalnum() and \
    termos == "SIM":
        print(f"SUCESSO: Cadastro!")
        break
    else:
        print(F"ERRO: Tente novamente!")
        print("-"*40)

else:
    print("BLOQUEADO: Muitas falhas.")