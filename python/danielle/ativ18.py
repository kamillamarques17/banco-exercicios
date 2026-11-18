print("----------------O SISTEMA DE SEGURANÇA EM DUAS ETAPAS------------------")

código_area = "100"
senha_pessoal = "ABCD"

for tentativa in range(3):
    código = input("Digite o código de área:").strip()
    senha = input("Digite a senha pessoal:")

    if (código) == código == código_area and senha == senha_pessoal:
     print ("Acesso Liberado!")
     break 
    else: 
     print("Acesso Negado!")

else: 
  print("Acesso bloqueado!")
print("-"*30)


     