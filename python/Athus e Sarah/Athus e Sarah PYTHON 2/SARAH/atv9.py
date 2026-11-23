print("-----Sistema de Controle de Drone de Resgate-----")

piloto = input("Nome do Piloto: ").strip()
regiao = input("Região de Busca: ").strip()
cidade = input("Cidade da Base: ").strip()
missao = input("Tipo de Missão: ").strip()
drone = input("Prefixo do Drone: ").strip()
canal = input("Canal do Transmissor: ").strip()
altitude = input("Altitude: ").strip()
bateria = input("Bateria em Porcentagem: ").strip()
data = input("Data da Missão (DD/MM/AAAA): ").strip()
email = input("E-mail dos Bombeiros: ").strip()
chave = input("Chave de Ativação do Motor: ").strip()
status = input("Status (CONECTADO): ").strip()

if piloto.isalpha() and \
regiao.isalpha() and \
cidade.isalpha() and \
missao.isalpha() and \
drone.startswith("DRONE-") and drone[6:].isalnum() and \
canal.isalnum() and \
altitude.isdigit() and \
bateria.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".bombeiros.gov.br") and \
chave.isalnum() and \
status == "CONECTADO":

    print("Drone conectado!")
else:
    print("Dados inválidos!")

print("-" * 30)