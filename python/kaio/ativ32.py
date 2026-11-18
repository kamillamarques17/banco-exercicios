curso = input("Digite qual e seu curso (Deve conter apenas letras): ").strip()
nome = input("Nome: ").strip()
matricula = input("Digite sua Matricula (Deve conter exatamente 6 numeros): ").strip()
ano = input("Digite o Ano (Deve conter 4 digitos numericos): ").strip()
campus = input("Digite seu campus (Deve ser exatamente igual a Central): ").strip()
senha = input("Digite sua Senha (não pode ser 12345): ").strip()

if curso.isalpha() and \
   nome.isalpha() and \
   len(matricula) == 6 and matricula.isalpha() and \
   len(ano) == 4 and ano.isdigit() and \
   senha.isdigit != "12345" and \
   campus.isalpha == "CENTRAL":

    print("Aluno matriculado com sucesso! Bem-vindo")
else:
    print("Erro: Verifique se esta tudo correto ")
    print("-" * 30)