print("------------------------- CADASTRO DE FUNCIONÁRIO --------------------------")

nome = input("Digite o seu nome (mais de 3 caracteres): ").strip()
cargo = input("Digite o cargo (mais de 3 caracteres): ").strip()
senha = input("Digite a sua senha (8 caracteres): ").strip()

if len(senha) == 8 and senha != "12345678":

    cpf = input("Digite o seu CPF (11 caracteres): ").strip()
    email = input("Digite o seu email (mais de 10 caracteres): ").strip()
    turno = input("Digite o seu turno (5 caracteres): ").strip()

    if (
        len(nome) > 3 and
        len(cargo) > 3 and
        len(cpf) == 11 and
        len(email) > 10 and
        len(turno) == 5
    ):
        print(f"Sucesso! Nome: {nome}, Cargo: {cargo}, CPF: {cpf}, Email: {email}, Turno: {turno}")
    else:
        print("Acesso negado, verifique suas respostas")
