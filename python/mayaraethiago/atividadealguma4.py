print("--- Sistema de Triagem e Prontuário Médico Hospitalar ---")

for tentativa in range(5):
    nome = input("Nome do Paciente: ").strip()
    especialidade = input("Especialidade Médica: ").strip()
    prontuario = input("Número do Prontuário: ").strip()
    crm = input("CRM do Médico: ").strip().upper()
    convenio = input("Código do Convênio: ").strip().upper()
    bpm = input("Batimentos Cardíacos (BPM): ").strip()
    temperatura = input("Temperatura Corporal: ").strip()
    sala = input("Sala de Atendimento: ").strip()
    email = input("E-mail do Hospital: ").strip().lower()
    status = input("Status da Triagem (Digite URGENTE): ").strip().upper()
    
    if nome.isalpha() and especialidade.isalpha() and \
       prontuario.isdigit() and \
       crm.isalnum() and  len(crm) == 7 and \
       convenio.isalnum() and \
       bpm.isdigit() and \
       temperatura.isdigit() and \
       sala.isdigit() and \
       "@" in email and \
       email.endswith("med.br") and \
       status == "URGENTE":
        print(f"\nSucesso: Paciente {nome}, prontuário {prontuario} registrado com prioridade URGENTE!")
        break

    else:
        print(f"\nERRO: Dados inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)

else:

    print("\nBLOQUEADO: Limite de 5 tentativas excedido. Procure a administração do hospital.")