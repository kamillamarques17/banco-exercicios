print("-----Sistema de Perícia Digital-----")

perito = input("Nome do Perito: ").strip()
especialidade = input("Especialidade: ").strip()
departamento = input("Departamento: ").strip()
cidade = input("Cidade: ").strip()
evidencia = input("Código da Evidência: ").strip()
hash = input("Hash SHA256: ").strip()
tamanho = input("Tamanho do Arquivo em MB: ").strip()
lacre = input("Número do Lacre: ").strip()
data = input("Data da Perícia (DD/MM/AAAA): ").strip()
email = input("E-mail Institucional: ").strip()
senha = input("Senha do Cofre: ").strip()
status = input("Status (INTEGRO): ").strip()

if perito.isalpha() and \
especialidade.isalpha() and \
departamento.isalpha() and departamento == departamento.upper() and \
cidade.isalpha() and \
evidencia.startswith("EVID-") and evidencia[5:].isalnum() and \
hash.isalnum() and \
tamanho.isdigit() and \
lacre.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".policia.gov.br") and \
senha.isalnum() and \
status == "INTEGRO":

    print("Evidência íntegra!")
else:
    print("Dados inválidos!")

print("-" * 30)