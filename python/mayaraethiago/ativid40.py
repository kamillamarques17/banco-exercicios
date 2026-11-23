print("----- CADASTRO DE COFRE ELETRÔNICO -----")
for tentativa in range(3):
 usuario = input("Usuário: ").strip().upper()
senha = input("Senha: ").strip()
palavra = input("Palavra de Segurança: ").strip().upper()
codigo = input("Código do Cofre: ").strip()
cidade = input("Cidade de Origem: ").strip()
email = input("E-mail de Recuperação: ").strip().lower()

if len(usuario) > 3 and \
 len(senha) == 6 and senha.isdigit() and \
 palavra == "FALCAO" and \
 len(codigo) == 4 and \
 cidade.isalpha() and \
  len(email) > 10:
    
    print("Cofre cadastrado com sucesso!")
    break
 else:
  print(f"Erro! Tentativa {tentativa + 1} de 3.")
  print("Verifique os dados e tente novamente.")
  print("-" * 30)
else:

print("Sistema bloqueado.")