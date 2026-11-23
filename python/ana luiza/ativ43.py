print("----------Cadastro igoroso de paciente em estado critico----------")
for tentativa in range(3):
    paciente = input("Paciente?").strip()
    medico = input("Qual o médico?:")
    leito = input("Qual o leito?:")
    CRM = input("Qual o CRM?:")
    batimentos = input ("Digite os batimentos:")
    tipo_sanguineo = input("Qual o tipo sanguineo: ")
    alergias = input("Tem alguma alergia?: ")

    if paciente.isalpha() and medico.isalpha() and leito.isdigit() and \
    CRM.isdigit() and batimentos.isdigit() and tipo_sanguineo == "O+" and alergias != "NADA":
        
        print("Cadastro concluido!")
        break
    else:
        print("Erro fatal.")
        print("-"*30)

else:
    print("Tentativas bloqueadas")