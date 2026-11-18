print("--------PRONTUÁRIO DE CLÍNICA VETERENÁRIA---------")
for tentativa in range(3): 
    Pet = input("Informe o pet: ").strip().upper()
    Espécie = input("Qual a espécie: ").strip()
    Raça = input("Qual a raça: ").strip()
    Idade = input("Digite a idade: ").strip()
    Peso = input("Digite o peso: ").strip()
    Tutor = input("Informe o nome do tutor: ").strip()
    CPF = input("Informe o cpf: ").strip()
    email = input("Informe o e-mail: ").strip().lower()
    Fone = input("Informe o telefone: ").strip()
    Vacina = input("Informe a vacina: ").strip()
    Clínica = input("Informe a clínica: ").strip().upper()
    Veterinário = input("Qual o veterinário: ").strip()
    Data = input("Data (DD/MM/AAAA): ").strip()
    CRMV = input("Informe o CRMV: ").strip()
    Status = input("Qual os status: ").strip().upper()

    if Pet.isupper() and \
       Espécie.isalpha()  and \
       Raça.isalpha() and Idade.isdigit() and \
       Peso.isdigit() and Tutor.istitle() and CPF.isdigit() and email.endswith(".com") and \
       Fone.isupper() and Vacina.isalnum() and Clínica.isupper() and Veterinário.isdigit() and Data.count("/") == 2 and \
       CRMV.isdigit() and \
       Status.isupper() == "OK":
     
       print(f"SUCESSO: Seu prontuário foi reaizado!")
       break
    else:
        print(f"ERRO: Dados inválidos! Tentativa {tentativa + 1} de 3.")
        print("-" * 40)
else:
    print("BLOQUEADO: Muitas falhas.")
