print("-------------------------Cadastro de perfil de Usuário---------------------")
for tentativa in range(3):
    nome = input("Digite o nome:"). strip()
    cidade = input("Digite a cidade"). strip ()
    sigla = input ("Digite a sigla do estado").strip()
    if len(nome) >3 and len(cidade) >4 and len(sigla) ==2:
       print("Está correto!")
    break
else:
    print("prenchimento inorreto")