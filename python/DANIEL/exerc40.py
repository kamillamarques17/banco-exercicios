print("--- CADASTRO DE COFRE ELETRONICO ---")

for tentativa in range(3):

    usuario = input("Digite seu usuário: ").strip()
    senha_master = input("Digite sua senha: ").strip()
    palavras_de_seguranca = input("Digite sua palavra de segurança: ").strip()
    codigo_de_cofre = input("Digite o código do cofre: ").strip()
    cidade_de_origem = input("Digite sua cidade de origem: ").strip()
    email_de_recuperacao = input("Digite o email de recuperação: ").strip()

    if (
        len(usuario) > 3 and \
        senha_master.isdigit() and len(senha_master) >= 6 and \
        palavras_de_seguranca == "FALCAO" and \
        len(codigo_de_cofre) == 4 and codigo_de_cofre.isdigit() and \
        cidade_de_origem.isalpha() and \
        len(email_de_recuperacao) > 10
    ):

        print(f"Acesso liberado! Bem-vindo ao sistema, {usuario}.")
        break

    else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3.")

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")