curso = input("digite qual e o seu curso (deve conter apenas letras):").strip()
nome = input("nome :").strip()
matricula = input("digite sua matricula (deve conter exatamente 6 numeros)").strip()
ano = input("digite o ano ( deve conter 4 digitos numericos  )").strip()
campus = input("diite seu campus (deve ser exatamente igual a a central)").strip()
senha = input("digite sua senha ( não pode ser 12345)").strip()

if curso.isalpha() and \
   nome.isalpha() and \
   len(matricula) == 6 and matricula.isalpha() and \
   len(ano) == 4 and ano.isdigit() and \
   senha.isdigit != "12345" and \
   campus.isalpha == " central":

    print("aluno matriculado com sucesso! BEM-VINDO")
else:
    print("erro : verifique se esta tudo correto ")
    print("-" * 30)  