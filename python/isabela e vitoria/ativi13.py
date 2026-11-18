print("--- GESTÃO DE FROTA E TELEMETRIA VEICULAR PESADA ---")

for tentativa in range(5):
    nome = input("Nome do Motorista: ").strip()
    sobrenome = input("Sobrenome: ").strip()
    cidade_saida = input("Cidade de Saída: ").strip()
    cidade_chegada = input("Cidade de Chegada: ").strip()
    placa = input("Placa do Caminhão: ").strip()
    chassi = input("Chassi do Veículo: ").strip()
    quilometragem = input("Quilometragem Atual: ").strip()
    tanque = input("Capacidade do Tanque: ").strip()
    codigo_carga = input("Código da Carga: ").strip()
    data_viagem = input("Data da Viagem (DD/MM/AAAA): ").strip()
    email = input("E-mail da Central: ").strip()
    autorizacao = input("Autorização da Viagem: ").strip()

    if nome.isalpha() and \
       sobrenome.isalpha() and \
       cidade_saida.isalpha() and \
       cidade_chegada.isalpha() and \
       placa.isalnum() and \
       chassi.isalnum() and \
       codigo_carga.isalnum() and \
       quilometragem.isdigit() and \
       tanque.isdigit() and \
       len(placa) == 7 and \
       email.endswith(".transporte.com") and \
       autorizacao == "AUTORIZADO":

        print("\nSUCESSO: Viagem autorizada!")
        print(f"Motorista: {nome} {sobrenome}")
        print(f"Rota: {cidade_saida} -> {cidade_chegada}")
        print(f"Placa: {placa}")
        print(f"Chassi: {chassi}")
        print(f"Quilometragem: {quilometragem} km")
        print(f"Capacidade do Tanque: {tanque}")
        print(f"Código da Carga: {codigo_carga}")
        print(f"Data da Viagem: {data_viagem}")
        print(f"E-mail da Central: {email}")
        print(f"Autorização: {autorizacao}")
        break

    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)

else:
    print("\nBLOQUEADO: Limite de 5 tentativas atingido.")
    print("Contate o suporte técnico.")

