print('-----Cadastro de Cofre Eletrônico-----')
for tentativa in range (3):
    usuario = input("Nome do usuário: ").strip().upper()
    senha_master = input("Sua senha: ").strip()
    palavra_segurança = input("Qual a palavra de segurança? ").strip()
    cofre = input("Qual o código do cofre? ").strip()
    cidade = input ("Digite sua cidade: ").strip()
    email = input("Qual seu e-mail? ").strip().lower()
    if len(usuario) > 3 \
    and len(senha_master) == 6 and senha_master.isdigit()  and \
   palavra_segurança == "FALCÃO" and \
    len(cofre) == 4 and \
    cidade.isalpha() and \
    len(email) > 10:
            print("Cadastro concluído!")
            break
    else:
          print("Erro fatal.")
          print("=" * 30)
else:
      print("Tentativas bloqueadas")