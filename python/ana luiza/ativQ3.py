print("--- CENTRAL DE TRANSPLANTES DE ÓRGÃOS ---")
for tentativa in range(5):
    paciente = input("Nome do Paciente Receptor: ").strip().title()
    orgao = input("Tipo do Órgão: ").strip().title()
    hospital = input("Hospital de Origem: ").strip().upper()
    cirurgiao = input("Médico Cirurgião: ").strip().title()
    protocolo = input("Código do Protocolo: ").strip()
    crm = input("CRM do Médico: ").strip()
    temp = input("Temperatura do Recipiente: ").strip()
    bpm = input("Batimentos Cardíacos: ").strip()
    data = input("Data do Procedimento (DD-MM-AAAA): ").strip()
    email = input("E-mail do SUS: ").strip().lower()
    senha = input("Senha de Abertura do Lacre: ").strip()
    parecer = input("Parecer Médico (COMPATIVEL): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if paciente.isalpha() and \
       orgao.isalpha() and \
       cirurgiao.isalpha() and \
       protocolo.startswith("MED-") and \
       crm.isalnum() and \
       len(crm) == 6 and \
       temp.isdigit() and \
       bpm.isdigit() and \
       data_formatada.count("/") == 2 and \
       email.endswith(".saude.gov.br") and \
       parecer == "COMPATIVEL":
        
        senha_oculta = "*" * len(senha)
        print(f"\nSUCESSO: Paciente {paciente} no hospital {hospital} com cirurgião {cirurgiao}!")
        print(f"Data Padronizada: {data_formatada} | Senha Protegida: {senha_oculta}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")