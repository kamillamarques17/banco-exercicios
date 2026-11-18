print("--------------------Cadastro de Funcionário Completo---------------------")
Nome = input("Digite o Nome:").strip() 
Cargo = input("Digite a Cargo:").strip() 
Cpf = input("DIgite o Cpf:").strip()
Email = input("Digite o e-mail:").strip()
Senha = input("Digite a senha:").strip()
Turno= input("Digite o turno:").strip()
if len(Nome) >3 and len(Cargo) >3 and len(Cpf) ==11 and len(Email) >10 and len(Senha) ==8 and len(Turno) ==5:
    print("Cadastro de Funcionário completo")
else:
    print("Cadastro realizado")