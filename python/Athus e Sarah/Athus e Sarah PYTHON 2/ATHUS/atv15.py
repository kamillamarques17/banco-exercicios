print("-----Sistema de Controle da Plataforma de Petróleo-----")

supervisor = input("Nome do Supervisor: ").strip()
bacia = input("Bacia Petrolífera: ").strip()
campo = input("Campo de Extração: ").strip()
porto = input("Cidade Portuária: ").strip()
poco = input("Código do Poço: ").strip()
valvula = input("Identificação da Válvula: ").strip()
pressao = input("Pressão: ").strip()
vazao = input("Vazão: ").strip()
data = input("Data da Inspeção (DD/MM/AAAA): ").strip()
email = input("E-mail da Plataforma: ").strip()
emergencia = input("Chave da Válvula de Emergência: ").strip()
status = input("Status (ATIVO): ").strip()

if supervisor.isalpha() and \
bacia.isalpha() and \
campo.isalpha() and \
porto.isalpha() and \
poco.startswith("POCO-") and poco[5:].isalnum() and \
valvula.isalnum() and \
pressao.isdigit() and \
vazao.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".oil.com.br") and \
emergencia.isalnum() and \
status == "ATIVO":

    print("Plataforma ativa!")
else:
    print("Dados inválidos!")

print("-" * 30)