print("-------Cadastro de Funcionario completo------")
for tentativa in range(1):
    nome = input ("Qual seu nome?:")
    cargo = input ("Qual seu cargo?: ")
    cpf = input("Qual o seu CPF?: ")
    email = input("Qual seu email?: ")
    senha = input ("Qual sua senha?: ")
    turno = input ("Qual seu turno?:")
    if len(nome) > 3 and len(cargo) > 3 and len(cpf) ==11 and len(email) > 10 and len(senha) == 8 and len(turno) ==5:
        print(f'Olá, {nome} você é um(a) {cargo} e possui o cpf {cpf}, seu email é {email}, sua senha é{senha} e você trabalha no turno{turno}');
        break
    else:
        print("Você foi demitido!")
    print("-"*42) 