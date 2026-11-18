print("----------------Segurança de Banco Central----------------")
for tentativa in range(3):
    gerente = input("Gerente? ").strip()
    cidade = input("Qual sua cidade? ").strip()
    cpf = input("Qual seu CPF? ").strip()
    agência = input("Qual a agência? ").strip()
    conta = input("Digite a conta: ").strip()
    nível = input("Qual o nível? ").strip()
    senha = input("Qual a senha? ").strip()
    chave = input("Qual chave? ").strip()
    if gerente.isalpha() and cidade.isalpha() and cpf.isdigit() and \
    agência.isdigit() and conta.isdigit() and nível.upper() == "DIRETOR" and senha != "123" and chave == "ALPHA":
       print("Cadastro concluido!")
       break
    else:
       print("Erro fatal.")
print("-" * 30)