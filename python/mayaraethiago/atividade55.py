print("---------SISTEMA DE MATRÍCULA UNIVERSITÁRIA---------")
for tentativa in range(3):
    Aluno = input("Informe o nome do aluno: ").strip()
    CPF = input("Informe o CPF: ").strip()
    RG  = input("Informe o RG: ").strip()
    Idade = input("Digite a idade: ").strip()
    Curso = input("Digite o curso: ").strip()
    Semestre = input("Informe o semestre: ").strip()
    Turno = input("Digite o turno: ").strip()
    Campus = input("Digite o campus: ").strip()
    Email_A = input("Informe o e-mail: ").strip()
    RA = input("Informe o RA: ").strip()
    Bolsista = input("Informe se sim/não: ").strip()
    Coordenador = input("Informe o nome do coordenador: ").strip()
    Telefone = input("Informe o telefone: ").strip()
    Data_Matricula = input("(DD/MM/AAAA) ").strip()
    Status = input("Qual os status: ").strip()

    if Aluno.istitle() and Coordenador.istitle() and\
       Curso.isalpha() and Campus.isalpha() and CPF.isdigit() and RG.isdigit() and Idade.isdigit() and Semestre.isdigit() and RA.isdigit() and Telefone.isdigit() and\
       Turno.upper() and Bolsista.upper() and Status.upper() =="REGULAR" and \
       Email_A.count(".com") and \
       Data_Matricula.count(".com"):
       
       print(f"Cadastro realizado!")
       break
    else:
        print(f"ERRO: Tente novamente!.")
        print("-" * 40)
else:
    print("BLOQUEADO: Muitas falhas.")

