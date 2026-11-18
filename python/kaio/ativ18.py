print("-------------------------SISTEMAS DE SEGURANÇA EM ETAPS----------------------------")
codigo_area = "100"
senha_correta = "kaio22"
for tentativa in range(3):
   
    chute = input("Digite o codigo de área: ")
    senha = input("Digite a senha: ")
    if chute == codigo_area and senha == senha_correta:
        print("senha correta! Entrando...")
        break
    else:
        print("Senha incorreta")
else:
 print("Muitas falhs, conta bloqueada!")