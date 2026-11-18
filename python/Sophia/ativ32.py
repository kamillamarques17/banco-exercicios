for tentativa in range(6):
    nome = input("Nome: ").strip()
    curso = input("curso: ").strip()
    matrícula = input("matrícula (6 dígitos): ").strip()
    ano = input("ano: ").strip()
    campus = input("campus: ").strip()
    senha = input("senha: ").strip()

    if len(nome) > 2 and  nome.isalpha() and len(curso) > 2 and curso.isalpha() and \
       len(matrícula) == 6 and matrícula.isdigit() and \
       len(ano) == 4 and ano.isdigit() and \
       len(campus) == 7 and campus.isdigit() and \
       len(senha) == 6 and senha != "123456":
        
        print("Cadastro realizado!")
        break 
    else: 
        print("Erro: Verificar os dados.")
        print("-" * 30)
else:
    print("Muitas tentativas falhas. Tente mais tarde.")
