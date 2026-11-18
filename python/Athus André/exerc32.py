print('-----Matrícula de Aluno em Universidade-----')
for tentativa in range(3):
    nome = input("Nome do Aluno: ").strip()
    curso = input("Curso (apenas letras): ").strip()
    matricula = input("Nº Matrícula (6 números): ").strip()
    ano = input("Ano de Ingresso (4 números): ").strip()
    campus = input("Campus (Digite CENTRAL): ").strip()
    senha = input("Crie uma senha: ").strip()

    if nome.isalpha() and curso.isalpha() and \
       len(matricula) == 6 and matricula.isdigit() and \
       len(ano) == 4 and ano.isdigit() and \
       campus == "CENTRAL" and senha != "123456":
        
         print("Matrícula realizada com sucesso!")
         break
    else:
        print("Erro: Verifique os dados.")
        print("-" * 30)
else:
    print("Muitas tentativas. Procure a secretaria.")
print('-'*42)