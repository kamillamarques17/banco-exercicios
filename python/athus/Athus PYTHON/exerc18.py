print("----------O SISTEMA DE SEGURANÇA EM DUAS ETAPAS----------")
codigo_area = "022"
senha_pessoal = "euamonimes123"
for tentativa in range(3):
 tentativa_codigoarea = input("Digite o código de área: ").strip()
 tentativa_senhapessoal = input("Digite a sua senha: ").strip()
 if tentativa_codigoarea == codigo_area and tentativa_senhapessoal == senha_pessoal:
    print("Seu acesso foi liberado!")
    break
 else:
  print("Seu acesso foi negado.")
else:
  print("-"*50)