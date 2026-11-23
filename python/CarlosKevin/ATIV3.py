print ("--- SISTEMA DE ACESSO DE SEGURO AO SEVIRDOR DE DADOS ---")

for tentativa in range(5):
    #colentando e tartando os dados na entrada 
    Nome= input("Nome do adm: ").strip()
    Cargo = input("Cargo do usuario : ").strip()
    Codigo= input("Codigo do Servidor: ").strip()
    ip = input("Ip do Terminal: ").strip() 
    Porta = input("Porta da rede: ").strip()
    Setor = input("Setor Responsavel: ").strip()
    Protocolo = input("Protocolo de Rede: ").strip()
    Senha = input("Senha Provisoria: ").strip()
    Dominio = input("Dominio Corporativo: ").strip()
    Confimarçao = input("Confimarçao de Segurança (Digite APROVADO) : ").strip().upper()

    #VALIDAÇAO DIRETA COM IF + QUEBRA DE LINHA (\)
    if Codigo.isalnum() and \
       Protocolo.isalnum() and \
       Porta.isdigit() and \
       ip.isdigit() and \
       Cargo.isalpha() and \
       Setor.isalpha() and \
       Dominio.endswith(".org") and \
       len(Senha) == 8 and\
       Confimarçao == "APROVADO":

        print(f"\nSUCESSO: SEU BOSTA {Codigo}, SETOR {Cargo} liberado!")
        break
    else:
        #Exibe a tentativa amigavel (1 a 5)
        print(f"nERRO: VOÇÊ ERROU SEU BOT! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEAO: Limite de 5 tentativas excedido. Procure o Diretor da Base.")