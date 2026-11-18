print("---ACESSO REGISTRO: ADMINISTRADOR---")
for tentativa in range(3):
    # .lower -> Garante que o usúario fique em minúsculo (ex: adm -> adm)
    user = input("Digite seu Usúario: ").strip().lower()

    # .upper() -> Garente que o nível fique sempre em MAIÚSCULO 9ex: adm -> ADMIN)
    senha = input("senha: ").strip()
    nível = input("Senha: ").strip()
    token = input("Token (6 números): ").strip()
    setor = input("Setor (apenas letras): ").strip()
    maquina = input("ID da Máquina (4carac.): ").strip()

    # \ -> Ponte para organizar as 6 regras de validação
    # == -> Verifica se o nível é exatamente ADMIN
    # != ->Verifuica se a senha NÃO é 12345
    if len(user) > 3 and len (token) == 6 and \
    senha != "12345" and len (token) == 6 and \
    token.isdigit() and setor.isalpha() and len(maquina) == 4:

     print(f"Acesso liberado! Bem-vindo ao sistema, {user}. ")
     break
    else:
       print(f"Erro nos dados! tentativa {tentativa + 1} de 3.") 
       print("Dica: Verifique o token (6 números) e se o nível é ADMIN.")
       print("-"*30)
else:
   print("Sistema bloqueado. alerta de intrusão enviado à segurança.")

