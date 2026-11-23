print("-----Sistema de Exportação de Carnes Refrigeradas-----")

auditor = input("Nome do Auditor: ").strip()
empresa = input("Empresa de Refrigeração: ").strip()
corte = input("Tipo de Corte: ").strip()
porto = input("Porto de Exportação: ").strip()
container = input("Código do Contêiner: ").strip()
certificado = input("Certificado: ").strip()
temperatura = input("Temperatura: ").strip()
peso = input("Peso da Carga: ").strip()
data = input("Data da Exportação (DD/MM/AAAA): ").strip()
email = input("E-mail do MAPA: ").strip()
lacre = input("Lacre Eletrônico: ").strip()
status = input("Status (LIBERADO): ").strip()

if auditor.isalpha() and \
empresa.isalpha() and \
corte.isalpha() and \
porto.isalpha() and \
container.startswith("REEFER-") and container[7:].isalnum() and \
certificado.isalnum() and \
temperatura.isdigit() and \
peso.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".mapa.gov.br") and \
lacre.isalnum() and \
status == "LIBERADO":

    print("Carga liberada para exportação!")
else:
    print("Dados inválidos!")

print("-" * 30)