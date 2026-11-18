print("----------------DATACENTER SEGURANÇA NACIONAL---------------------")

for tentativas in range(5):
    nome_especialista = input("Nome do Especialista: ").strip()
    area_atuação = input("Digite a area de atuação: ").strip()
    empresa_contratada = input("Digite a empresa contratada: ").strip().upper()
    cidade = input("Digite a cidade sede: ").strip()
    codigo_rack = input("Código rack: ").strip().upper()
    id = input("Digite o ID do gabinete: ").strip()
    temperatura = input("Digite a temperatura do corredor frio: ").strip()
    umidade = input("Umidade relativa do ar: ").strip()
    data = input("Data da Expedição (DD/MM/AAAA): ").strip()
    email = input("E-mail do Comprador: ").strip()
    senha = input("Digite a senha Biometrica: ").strip()
    liberação = input("Status (ABERTO): ").strip()

    if nome_especialista.isalpha() and \
        area_atuação.isalpha() and \
        empresa_contratada.isalpha() and \
        cidade.isalpha() and \
        codigo_rack.startswith("DATA-") and codigo_rack[4:].isalnum() and \
        id.isalnum() and \
        temperatura.isdigit() and \
        umidade.isdigit() and \
        len(data) == 10 and data.count("/") == 2 and \
        email.count("@") and email.endswith(".datacenter.com") and \
        senha.isalnum() and \
        liberação == "ABERTO":

        
        print(f"\nSUCESSO: titular {nome_especialista}, Especialista autorizado!")
        break

    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 5")
        print("-" * 40)

else:
    print("\nAcesso negado")