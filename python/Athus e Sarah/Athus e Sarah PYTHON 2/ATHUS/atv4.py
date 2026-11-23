print("-----Sistema de Controle da Usina Termelétrica-----")

engenheiro = input("Nome do Engenheiro: ").strip()
setor = input("Setor: ").strip()
usina = input("Nome da Usina: ").strip()
cidade = input("Cidade: ").strip()
reator = input("Código do Reator: ").strip()
turbina = input("Identificação da Turbina: ").strip()
pressao = input("Pressão: ").strip()
rpm = input("Rotação por Minuto (RPM): ").strip()
data = input("Data da Inspeção (DD/MM/AAAA): ").strip()
email = input("E-mail Institucional: ").strip()
chave = input("Chave de Bypass: ").strip()
status = input("Status (NORMAL): ").strip()

if engenheiro.isalpha() and \
setor.isalpha() and \
usina.isalpha() and usina == usina.upper() and \
cidade.isalpha() and \
reator.startswith("TURB-") and reator[5:].isalnum() and \
turbina.isalnum() and \
pressao.isdigit() and \
rpm.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".energia.ind.br") and \
chave.isalnum() and \
status == "NORMAL":

    print("Usina operando normalmente!")
else:
    print("Dados inválidos!")

print("-" * 30)