for tentativa in range(3):
    nome = input ("Nome: ").strip()
    sobrenome = input ("Sobrenome: ").strip()
    cpf = input ("CPF(11 numeros):").strip()
    agencia = input ("Agência (4 numeros):").strip()
    senha = input ("Senha (6 digitos):").strip()
    pix = input ("Chave Pix: ").strip()

    #\ -> Ponte para quebrar a linha
    #.isdigit() -> garante que idade e carteirinha sejam numeros
    # == -> Exige que o plano seja extamente OURO
    # != -> Proíbe que o código do médico seja 000
    # .isalpha() -> O setor não pode ter números

    if len(nome) > 2 and len(sobrenome) > 2 and \
    len(cpf) == 11 and cpf.isdigit() and \
    len(agencia) == 4 and agencia.isdigit() and \
    len(senha) == 6 and pix != "TESTE":
        print("Conta aberta com sucesso! Bem-vindo ao banco.")
        break
    else:
        print("Erro: Verifique seu cpf e Agência são apenas números e se os tamanhos estão corretos.")
        print("-"*30)
else:
    print("Há muitas tentativas falhas. Procure uma agência física.")