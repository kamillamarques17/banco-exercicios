print("---------CONTROLE DE ESTOQUE INDUSTRIAL---------")
for tentativa in range(3):
    Máquina = input("Qual a máquina: ").strip()
    Série = input("nforme a série: ").strip()
    Operador  = input("Nome do operador: ").strip()
    Turno = input("Digite o turno: ").strip()
    Peças_Dia = input("Digite as peças: ").strip()
    Defeitos = input("Informe os defeitos: ").strip()
    Email_T = input("Digite o e-mail: ").strip()
    Fábrica = input("Digite a fábrica: ").strip()
    Setor = input("Informe o setor: ").strip()
    Corredor = input("Informe o corredor: ").strip()
    Gaveta = input("Informe a gaveta: ").strip()
    Fornecedor = input("Nome do forncedor: ").strip()
    CNPJ_f = input("CNPJ: ").strip()
    Data_Manut = input("(DD/MM/AAAA) ").strip()
    Status = input("Qual os status: ").strip()

    if Setor.isalpha() and Fornecedor.isalpha() and\
       Peças_Dia.isdigit() and Defeitos.isdigit() and Gaveta.isdigit() and CNPJ_f.isdigit() and\
       Máquina.upper() and Turno.upper() and Fábrica.upper() and Status.upper() =="OPERACIONAL" and \
       Série.isalnum() and Operador.istitle()  and Email_T.count("@") == 1 and Email_T.count(".com") and \
       Data_Manut.count("/"):
       
       print(f"Controle realizado!")
       break
    else:
        print(f"ERRO: Tente novamente!.")
        print("-" * 40)
else:
    print("BLOQUEADO: Muitas falhas.")

