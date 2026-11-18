print ("-------prontuário veterinaria------")

pet = input("Pet: ")
especie = input("Espécie: ")
raca = input("Raça: ")
idade = input("Idade: ")
peso = input("Peso: ")
tutor = input("Tutor: ")
cpf = input("CPF: ")
email = input("E-mail: ")
fone = input("Fone: ")
vacina = input("Vacina: ")
clinica = input("Clínica: ")
veterinario = input("Veterinário: ")
crmv = input("CRMV: ")
data = input("Data: ")
status = input("Status: ")

if (especie.isalpha() and
    raca.isalpha() and
    idade.isdigit() and
    peso.isdigit() and
    cpf.isdigit() and len(cpf) == 11 and
    crmv.isdigit() and
    clinica.isupper() and
    status.isupper() and
    tutor.istitle() and
    vacina.isalnum() and
    email.endswith(".com") and
    data.count("/") == 2 and
    status == "OK"):

    print("Prontuário válido!")
else:
    print("Prontuário inválido!")





