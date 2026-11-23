print("--------Sistema de mátricula--------")
for tentativa in range (3):
    aluno = input ("Nome do aluno:").strip()
    CPF = input ("Informe  o CPF: ").strip()
    RG = input ("Digite seu RG: ").strip()
    idade = input ("Digite sua idade:").strip()
    curso = input("Informe o curso: ").strip()
    semestre = input("Informe o semestre: ").strip()
    turno = input("Digite o turno: ").strip()
    campus = input ("Digite o campus: ").strip()
    email_A= input ("Informe o email: ").strip()
    RA = input("Informe o RA: ").strip()
    bolsista = input("Informe se sim/não:").strip()
    coordenador =  input ("Nome do coordenador: ").strip()
    Telefone = input("Telefone: ").strip()
    data_matricula = input ("(DD/MM/AAAA): ").strip()
    status = input ("Qual o status: ").strip()

    if aluno and coordenador and\
    curso.isalpha() and campus.isalpha() and CPF.isdigit() and RG.isdigit() and idade.isdigit() and semestre.isdigit() and RA.isdigit() and Telefone.isdigit() and \
    turno.upper() and bolsista.upper() and status.upper() =="REGULAR" and \
    email_A.count(".com") and \
    data_matricula.count(".com"):
        
        print(f"controle realizado!")
        break
    else:
        print(f"Erro: TENTE NOAVMENTE!")
        print("-"*40)

else:
    print("BLOQUEADO: muitas tentativas falhas.")

