print("---------------------Sistema de Transporte Ferroviário--------------------------")

for tentativas in range(5):

    maquinista = input("Digite o Nome do Maquinista: ").strip()
    origem = input(" Digite o Terminal de Origem: ").strip()
    destino = input("Digite o Terminal de Destino: ").strip()
    minerio = input(" Digite o Tipo de Minério: ").strip()
    vagao = input("Digite o Código do Vagão: ").strip()
    trem = input("Digite o Número do Trem: ").strip()
    peso = input("Digite o Peso da Carga: ").strip()
    distancia = input("Digite o Distância em Quilômetros: ").strip()
    data = input("Digite a Data do Transporte (DD/MM/AAAA): ").strip()
    email = input("Digite o E-mail Ferroviário: ").strip()
    freio = input("Digite a Chave do Freio: ").strip()
    status = input("Status (VERDE): ").strip()

    if maquinista.isalpha() and \
    origem.isalpha() and \
    destino.isalpha() and \
    minerio.isalpha() and \
    vagao.startswith("CARGA-") and vagao[6:].isalnum() and \
    trem.isalnum() and \
    peso.isdigit() and \
    distancia.isdigit() and \
    len(data) == 10 and data.count("/") == 2 and \
    email.count("@") and email.endswith(".ferrovia.log.br") and \
    freio.isalnum() and \
    status == "VERDE":

        print(f"\nSUCESSO: titular {maquinista}, Maquinista autorizado!")
        break

    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 5")
        print("-" * 40)

else:
    print("\nAcesso negado")