print("------SISTEMA DE AUDITORIA COMPLETO---------")
for tentativa in range(3):
    # Coletando e tratando os dados
    # Removi o traço antes de checar o .isalnum() para a lógica funcionar 
    codigo = input("Cód. Relátorio (Ex: REL101): ").strip().upper()
    data = input("Data (DD/MM/AAAA): ").strip()
    email = input("E-mail do Auditor: ").strip().lower()
    id_auditor = input("ID Numérico do Auditor: ").strip()
    status = input("Status (Digite APROVADO): ").strip().upper()

    # EXPLICAÇÃO DA LÓGICA:
    # O .isalnum() verifica se o código contém apenas letras e números (sem símbolos ou espaços).
    # O .count("/") == 2 verifica se existem exatamente DUAS barras na data. 
    # O .count("@") == 1 verifica se existe exatamente UM arroba no e-mail. 
    # O .endswith(".com") garante que o e-mail termine corretamnte. 
    # O .isdigit() garante que o ID do auditor seja apenas numérico.

    if codigo.isalnum() and \
       data.count("/") == 2 and \
       email.count("@") == 1 and email.endswith(".com") and \
       id_auditor.isdigit() and \
       status == "APROVADO":
        
        print(f"\n✅ SUCESSO: Auditor {id_auditor}, seu relatório {codigo} foi enviado!")
        break
    else:
        #Exibe o número da tentaiva amigável (1, 2 ou 3)
        print(f"\n❌ ERRO: Dados inválidos! Tenttiva {tentativa + 1} de 3.")
        print("-" * 40)
else:
    print("\n⚪ BLOQUEADO: Muitas falhas. Procure o diretor de segurança.")

    #----------------------------------------------------------------------
    # LEGENDA TÉCNICA: O QUE CADA FUNÇÃO FAZ NESTE CÓDIGO?
    # ---------------------------------------------------------------------
     
    # 1. .strip()  -> "O FAXINEIRO": Remove espaços em branco acidentais no início e fim.
    # 2. .upper()  ->  "O GRITADOR": Transforma tudo em MAISCULO para padronizar o banco de dados.
    # 3. .lower()  ->  "O CONCHICADOR": Transforma tudo em minusculo (ideal para e-mails).
    # 4. .isalnum() -> "O MISTURADOR": Só aceita letras e números. Bloqueia símbolos (!, @, #, $).
    # 5. .count()   -> "O CONTADOR": Conta símbolos específicos (como a barra "/") para validar formatos.
    # 6. .endswith() -> "O PORTEIRO": Verifica se o texto termina com o domínio certo (.com).
    # 7. .isdigit() -> "O FILTRO": Garante que o campo tenha apenas números (0-9).
    # 8. \ (Ponte) -> "A PONTE": Permite quebrar o "if" em várias linhas pra organizar o código.
    # 9. (t + 1)  -> "O TRADUTOR": Ajusta a contagem do Python (0, 1, 2) para o humana (1, 2, 3). 