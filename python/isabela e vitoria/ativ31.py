print("------ CADASTRO DE ALUNO NA UNIVERSIDADE ------")

for tentativa in range(2):
    nome = input("Digite o nome: ").strip()
    curso = input("Digite o curso: ").strip()
    matricula = input("Digite a matrícula (6 dígitos): ").strip()
    ano = input("Digite o ano: ").strip()
    campus = input("Digite o campus: ").strip()
    senha = input("Digite a senha: ").strip()

    # .isalpha() -> garante apenas letras
    # .isdigit() -> garante apenas números
    # len() -> valida tamanho
    # == -> exige valor exato
    # != -> impede valor específico

    if nome.isalpha() and \
       curso.isalpha() and \
       len(matricula) == 6 and matricula.isdigit() and \
       len(ano) == 4 and ano.isdigit() and \
       campus == "CENTRAL" and \
       senha != "123456":
        
        print("Cadastro realizado com sucesso!")
        break
    else:
        print("Erro: Verifique os dados digitados.")
        print("-" * 30)