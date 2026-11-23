print("-----Sistema de Comando Aeroespacial-----")

comandante = input("Nome do Comandante: ").strip()
forca = input("Força Armada: ").strip()
bateria = input("Tipo de Bateria: ").strip()
cidade = input("Cidade de Controle: ").strip()
alvo = input("Código do Alvo: ").strip()
radar = input("Código do Radar 3D: ").strip()
distancia = input("Distância do Vetor: ").strip()
altitude = input("Altitude: ").strip()
data = input("Data da Operação (DD/MM/AAAA): ").strip()
email = input("E-mail Institucional: ").strip()
chave = input("Chave Criptografada: ").strip()
status = input("Status (PRONTO): ").strip()

if comandante.isalpha() and \
forca.isalpha() and \
bateria.isalpha() and \
cidade.isalpha() and \
alvo.startswith("TARGET-") and alvo[7:].isalnum() and \
radar.isalnum() and \
distancia.isdigit() and \
altitude.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".defesa.gov.br") and \
chave.isalnum() and \
status == "PRONTO":

    print("Sistema pronto!")
else:
    print("Dados inválidos!")

print("-" * 30)