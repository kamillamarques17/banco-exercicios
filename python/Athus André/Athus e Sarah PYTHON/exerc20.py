print("----------O SISTEMA DE SEGURANÇA EM DUAS ETAPAS----------" )
usuario = input("Digite o nome do seu usuário (mínimo 5 caracteres): ").strip()
for tentativa in range(3):
        if len(usuario) >= 5:
            print("Usuário aceito!")
            break
        else:
          print("Usuário muito curto.")
else:
 print("Acesso bloqueado.")
print('-'*30)