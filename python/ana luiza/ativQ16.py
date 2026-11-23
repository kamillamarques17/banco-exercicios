print("--- CONTROLE DE VOOS MILITAR ---")
for tentativa in range(5):
    oficial = input("Nome do Oficial Aviador: ").strip().title()
    posto = input("Posto Militar: ").strip().title()
    esquadrao = input("Esquadrão Aéreo: ").strip().title()
    cidade = input("Cidade da Base Aérea: ").strip().title()
    matricula = input("Matrícula do Caça: ").strip()
    missao = input("Código da Missão (Ex: MISSAO-01): ").strip()
    combustivel = input("Combustível Abastecido (L): ").strip()
    teto = input("Teto de Voo em Pés: ").strip()
    data = input("Data da Missão (DD-MM-AAAA): ").strip()
    email = input("E-mail da FAB: ").strip().lower()
    chave = input("Chave do IFF Transponder: ").strip()
    autorizacao = input("Autorização de Decolagem (AUTORIZADO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if oficial.isalpha() and \
       posto.isalpha() and \
       esquadrao.isalpha() and \
       cidade.isalpha() and \
       missao.startswith("MISSAO-") and \
       matricula.isalnum() and \
       combustivel.isdigit() and \
       teto.isdigit() and \
       data_formatada.count("/") == 2 and \
       email.endswith(".fab.mil.br") and \
       autorizacao == "AUTORIZADO":
        
        chave_oculta = "*" * len(chave)
        print(f"\nSUCESSO: Missão {missao} autorizada para o {posto} {oficial}!")
        print(f"Data Padronizada: {data_formatada} | Chave Protegida: {chave_oculta}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")
