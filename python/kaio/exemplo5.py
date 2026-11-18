print("---------SISTEMA DE AUDITORIA COMPLETO----------")

for tentiva in range(3):
    #coletando e tratamento os dados
    # removi o traço antes de checar o .isalnum() para a logica funcionar
    codigo = input("cod. relatorio (Ex: REL101): ").strip().upper()
    data = input("Data (DD/MM/AAAA): ").strip()
    email = input("E-mail do auditor").strip().lower()
    id_auditor = input("ID Numero de auditor: ").strip()
    status = input("status (DIGITE APRVODA): ").strip().upper()

    # Validação da lógica
    # [isalnum()] verifica se o código contém apenas letras e números
    # [count("/")] verifica se existem exatamente DUAS barras no texto
    # [count("@")] verifica se existe exatamente UM arroba no email
    # [endswith()] verifica se o e-mail termina corretamente
    # [isdigit()] garante que o ID do auditor seja apenas numérico

    if (
        codigo.isalnum() and
        data.count("/") == 2 and
        email.count("@") == 1 and
        email.endswith(".com") and
        id_auditor.isdigit() and
        status == "APROVADO"
    ):

        print(f"\n SUCESSO: Auditor {id_auditor}, seu relatório {codigo} foi enviado")
        break

    else:
        # Exibe o número de tentativa amigável
        print(f"\n ERRO: Dados inválidos! Tentativa {tentiva + 1} de 3.")
        print("-" * 40)

else:
    print("\n BLOQUEADO: Muitas falhas. Procure o Diretor de Segurança.") 