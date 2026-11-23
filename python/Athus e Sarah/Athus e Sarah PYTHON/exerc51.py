print('-----Prontuário de Clínica Veterinária-----')
pet = input("Nome do pet: ").strip()
especie = input("Espécie: ").strip()
raca = input("Raça: ").strip()
idade = input("Idade do pet (Núm.): ").strip()
peso = input("Peso do pet (Núm.): ").strip()
tutor = input("Nome do tutor: ").strip()
cpf = input("Digite o CPF (11 dígi.): ").strip()
email = ("Digite o e-mail: ").strip()
telefone = input("Digite o telefone de contato (Núm.): ").strip()
vacina = input("O pet está com as vacinas em dia (SIM/NÃO)? ").strip()
clinica = print("Nome da clínica: SILK&PETS ")
veterinario = input("Veterinário reponsável: ").strip()
crmv = input("Digite o CRMV do veterinário responsável (Núm.): ").strip()
data = input("Digite a data (DD/MM/AAAA): ").strip()
status = print("Digite o status de atendimento: AGUARDANDO VÉT. RESPONSÁVEL")
if especie.isalpha() and raca.isalpha() and \
idade.isdigit() and peso.isdigit() and cpf.isdigit() and crmv.isdigit() and len(crmv) == 7 and \
len(cpf) == 11 and tutor.istitle() and vacina.isalnum() and \
email.count("@") == 1 and email.endswith(".com") and data.count("/") == 2:
    print("Registrado com sucesso.")
print("-" * 42)