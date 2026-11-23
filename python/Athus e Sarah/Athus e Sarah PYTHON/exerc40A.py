print('-----Cadastro de Cofre Eletrônico-----')
for tentativa in range (3):
    usuario = input("Nome do usuário: ").strip().upper()
    senha_master = input("Sua senha: ").strip()
    palavra_seg = input("Qual a palavra de segurança? ").strip()
    cod_cofre = input("Qual o código do cofre? ").strip()
    cidade = input ("Digite a cidade de origem: ").strip()
    email_rec = input("Qual seu e-mail? ").strip().lower()
    if usuario > 3 and usuario.upper() and \
    senha_master == 6 and senha_master.isdigit() and \
    palavra_seg == "FALCÃO" and cod_cofre == 4 and \
    cidade.isalpha and email_rec > 10 and email_rec.lower():
        print("cadastrado com sucesso!")
        break
    else:
        print("ERRO.")
        print('-'*42)
else:
    print("SISTEMA BLOQUEADO.")