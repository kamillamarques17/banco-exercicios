usuários = ["Admin", "Suporte", "Financeiro", "Cliente", "Funcionário Comum"] 

for pessoa in usuários:

    senha = (input(f"Olá, {pessoa}, digite sua senha: "))

    if senha == "euamonimes123":
        print(f"Acesso liberado, {pessoa}.")

    else:
        print(f"Acesso negado, {pessoa}.")