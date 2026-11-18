print("----------------Cadastro rigoroso de paciente em estado crítico----------------")
for tentativa in range(3):
    paciente = input("Paciente?").strip()
    médico = input("Qual o médico?: ").strip()
    leito = input("Qual o leito?: ").strip()
    CRM = input("Qual o CRM?: ").strip()
    batimentos = input("Digite a conta?: ").strip()
    tipo_sanguíneo = input("Qual o tipo sanguíneo?: ").strip()
    alergia = input("Tem aguma alergia?: ").strip()
   
    if paciente.isalpha() and médico.isalpha() and leito.isdigit() and \
    CRM.isdigit() and batimentos.isdigit() and tipo_sanguíneo == "O+" and alergia != "NADA":
       
       print("Cadastro concluido!")
       break
    else:
       print("Erro fatal.")
       print("-" * 30)


else:
   print("Tentativas bloqueadas")

