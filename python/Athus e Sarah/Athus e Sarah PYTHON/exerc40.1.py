print('-----Cadastro Cofre Eletrônico-----')
for tentativa in range(3):
    usuario = input("Nome do usuário?: ").strip().upper()
    senha_master = input("Qual senha (6 números)?: ").strip()
    palavra_seguranca = input("Qual a palavra de segurança?: ").strip().upper()
    
    # AJUSTE 1: Adicionei os () no final do .strip()
    cofre = input("Qual o cód cofre (4 dígitos)?: ").strip()
    cidade = input("Digite sua cidade: ").strip()
    email = input("Qual o email?: ").strip().lower()

    # AJUSTE 2: Removi o til de "FALCAO" para evitar erro de teclado
    # Usei a ponte \ para ficar didático
    if len(usuario) > 3 and \
       len(senha_master) == 6 and senha_master.isdigit() and \
       palavra_seguranca == "FALCAO" and \
       len(cofre) == 4 and \
       cidade.isalpha() and \
       len(email) > 10:
        print("Cadastro concluído!")
        break
    else:
        print(f"Erro nos dados! Tentativa {tentativa} de 3.")
        print("=" * 30)
else:
    print("Tentativas bloqueadas. Procure o suporte.")