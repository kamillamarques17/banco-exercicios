print("-----------------Cadastro de perfil-----------------")
nome =  input("Digite o seu nome: ")
cidade = input("Digite o nome de sua cidade:")
sigla = input("Digite a sigla: ")
for tentativa in range(3):
   if len(nome) > 3 and len(cidade) > 4 and len(sigla) == 2:
    print("Cadastro concluido.")
    break
else:
    print("Acesso negado! Tente em outro momento.")    
print('-'*50)