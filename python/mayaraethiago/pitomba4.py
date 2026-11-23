print ("-----Gestão de frota-----")

for tentativa in range(5):
    nome = input("Nome do motorista: ").strip()
    sobrenome = input("Sobrenome do motorista: ").strip()
    cidade = input("Cidade de saída: ").strip()
    cidade = input("Cidade de chegada: ").strip()
    placa = input("Placa do caminhão: ").strip()
    chassi = input("Chassi do veículo: ").strip()
    atual = input("Quilometragem atual: ").strip()
    tanque = input("Capacidade do tanque: ").strip()
    carga = input("Código da carga: ").strip()
    data = input("DD/MM/AAAA").strip()
    email = input("E-mail da central: ").strip()
    viagem = input("AUTORIZADO").strip()

    nome.isalpha() and sobrenome.isalpha() and cidade.isalpha and cidade.isalpha() and\
    placa.isalnum() and chassi.isalnum() and carga.isalnum() and atual.isdigit() and\
    tanque.isdigit() and len(placa) == 7 and email.endswith(".transporte.com") and\
    viagem == "AUTORIZADO"

    
    print(
                 f"\nSUCESSO: gestão {nome}, "
                 f"cadastro {viagem} registrado"
            )
    break
              
else:
            print(f"\nERRO: cadastros inválidos, Tentativa {+ 1}de 5")
            print("-" * 40) 