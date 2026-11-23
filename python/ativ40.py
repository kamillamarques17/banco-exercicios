print("-------------Cadastro de cofre-------------")
for tentativa in range(3):
    usuário = input("Nome do usuario: ").strip().upper()
    senha_master = input("Qual a senha?: ").strip()
    palavras_seg = input("Qual a palavra de segurança?: ").strip()
    cod_cofre = input("Qual o codigo?: ").strip()
    cid_origem = input("Digite a sua cidade: ").strip()
    email_rec = input("Email de recuperação?: ").strip().lower()

    if usuário.isalpha() > 3 and senha_master.isdigit > 6 and palavras_seg == "FALCÃO" and cid_origem.isalpha() and cod_cofre == 4 and email_rec > 10:

        print(f"Acesso liberado! Bem-vindo ao sistema. {usuário}." )
        break
    else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3. ")
        print("-"* 30)
else:
    print("SISTEMA BLOQUEADO Alerta de intrusão enviado à segurança.") 


