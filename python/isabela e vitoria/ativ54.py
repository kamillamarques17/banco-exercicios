print("-----------Controle de Estoque Industrial------")

maquina = input("Máquina: ")
serie = input("Série: ")
operador = input("Operador: ")
turno = input("Turno: ")
pecas_dia = input("Peças por dia: ")
defeitos = input("Defeitos: ")
email_t = input("Email: ")
fabrica = input("Fábrica: ")
setor = input("Setor: ")
corredor = input("Corredor: ")
gaveta = input("Gaveta: ")
fornecedor = input("Fornecedor: ")
cnpj_f = input("CNPJ fornecedor: ")
data_manut = input("Data manutenção: ")
status = input("Status: ")

if (setor.isalpha() and
    fornecedor.isalpha() and
    pecas_dia.isdigit() and
    defeitos.isdigit() and
    gaveta.isdigit() and
    cnpj_f.isdigit() and len(cnpj_f) == 14 and
    maquina.isupper() and
    turno.isupper() and
    fabrica.isupper() and
    status.isupper() and
    serie.isalnum() and
    "@" in email_t and
    email_t.endswith(".com") and
    data_manut.count("/") == 2 and
    status == "OPERACIONAL"):

    print("Estoque válido!")

else:
    print("Estoque inválido!")



