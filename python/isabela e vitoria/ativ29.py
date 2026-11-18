print("------------------------- PRONTUÁRIO MÉDICO SIMPLES --------------------------")

paciente = input("Digite o paciente (mais de 4 caracteres): ").strip()
medico = input("Digite o médico (mais de 4 caracteres): ").strip()
CRM = input("Digite o CRM (5 caracteres): ").strip()
hospital = input("Digite o hospital (mais de 4 caracteres): ").strip()
alta = input("Digite a alta (2 caracteres): ").strip()
sintoma = input("Digite o sintoma: ").strip()

if len(sintoma) > 0:

    if (len(paciente) > 4 and
        len(medico) > 4 and
        len(CRM) == 5 and
        len(hospital) > 4 and
        len(alta) == 2):

        print(f"Sucesso! Paciente: {paciente}, Médico: {medico}, CRM: {CRM}, Hospital: {hospital}, Alta: {alta}, Sintoma: {sintoma}")
    else:
        print("Acesso negado, verifique suas respostas")
