print("--------Controle de estoque industrial--------")
for tentativa in range (3):
    máquina = input ("Qual a máquina?:").strip()
    série = input ("Informe a serie: ").strip()
    operador = input ("Nome do operador: ").strip()
    turno = input ("Digite o turno:").strip()
    peças_dias = input("Informe as peças: ").strip()
    defeitos = input("Informe os defeitos: ").strip()
    email_t = input("Digite o e-mail: ").strip()
    fábrica = input ("Digite a fábrica: ").strip()
    setor = input ("Informe o setor: ").strip()
    corredor = input("Informe o corredor: ").strip()
    gaveta = input("Informe a gaveta:").strip()
    fornecedor =  input ("Nome do fornecedor: ").strip()
    CNPJ_F = input("CNPJ: ").strip()
    data_manut = input ("(DD/MM/AAAA): ").strip()
    status = input ("Qual o status: ").strip()

    if setor.isalpha() and fornecedor.isalpha() and\
    peças_dias.isdigit() and defeitos.isdigit() and gaveta.isdigit() and CNPJ_F.isdigit() and \
    máquina.upper() and turno.upper() and fábrica.upper() and status.upper() =="OPERACIONAL" and \
    série.isalnum() and operador and email_t.count("@") == 1 and email_t.count(".com") and \
    data_manut.count("/"):
        
        print(f"controle realizado!")
        break
    else:
        print(f"Erro: TENTE NOAVMENTE!")
        print("-"*40)

else:
    print("BLOQUEADO: muitas tentativas falhas.")

