print("-----Sistema de Registro de Transplantes-----")

paciente = input("Nome do Paciente: ").strip()
orgao = input("Órgão para Transplante: ").strip()
hospital = input("Nome do Hospital: ").strip()
cirurgiao = input("Nome do Cirurgião: ").strip()
protocolo = input("Protocolo Médico: ").strip()
crm = input("CRM do Cirurgião: ").strip()
temperatura = input("Temperatura Corporal: ").strip()
batimentos = input("Batimentos Cardíacos: ").strip()
data = input("Data do Registro (DD/MM/AAAA): ").strip()
email = input("E-mail Médico: ").strip()
senha = input("Senha de Acesso: ").strip()
status = input("Status (COMPATIVEL): ").strip()

if paciente.isalpha() and \
orgao.isalpha() and \
hospital.isalpha() and hospital == hospital.upper() and \
cirurgiao.isalpha() and \
protocolo.startswith("MED-") and protocolo[4:].isalnum() and \
crm.isalnum() and len(crm) == 6 and \
temperatura.isdigit() and \
batimentos.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".saude.gov.br") and \
senha.isalnum() and \
status == "COMPATIVEL":

    print("Registro compatível!")
else:
    print("Dados inválidos!")

print("-" * 30)