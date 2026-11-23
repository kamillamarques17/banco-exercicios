print("-----Desafio Integrador: Centro Espacial e Telemetria de Satélites-----")

diretor = input("Nome do Diretor: ").strip()
agencia = input("Agência Espacial: ").strip()
satelite = input("Nome do Satélite: ").strip()
transponder = input("Código do Transponder: ").strip()
altitude = input("Altitude Orbital: ").strip()
velocidade = input("Velocidade Orbital: ").strip()
frequencia = input("Frequência de Uplink: ").strip()
potencia = input("Potência dos Painéis: ").strip()
pais = input("País Operador: ").strip()
data = input("Data do Rastreio (DD/MM/AAAA): ").strip()
email = input("E-mail do Centro de Controle: ").strip()
sinal = input("Sinal de Telemetria (SINCRONIZADO): ").strip()

if diretor.isalpha() and \
agencia.isalpha() and \
pais.isalpha() and \
satelite.isalnum() and \
transponder.isalnum() and \
altitude.isdigit() and \
velocidade.isdigit() and \
frequencia.isdigit() and \
potencia.isdigit() and \
len(transponder) == 8 and \
email.count("@") and \
email.endswith(".space.org") and \
sinal == "SINCRONIZADO":

    print("Telemetria sincronizada!")
else:
    print("Dados inválidos!")

print("-" * 30)