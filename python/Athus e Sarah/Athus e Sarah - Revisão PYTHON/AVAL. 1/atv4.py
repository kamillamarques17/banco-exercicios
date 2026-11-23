print("-----Gestão de Frota e Telemetria Veicular Pesada-----")

nome = input("Nome do Motorista: ").strip()
sobrenome = input("Sobrenome: ").strip()
saida = input("Cidade de Saída: ").strip()
chegada = input("Cidade de Chegada: ").strip()
placa = input("Placa do Caminhão: ").strip()
chassi = input("Chassi do Veículo: ").strip()
quilometragem = input("Quilometragem Atual: ").strip()
tanque = input("Capacidade do Tanque: ").strip()
carga = input("Código da Carga: ").strip()
data = input("Data da Viagem (DD/MM/AAAA): ").strip()
email = input("E-mail da Central: ").strip()
autorizacao = input("Autorização da Viagem (AUTORIZADO): ").strip()

if nome.isalpha() and \
sobrenome.isalpha() and \
saida.isalpha() and \
chegada.isalpha() and \
placa.isalnum() and \
chassi.isalnum() and \
carga.isalnum() and \
quilometragem.isdigit() and \
tanque.isdigit() and \
len(placa) == 7 and \
email.endswith(".transporte.com") and \
autorizacao == "AUTORIZADO":

    print("Viagem autorizada!")
else:
    print("Dados inválidos!")

print("-" * 30)