print("--------Sistema de Matrícula Universitária ------")

aluno = input("Aluno: ")
cpf = input("CPF: ")
rg = input("RG: ")
idade = input("Idade: ")
curso = input("Curso: ")
semestre = input("Semestre: ")
turma = input("Turma: ")
campus = input("Campus: ")
email_a = input("Email: ")
ra = input("RA: ")
bolsista = input("Bolsista: ")
coordenador = input("Coordenador: ")
telefone = input("Telefone: ")
data_matricula = input("Data matrícula: ")
status = input("Status: ")

if (aluno.istitle() and
    coordenador.istitle() and
    curso.isalpha() and
    campus.isalpha() and
    cpf.isdigit() and len(cpf) == 11 and
    rg.isdigit() and
    idade.isdigit() and
    semestre.isdigit() and
    ra.isdigit() and len(ra) == 6 and
    telefone.isdigit() and
    turma.isupper() and
    bolsista.isupper() and
    status.isupper() and
    email_a.endswith(".com") and
    data_matricula.count("/") == 2 and
    status == "REGULAR"):

    print("Matrícula válida!")

else:
    print("Matrícula inválida!")