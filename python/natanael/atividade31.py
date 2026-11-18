for tentativa in range(3):
    nome = input("Nome:").strip()
    sobrenome = input("Sobrenome").strip()
    cpf = input("CPF 11 números").strip()
    agencia = input("Agência (4 números):").strip()
    senha = input("Senha (6 dígitos):").strip()
    pix = input("Chave pix: ").strip()
    
    # \ -> Ponte para quebrar a linha
    # .isdigit() -> garante que idade e carteirinha sejam número
    # == -> Exige que o plano seja exatamente OURO
    # != -> Proíbe que o código seja do médico seja 000
    # .isalpha() -> O setor não pode ter números
    if len(nome) >3 and len(sobrenome) >2 and \
       len(cpf) == 11 and cpf.isdigit() and\
       len(agencia) == 4 and agencia.isdigit() and\
       len(senha) == 6 and pix != "TESTE":
           print("Conta aberta com sucesso! Bem-vindo ao banco.")
           break
    else:
        print("Erro: Verificar se CPF e Agência são apenas númeross e sse os tamanhos etão corretos.")
        print('-' *30)
else:
    print("Muitas tentativas falhas. Procure uma agência física.")