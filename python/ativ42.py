print("-------------segurança de banco central-------------")
for tentativa in range(3):
    gerente = input("gerente? ").strip()
    cidade = input("Qual a cidade?: ").strip()
    cpf = input("Qual o cpf?: ").strip()
    agencia = input("Qual a agencia: ").strip()
    conta = input("Digite a conta: ").strip()
    nível = input("qual o nivel: ").strip()
    senha = input("qual a senha?: ").strip()
    chave = input("qual a chave?: ").strip()

    if gerente.isalpha()and cidade.isalpha and cpf.isdigit() and\
    agencia.isdigit() and conta.isdigit()  and nível.upper() == "diretor" and senha !="123" and chave == "alpha":
        
        print("cadastro concluido!")
        break
    else:
        print("erro fatal.")
        print ("-" * 30 )
else:
    print("tentativas bloqueadas")

