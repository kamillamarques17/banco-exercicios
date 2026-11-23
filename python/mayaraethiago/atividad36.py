print("-----------Validação de embarque Nacional-----------")
sub = input("Qual substância você deseja licenciar? ")
tipo = input("Tipo: ")
lote = input("Lote: ")
resp = input("Nome do(a) resposnsável: ")
crm = input("Nº CRM: ")
validade = input("Validade: ")

if len(crm) == 5 and len(validade) == 8 and \
tipo == "SOLVENTE" and lote != "000":
    print("Reservado com sucessso!")
print("-"*50)