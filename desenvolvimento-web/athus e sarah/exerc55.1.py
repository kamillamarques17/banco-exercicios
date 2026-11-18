print('----------Sistema de Matrícula Universitária----------')

aluno = input("Nome do aluno: ").strip()
cpf = input("CPF: ").strip()
rg = input("RG: ").strip()
idade = input("Idade: ").strip()
curso = input("Curso: ").strip()
semestre = input("Semestre: ").strip()
turno = input("Turno: ").strip()
campus = input("Campus: ").strip()
email_a = input("E-mail: ").strip()
ra = input("RA: ").strip()
bolsista = input("Bolsista (SIM/NAO): ").strip()
coordenador = input("Coordenador: ").strip()
telefone = input("Telefone: ").strip()
data_matricula = input("Data da matrícula (DD/MM/AAAA): ").strip()
status = input("Status: ").strip()

if aluno.isalpha() and coordenador.isalpha() and \
curso.isalpha() and campus.isalpha() and \
cpf.isdigit() and rg.isdigit() and idade.isdigit() and \
semestre.isdigit() and ra.isdigit() and telefone.isdigit() and \
turno.isupper() and bolsista.isupper() and status.isupper() and \
email_a.endswith(".com") and \
data_matricula.count("/") == 2 and \
status == "REGULAR":

    print("Matrícula realizada com sucesso!")