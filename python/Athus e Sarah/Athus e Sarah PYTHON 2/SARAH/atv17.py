print("-----Sistema de Registro de Diplomas Acadêmicos-----")

formando = input("Nome do Formando: ").strip()
sobrenome = input("Sobrenome: ").strip()
curso = input("Curso de Formação: ").strip()
campus = input("Cidade do Campus: ").strip()
diploma = input("Código do Diploma: ").strip()
livro = input("Livro de Registro: ").strip()
horas = input("Carga Horária: ").strip()
nota = input("Nota Final: ").strip()
data = input("Data de Emissão (DD/MM/AAAA): ").strip()
email = input("E-mail Universitário: ").strip()
certificado = input("Hash do Certificado: ").strip()
status = input("Status (REGISTRADO): ").strip()

if formando.isalpha() and \
sobrenome.isalpha() and \
curso.isalpha() and \
campus.isalpha() and \
diploma.startswith("DIP-") and diploma[4:].isalnum() and \
livro.isalnum() and \
horas.isdigit() and \
nota.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".universidade.edu.br") and \
certificado.isalnum() and \
status == "REGISTRADO":

    print("Diploma registrado!")
else:
    print("Dados inválidos!")

print("-" * 30)