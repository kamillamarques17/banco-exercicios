print("-----Sistema de Rastreamento de Satélites-----")

nome = input("Nome do Satélite: ").strip()
sigla = input("Sigla da Agência: ").strip()
operador = input("Nome do Operador: ").strip()
cidade = input("Cidade de Controle: ").strip()
telemetria = input("Código de Telemetria: ").strip()
chave = input("Chave de Acesso: ").strip()
frequencia = input("Frequência: ").strip()
altitude = input("Altitude: ").strip()
data = input("Data de Rastreamento (DD/MM/AAAA): ").strip()
email = input("E-mail Institucional: ").strip()
senha = input("Senha: ").strip()
status = input("Status (CONFIRMADO): ").strip()

if nome.isalpha() and \
sigla.isalpha() and \
operador.isalpha() and \
cidade.isalpha() and \
telemetria.isalnum() and \
chave.startswith("SAT-") and chave[4:].isalnum() and \
frequencia.isdigit() and \
altitude.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".defesa.mil.br") and \
len(senha) >= 8 and \
status == "CONFIRMADO":

    print("Rastreamento confirmado!")
else:
    print("Dados inválidos!")

print("-" * 30)