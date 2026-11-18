print("-------------Pontuário de Clínica Vetrinária-------------")
pet = input("Digite o nome do pet:").strip()
especie = input("Digite a espécie do pet:").strip()
raca = input("Digite a raça do pet:").strip()
idade = input("Digite a idade do pet:").strip()
peso = input("Digite o peso do pet:").strip()
tutor = input("Digite o nome do tutor do pet:").strip()
CPF = input("Digite o CPF do tutor (somente números):").strip()
email = input("Digite o E-mail do tutor:").strip()
fone = input("Digite o telefone de contato do tutor (somente números):").strip()
vacina = input("Digite o nome da última vacina aplicada no pet:").strip()
clinica = input("Digite o nome da clínica onde o pet é atendido:").strip()
veterinário = input("Digite o nome do veterinário responsável pelo pet:").strip()
CRMV = input("Digite o número do CRMV do veterinário (somente números):").strip()
data = input("Digite a data da consulta (DD/MM/AAAA):").strip()
status = input("Digite o status do pet (Digite 'OK' para confirmar):").strip().upper()
if especie.isalpha() and raca.isalpha() and idade.isdigit() and peso.isdigit() and\
    CPF.isdigit() and CPF == 11 and CRMV.isdigit() and clinica.isupper() and status.isupper() and\
        tutor.istitle() and vacina.isalnum() and email.count("@") == 1 and email.endswith(".com") and\
            fone.isdigit() and len(fone) == 11 and data.count("/") == 2 and status == "OK":
                print(f"Sucesso: O pet {pet} do tutor {tutor} foi registrado com sucesso!")
else:    
    print("Erro: Dados inválidos. O registro do pet falhou.")