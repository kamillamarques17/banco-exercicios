print("-----Auditoria e Folha de Pagamento Corporativa-----")

for Tentativa in range(5):
    nome = input("Nome do Funcionário: ").strip()
    departamento = input("Departamento: ").strip()
    matricula = input("Matrícula Funcional: ").strip()
    cargo = input("Cargo Ocupado: ").strip()
    salario = input("Salário Base: ").strip()
    horas = input("Horas Trabalhadas: ").strip()
    banco = input("Código do Banco: ").strip()
    conta = input("Conta Corrente: ").strip()
    email = input("E-mail Corporativo: ").strip().lower()
    auditoria = input("Parecer da Auditoria: ").strip().upper()

    if nome.isalpha() and departamento.isalpha() and \
       matricula.isalnum() and len(matricula) == 6 and \
       salario.isdigit() and   horas.isdigit() and \
       banco.isdigit() and \
       email.endswith("@empresa.com") and \
       auditoria == "VALIDADO":

        print(
            f"\nSUCESSO: funcionário {nome}, "
            f"parecer {auditoria} registrado."
        )
        break

    else:

        print(f"\nERRO: cadastro inválido, Tentativa {Tentativa + 1} de 5")
        print("-" * 40)

else:

    print("\nBLOQUEADO: Limite de 5 tentativas excedido.")
