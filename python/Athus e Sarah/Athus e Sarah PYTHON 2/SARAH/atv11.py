print("-----Sistema de Controle de Datacenter-----")

especialista = input("Nome do Especialista: ").strip()
area = input("Área de Atuação: ").strip()
empresa = input("Nome da Empresa: ").strip()
cidade = input("Cidade: ").strip()
rack = input("Código do Rack: ").strip()
armario = input("ID do Armário: ").strip()
temperatura = input("Temperatura: ").strip()
umidade = input("Umidade: ").strip()
data = input("Data do Acesso (DD/MM/AAAA): ").strip()
email = input("E-mail do Datacenter: ").strip()
senha = input("Senha Biométrica: ").strip()
status = input("Status (ABERTO): ").strip()

if especialista.isalpha() and \
area.isalpha() and \
empresa.isalpha() and empresa == empresa.upper() and \
cidade.isalpha() and \
rack.startswith("RACK-") and rack[5:].isalnum() and \
armario.isalnum() and \
temperatura.isdigit() and \
umidade.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".datacenter.com") and \
senha.isalnum() and \
status == "ABERTO":

    print("Acesso liberado!")
else:
    print("Dados inválidos!")

print("-" * 30)