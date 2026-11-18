print("---- PRONTUÁRIO MÉDICO DE CIRURGIA ROBÓTICA ----")

for tentativa in range(3):

    paciente = input("Paciente: ").strip()
    cpf = input("CPF: ").strip()
    idade = input("Idade: ").strip()
    peso = input("Peso: ").strip()
    altura = input("Altura: ").strip()
    medico = input("Médico: ").strip()
    crm = input("CRM: ").strip()
    robo = input("Robô: ").strip().upper()
    sala = input("Sala: ").strip()
    hospital = input("Hospital: ").strip().upper()
    sangue = input("Tipo sanguíneo: ").strip().upper()
    alergia = input("Alergia: ").strip()
    anestesia = input("Anestesia: ").strip()
    batimentos = input("Batimentos: ").strip()
    oxigenio = input("Oxigênio: ").strip()

    if (paciente.isalpha() and
        medico.isalpha() and
        cpf.isdigit() and len(cpf) == 11 and
        crm.isdigit() and len(crm) == 6 and
        robo == "DA_VINCI" and
        hospital != "TESTE" and
        (len(sangue) == 2 or len(sangue) == 3) and
        batimentos.isdigit() and
        oxigenio.isdigit()):

        print("Prontuário aprovado.")
        break

    else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3.")

else:
    print("SISTEMA BLOQUEADO.")


