print("---PRONTUARIO MEDICO DE CIRURGIA ROBOTICA---")

for tentativa in range(3):

    paciente = input("Digite o nome do pasciente:  ").strip()
    cpf = input("Digite o seu cpf: ").strip()
    idade = input("Digite o sua idade (Apenas numeros): ").strip()
    peso = input("Digite seu peso (Deve conter apenas numeros): ").strip()
    altura = input("Digite sua altura (Deve conter apenas numeros): ").strip()
    medico = input("Digite o nome do medico: ").strip()
    tipo = input("Digite o seu tipo sanguineo (Deve ser O+ ou similar) : ").strip()
    crm = input("Digite se crm (deve conter 6 numeros)")
    alergia = input("Digite sua alergia (Deve pode ser NADA) : ").strip()
    robo = input("Digite o nome do robo (Deve ser DA_VINC)").strip().upper()
    sala = input("Digite o nome da sala").strip()
    hospital = input("Digite o nome do hospital (Não pode )").strip().upper()
    alergia = input("Digite o nome da alergia ").strip()
    anestesia = input("Digite a anestesia").strip()
    batimentos = input("Digite o batimento").strip()
    oxigenio = input("Digite o oxigenio").strip()

    if paciente.isalpha() and paciente.isalpha() and \
       medico.isalpha() and \
       idade.isdigit() and \
       peso.isdigit() and \
       altura.isdigit and \
       crm.isdigit() and \
       cpf.isdigit() and \
       batimentos.isdigit() and \
       oxigenio.isalpha() and \
       len(hospital) and hospital.isalpha() != "TESTE" and \
       len(tipo) > 3 and tipo.isalpha() == "O+" and \
       len(robo) and robo.isdigit() != "DA_VINCI":

        print(f"Acesso liberado! Bem-vindo ao sistema, {paciente}.")
        break

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")