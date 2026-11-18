print("-----------------sistema de RH---------------")
nome = input("digite seu cargo (deve conter 3 letras): ").strip()
cpf = input("digite o cpf (deve conter 11 caracteres ):").strip()
email = input("digite seu E-email (deve conter mais de 10 caracteres):").strip()
senha = input("digite sua senha. (deve conter mais de 8 letras):").strip()
turno = input("digite seu turno. (deve conter mais de 5 letras):").strip()
if len(nome) >= 3 and len(cpf) == 11 and len(email) > 10 and len(senha) == 8 and len(turno) == 5 :
    print (f"seu nome e {nome}: seu CPF e {cpf}: seu E-email e {email}: sua senha e {senha}: seu turno e {turno}:")
else:
    print("seu nome, CPF, E-email esta incorreto(a)!. tente novamente mais tarde")