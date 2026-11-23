print("----------------Cadastro Rioroso de Paciente em Estado Crítico----------------")
for tentativa in range(3):
    paciente = input("Nome: ").strip()
    médico = input("Qual o médico? ").strip()
    leito = input("Qual o leito? ").strip()
    crm = input("Qual o CRM? ").strip()
    batimentos = input("Digite a conta? ").strip()
    tipo_sanguíneo = input("Qual o tipo sanguíneo? ").strip()
    alergia = input("Tem aguma alergia? ").strip()
   
    if paciente.isalpha() and médico.isalpha() and leito.isdigit() and \
    crm.isdigit() and batimentos.isdigit() and tipo_sanguíneo == "O+" and alergia != "NADA":
       print("Cadastro concluido!")
       break
    else:
       print("Erro fatal.")
       print("-" * 30)
else:
   print("Tentativas bloqueadas")