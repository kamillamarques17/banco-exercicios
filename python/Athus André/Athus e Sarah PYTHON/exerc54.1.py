print('----------Controle de Estoque Industrial----------')

maquina = input("Máquina: ").strip()
serie = input("Série: ").strip()
operador = input("Operador: ").strip()
turno = input("Turno: ").strip()
pecas_dia = input("Peças por dia: ").strip()
defeitos = input("Defeitos: ").strip()
email_t = input("E-mail técnico: ").strip()
fabrica = input("Fábrica: ").strip()
setor = input("Setor: ").strip()
gaveta = input("Gaveta: ").strip()
fornecedor = input("Fornecedor: ").strip()
cnpj_f = input("CNPJ fornecedor: ").strip()
data_manut = input("Data da manutenção (DD/MM/AAAA): ").strip()
status = input("Status: ").strip()

if setor.isalpha() and fornecedor.isalpha() and \
pecas_dia.isdigit() and defeitos.isdigit() and gaveta.isdigit() and cnpj_f.isdigit() and \
maquina.isupper() and turno.isupper() and fabrica.isupper() and status.isupper() and \
serie.isalnum() and operador.isupper() and \
"@" in email_t and email_t.endswith(".com") and \
data_manut.count("/") == 2 and \
status == "OPERACIONAL":

    print("Cadastro realizado com sucesso!")