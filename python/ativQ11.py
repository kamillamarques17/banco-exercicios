print("--- CONTROLE DE ACESSO AO DATACENTER ---")
for tentativa in range(5):
    especialista = input("Nome do Especialista: ").strip().title()
    area = input("Área de Atuação: ").strip().title()
    empresa = input("Empresa Contratada: ").strip().upper()
    cidade = input("Cidade da Sede: ").strip().title()
    rack = input("Código do Rack: ").strip()
    id_gab = input("ID do Gabinete: ").strip()
    temp = input("Temperatura do Corredor Frio: ").strip()
    umidade = input("Umidade Relativa do Ar: ").strip()
    data = input("Data do Acesso (DD-MM-AAAA): ").strip()
    email = input("E-mail Corporativo: ").strip().lower()
    senha = input("Senha Biométrica: ").strip()
    liberacao = input("Liberação da Porta (ABERTO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if especialista.isalpha() and \
       area.isalpha() and \
       cidade.isalpha() and \
       rack.startswith("RACK-") and \
       id_gab.isalnum() and \
       temp.isdigit() and \
       umidade.isdigit() and \
       data_formatada.count("/") == 2 and \
       len(data_formatada) == 10 and \
       email.endswith(".datacenter.com") and \
       liberacao == "ABERTO":
        
        senha_oculta = "*" * len(senha)
        print(f"\nSUCESSO: Especialista {especialista} da empresa {empresa} acessou o rack {rack}!")
        print(f"Data Padronizada: {data_formatada} | Senha Protegida: {senha_oculta}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")