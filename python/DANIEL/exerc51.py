print("---Aeronave executiva---")

for tentativa in range(3): 

    pet = input("Digite o nome do pet :").strip()
    especie = input("Digite s especie:").strip()
    raça = input("Digite a raça:").strip()
    idade = input("Digite a idade :").strip()
    peso = input("Digite o peso:").strip()
    tutor = input("Digite o nome do tutor :").strip()
    cpf = input("Digite o seu cpf (11 num):").strip()
    email = input("Digite seu email :").strip()
    fone = input("Digite o fone :").strip()
    vacina = input("Digite a vacina :").strip()
    clinica = input("Digite a clinica:").strip().upper()
    veterinario = input("Digite o nome do vet :").strip()
    crmv = input("Digite o crmv :").strip()
    data = input("Digite a data:").strip().upper()
    status = input("Digite o status:").strip().upper()

    if pet.isalpha() and pet.isalpha() and \
    especie.isalpha() and \
    raça.isalpha() and \
    idade.isdigit() and \
    peso.isdigit() and \
    tutor.isalpha() and \
    cpf.isdigit() and \
    fone.isdigit() and \
    vacina.isalpha() and \
    clinica.isalpha() and \
    veterinario.isalpha() and \
    crmv.isdigit() and \
    len(status) and status.isalpha() == "OK" and \
    data.count("/") == 2 and \
    email.count("@") == 1 and email.endswith(".com"):
        
           print(f"Acesso liberado! Bem-vindo ao sistema, {tutor}.")
           break

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")