print("---sistema de auditoria completo---")

for tentativa in range(3):
    #coletando e tratando os dados
    #removi o traço antes de checar o .isalnum() para a logica funcionar
    codigo = input("cód. relatorio (ex: REL101): ").strip().upper()
    data =input ("data (DD/MM/AAAA):").strip()
    email = input("e-mail do auditor:").strip().lower()
    id_auditor = input ("ID númerico do Auditor: ").strip()
    status = input ("Status (Digite APROVADO): ").strip().upper()

    #EXPLICAÇÃO DA LÓGICA:
    #O .isalnum() verifica se o código contém apenas letras e numeros (sem simbolos ou espaço).
    #O .count("/") == 2 verifica se existem exatamente DUAS barras na data.
    #O .count("@") == 1 verifica se existe exatamente UM arroba no e-mail.
    #O .endswith(".com") garante que o e-mail termine corretamente.
    #O .isdigit() garante que o ID do auditor seja apenas numérico.

    if codigo.isalnum() and\
    data.count("/") == 2 and\
    email.count("@") == 1 and email.endswith(".com") and\
    id_auditor.isdigit() and\
    status == "APROVADO":
        print(f"\n SUCESSO: Auditor {id_auditor}, seu relatório {codigo} foi enviado!")
        break
    else:
        #Exibe o número da tentativa amigável (1,2 ou 3)
         print(f"\n ERRO: Dados inválidos! Tentativa {tentativa + 1} de 3.")
         print("-"*40)
else:
    print(f"\n BLOQUEADO: Muitas falhas. Procure o Diretor de Segurança.")

#-------------------------------------------------------
# LEGENDA TÉCNICA: O QUE CADA FUNÇÃO QUE FAZ NESTE CÓDIGO?
#-------------------------------------------------------

#1. .strip()      -> "O FAXINEIRO": Renove espaços em branco acidentais no incio ao fim.
#2. .upper()      -> "O GRITADOR": Transforma tudo em MAIÚCULO para padronizar o banco de dados.
#3. .lower()      -> "O COCHICHADOR": Trasnfroma tudo em minúsculo (ideal para e-mails).
#4. .isalnum()    -> "O MISTURADOR": Só aceita letras e númeors. Bloqueia símbolos (!, @, # $).
#5. .count()      -> "O CONTADOR": Conta simbolos especificos (como a barra "/") para validar fromatos.
#6. .endswith()   -> "O PORTEIRO": Verifica se o texto etrmina com o dominio certo (.com).
#7. .isdigit()    ->"O FILTRO": Garante que o campo tenha apenas números (0-9).
#8. \(ponte)      -> "A PONTE": Permite quebrar o 'if' em várias linhas para organizar o código.
#9. (t + 1)       -> "O TRADUTOR": Ajusta a contagem do python (1. 2 , 3).