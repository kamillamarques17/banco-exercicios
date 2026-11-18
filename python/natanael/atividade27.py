print("-------------------------------Cadastro de Funcionário Completo----------------------------------------")
nome = ("Digite o nome:").strip()
cargo = input ("Digite o Cargo:").strip()
cpf = input("Digite seu CPF:").strip()
email = input("Digite sseu e-mail:").strip()
senha = input("Digite a senha:").strip()
turno = ("digite o turno").strip()
if len(nome) >3 and len (cargo) >3 and len(cpf) ==11 and len(senha) ==8 and len(turno) ==5:
    print("Cadastro de Funcionário completo")
else:
    print("Cadastro realiados")