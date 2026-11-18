for tentativa in range(6):
    nome = input("Mome:").strip()
    curso = input("Curso:").strip()
    matrícula = input("Matrícula(6 dígitos):").strip()
    ano = input("Ano:").strip()
    campus = input("campus:").strip()
    senha = input("Senha:").strip()
    if len(nome) > 2 and nome.isalpha() and len(curso) > 2 and curso.isalpha() and\
        len (matrícula) == 6 and matrícula.isdigit() and\
        len(ano) == 4 and ano.isdigit() and \
        len(campus) == 7 and campus.isdigit() and \
        len(senha) == 6 and senha != "123456": \
        
        print("cadastro realizado")
        break
    else:
        print("erro: Verificar os dados.")
        print('-' *30)
else:
    print("Muitas tentativas falhas. Tente mais tarde.")