print("-------------Sistema de Auditoria completo-------------")
for tentativa in range(3):
    #coletando e tratando os dados
    #removi o traço antes de checar o .isalnum() para a lógica funcionar
    codigo = input("Cod. Relatório(Ex: REL101): ").strip().upper()
    data = input("Data (DD/MM/AAAA): ").strip()
    email= input("Email do Auditor: ").strip()
    id_auditor= input("ID numérico do Auditor: ").strip()
    status = input("Status (Digite APROVADO)").strip().upper()
    
    #EXPLICAÇÃO DA LÓGICA:
    #isalnum() verifica se o código contém apenas letras e números (sem símbolos ou espaços)
    # O .count("/") == 2 verifica se existem exatamente DUAS barras na data.
    # O .count(@) == 1 verifica se existe examtamente UM @ no email.
    # O .endswith(".com") verifica se o email termina com .com
    # O .isdigit() verifica se o ID do auditor é composto apenas por números.
    if codigo.isalnum() and\
        data.count("/") ==2 and\
        email.count("@") ==1 and email.endswith(".com") and\
        id_auditor.isdigit() and\
        status == "APROVADO":
            print(f"Sucesso: Auditor {id_auditor}, seu relatório {codigo} foi enviado!")
            break
    else:
        #Exibe o número de tentativa amigável (1,2 ou 3)
        print(f"Erro: Dados inválidos. Tentativa {tentativa + 1} de 3.")
        print("-"*50)
else:
    print("Bloqueado:Muitas falhas. Procure o Diretor de Segurança.")
#====================================================
#Legenda técnica: O que cada função faz neste códgio?
#====================================================
#1.strip() -> "O FAXINEIRO": Remove espaços em branco acidentais no início e fim.
#2 .upper() -> "O GRITO": Converte tudo para maiúsculas, garantindo uniformidade.
#3 .lower() -> "O SUSSURRO": Converte tudo para minúsculas, útil para comparações.
#4 .isalnum() -> "O DETETIVE": Verifica se o código é
    