print("----- SISTEMA HOSPITALAR DE UTI -----")

for tentativa in range(5):
    nome_paciente = input("Nome do Paciente: ").strip()
    especialidade = input("Especialidade Médica: ").strip()
    crm = input("CRM do Médico: ").strip()
    codigo_leito = input("Código do Leito: ").strip()
    freq_cardiaca = input("Frequência Cardíaca: ").strip()
    pressao = input("Pressão Sistólica: ").strip()
    saturacao = input("Saturação de Oxigênio: ").strip()
    temperatura = input("Temperatura Corporal: ").strip()
    medicamento = input("Medicamento Prescrito: ").strip()
    data_admissao = input("Data da Admissão (DD/MM/AAAA): ").strip()
    email_hospital = input("E-mail do Hospital: ").strip().lower()
    status_clinico = input("Status Clínico (ESTAVEL): ").strip().upper()

    if nome_paciente.isalpha() and \
       especialidade.isalpha() and \
       medicamento.isalpha() and \
       crm.isalnum() and \
       codigo_leito.isalnum() and \
       freq_cardiaca.isdigit() and \
       pressao.isdigit() and \
       saturacao.isdigit() and \
       temperatura.isdigit() and \
       len(crm) == 6 and \
       "@" in email_hospital and \
       email_hospital.endswith(".med.br") and \
       data_admissao.count("/") == 2 and \
       status_clinico == "ESTAVEL":

        print("SUCESSO: Registro do paciente atualizado no sistema de UTI!")
        break
    else:
        print(f"\nERRO: Dados inválidos! Tentativa {tentativa + 1} de 5")
        print("-" * 40)

else:
    print("\nBLOQUEADO: Limite de 5 tentativas excedido. Procure a recepção médica.")