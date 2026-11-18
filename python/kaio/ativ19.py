print("-------------------------SISTEMAS DE SEGURANÇA EM ETAPS----------------------------")
codigo_login = "login, Admin, root, suporte"

for tentativa in range(3):
     codigo = input("Digite o login: ")
     if codigo == codigo_login:
          print("login incorreta!")
          break
     else:
          print("Login correto! Entrando...")
else:
 print("Muitas falhs, conta bloqueada")