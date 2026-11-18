print("---- PRONTUÁRIO MÉDICO DE UTI ----")

for tentativa in range(3):

    paciente = input("Digite o nome do paciente: ").strip()
    medico = input("Digite o nome do médico: ").strip()
    leito = input("Digite o número do leito (NUMEROS): ").strip()
    crm = input("Digite o CRM do médico(NUMERO): ").strip()
    batimentos = input("Digite os batimentos cardíacos(NUMERO): ").strip()
    tipo_sanguineo = input("Digite o tipo sanguíneo (o+): ").strip().upper()
    alergia = input("Digite a alergia (nao pode ser nada): ").strip().upper()

    if paciente.isalpha() and medico.isalpha() and \
       leito.isdigit() and crm.isdigit() and \
       batimentos.isdigit() and \
       tipo_sanguineo in ["O+"] and \
       alergia != "NADA":

        print(f"Cadastro aprovado! Paciente {paciente} registrado na UTI.")
        break

    else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3.")

else:
    print("SISTEMA BLOQUEADO. Equipe médica acionada.")

