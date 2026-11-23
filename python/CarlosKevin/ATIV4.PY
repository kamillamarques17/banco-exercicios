print ("--- TRIAGEM E PRONTUARIO MEDICO HOSPITALAR ---")

for tentativa in range(5):
    #colentando e tartando os dados na entrada 
    nome = input("Nome dO Paciente: ").strip()
    especialidade = input("Especialidade Medica: ").strip()
    numero_prontuario = input("Numero do Prontuario: ").strip()
    crm = input("CRM do Medico: ").strip() 
    codigo = input("Codigo do Convenio: ").strip()
    bpm = input("Batimentos Cardiacos: ").strip()
    temperatura = input("Temperatura Corporal: ").strip()
    sala = input("Sala de Atendimento: ").strip()
    email = input("E-mail do Hospital: ").strip()
    status = input("Status da Triagem : ").strip()

    #VALIDAÇAO DIRETA COM IF + QUEBRA DE LINHA (\)
    if nome.isalpha() and \
       especialidade.isalpha() and \
       numero_prontuario.isdigit() and \
       bpm.isdigit() and \
       sala.isdigit() and \
       len(crm).isalnum() == 7  and \
       codigo.isalnum() and \
       email.count("@") == 1 and email.endswith(".med.br") and \
       status == "URGENTE":

        print(f"\nSUCESSO: TRIAGEM {status}, PRONTUARIO {numero_prontuario} liberado!")
        break
    else:
        #Exibe a tentativa amigavel (1 a 5)
        print(f"nERRO: Dados Ivalido! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEAO: Limite de 5 tentativas excedido. Procure o Diretor da Base.")


