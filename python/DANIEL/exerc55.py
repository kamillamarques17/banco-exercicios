print("------------------- SISTEMA ESTOQUE--------------------")

aluno = input("Aluno: ").strip()
cpf = input("CPF: ").strip()
rg = input("RG: ").strip()
idade = input("Idade: ").strip()
curso = input("Curso: ").strip()
semestre = input("Semestre: ").strip()
turno = input("Turma: ").strip()
campus = input("Campus: ").strip()
email = input("Email: ").strip()
ra = input("RA: ").strip()
bolsista = input("Bolsista (SIM/NÃO): ").strip().upper()
coordenador = input("Coordenador: ").strip()
telefone = input("Telefone: ").strip()
data = input("Data matrícula: ").strip()
status = input("Status: ").strip()

if aluno.isalpha() and aluno.isalpha() and \
    cpf.isdigit() and \
    rg.isdigit() and \
    idade.isdigit() and \
    curso.isalpha() and \
    semestre.isdigit() and \
    turno.isdigit() and \
    campus.isdigit() and len(campus) == 6 and \
    telefone.isdigit() and len(telefone) == 10 and \
    ra.isdigit() and \
    coordenador.isalpha() and \
    bolsista.isalpha() and \
    status == "APROVADO" and \
    data.count("/") == 2 and \
    email.count("@") == 1 and email.endswith(".com"):
                  
            print(f"Acesso liberado! Bem-vindo {aluno}.")
            

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")