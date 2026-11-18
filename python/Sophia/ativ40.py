print("------CADASTRO DE COFRE ELETRÔNICO------")
for tentativa in range(3):
    usuário = input("Digite seu Usuário: ").strip()
    senha = input("Senha de acesso: (6 números): ").strip()
    palavra= input("Palavra de segurança: ").strip()
    código = input("Código do cofre (4 números): ").strip()
    cidade = input("Cidade de origem (apenas letras): ").strip()
    email = input("email de recuperação: ").strip()

    if usuário.upper() > 3 and senha.isdigit() == 6 and \
       palavra == "FALCAO" and código == 4 and \
       cidade.isalpha() and email.lower() > 10:
       
       print("Cadastro concluido.")
       break 
    else: 
        print(f"Erro nos dados!")
        
        print("-" * 30)
else: 
    print("SISTEMA BLOQUEADO. Acesse o email de recuperação.")

