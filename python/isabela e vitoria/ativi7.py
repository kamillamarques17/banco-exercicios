print("----- AUDITORIA E FOLHA DE PAGAMENTO CORPORATIVA -------")

for tentativa in range(5):
    # Coletando e tratando os dados de entrada
    nome_funcionario = input("Nome do funcionario: ").strip()
    departamento = input("Nome do departamento ").strip()
    matricula = input("matricula funcional: ").strip()
    cargo = input("cargo: ").strip()
    salario = input("salario: ").strip()
    horas = input("número de horas trabalhadas: ").strip()
    codigo= input("qual o codigo do banco: ").strip()
    conta = input("qual a conta: ").strip()
    email = input("email: ").strip()
    status = input("Confirmar status (digite VALIDADO): ").strip().upper()

    # Validação direta com IF + AND
    if nome_funcionario.isalpha() and \
       departamento.isalpha() and \
       matricula.isalnum() and \
       len (matricula) == 6 and \
       salario.isdigit() and \
       horas.isdigit() and \
       codigo.isdigit and \
        email.endswith("@empresa.com") and \
        status == "VALIDADO":

       print(
            f"\nSUCESSO: cliente {nome_funcionario}, "
            f"tudo certo"
        )
       break
    else:
        # Exibe a tentativa amigável (1 a 5)
        print(f"\nERRO: dados inválidos, tentativa {tentativa + 1} de 5")
        print("-" * 40)

else:
 print(
        "\nBLOQUEADO: limite de 5 tentativas excedido. "
        "Procure o suporte da corretora."
    )
