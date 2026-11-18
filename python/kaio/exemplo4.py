print("--- ACESSO RESTRITO: ADMINISTRADOR ---")

for tentativa in range(3):

    # .lower() -> Garante que o usuário fique sempre em minúsculo (ex: adm -> adm)
    user = input("Digite seu Usuário: ").strip().lower()

    # .upper() -> Garante que o nível fique sempre em MAIÚSCULO (ex: admin -> ADMIN)
    nivel = input("Nível de Acesso (Dica: ADMIN): ").strip().upper()

    senha = input("Senha: ").strip()
    token = input("Token (6 números): ").strip()
    setor = input("Setor (apenas letras): ").strip()
    maquina = input("ID da Máquina (4 carac.): ").strip()

    # \ -> Ponte para organizar as 6 regras de validação
    # == -> Verifica se o nível é exatamente ADMIN
    # != -> Verifica se a senha NÃO é 12345

    if len(user) > 3 and nivel == "ADMIN" and \
       senha != "12345" and len(token) == 6 and \
       token.isdigit() and setor.isalpha() and len(maquina) == 4:

        print(f"Acesso liberado! Bem-vindo ao sistema, {user}.")
        break

    else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3.")
        print("Dica: Verifique o Token (6 números) e se o Nível é ADMIN.")
        print("-" * 30)

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")

