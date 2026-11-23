print("-----Cadastro de Desenvolvimento e Repositório Git-----")

for Tentativa in range(5):
    nome = input("Nome do Desenvolvedor: ").strip()
    git = input("Nickname: ").strip()
    repositorio = input("Nome do Repositório: ").strip()
    ID = input("ID do Commit: ").strip()
    linhas = input("Quantidade de linhas: ").strip()
    branch = input("Branch principal: ").strip()
    linguagem = input("Linguagem de programação: ").strip()
    chave = input("Chave SSH do usuário: ").strip()
    email = input("E-mail institucional: ").strip().lower()
    status = input("Status do Deploy: ").strip().upper()

    if git.isalnum() and repositorio.isalnum() and ID.isalnum() and \
       linhas.isdigit() and  nome.isalpha() and \
       branch.isalpha() and \
       linguagem.isalpha() and \
       email.endswith("edu.br") and len(chave) == 12 and \
       status == "SUCESSO":

        print(
            f"\nSUCESSO: desenvolvedor {nome}, "
            f"cadastro {status} registrado"
        )

        break

    else:

        print(f"\nERRO: cadastros inválidos, Tentativa {Tentativa + 1} de 5")

        print("-" * 40)

else:

    print("\nBLOQUEADO: Limite de 5 tentativas excedido.")

