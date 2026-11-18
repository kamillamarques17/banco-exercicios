print("----------Cadastro de perfil--------------")
nome = input("Digite seu nome")
cidade = input("Digite o nome de sua cidade")
sigla = input("Digite a sigla")
for tentativa in range(3):
    if len(nome)>3 and len(cidade)>4 and len(sigla) ==2:
        print("Cadastrp concluido.")
        break
    else:
        print("Acesso negado. Tente novamente mais tarde.")
    print("-"*30)