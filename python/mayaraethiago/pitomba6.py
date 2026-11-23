print("-----Auditoria Financeira e Custódia de Criptoativos-----")

for tentativa in range(5):
    nome = input("Nome do Auditor: ").strip()
    cargo = input("Cargo na Empresa: ").strip()
    token = input("Símbolo do Token: ").strip()
    hashbloco = input("Código Hash do Bloco: ").strip()
    chave = input("Chave Pública: ").strip()
    gas = input("Taxa de Gas: ").strip()
    quantidade = input("Quantidade Transferida: ").strip()
    confirmacoes = input("Número de Confirmações: ").strip()
    pais = input("País da Exchange: ").strip()
    data = input("Data da Operação (DD/MM/AAAA): ").strip()
    email = input("E-mail de Compliance: ").strip().lower()
    parecer = input("Parecer da Auditoria: ").strip().upper()

    if nome.isalpha() and cargo.isalpha() and pais.isalpha() and \
       token.isalnum() and hashbloco.isalnum() and chave.isalnum() and \
       gas.isdigit() and quantidade.isdigit() and confirmacoes.isdigit() and \
       len(chave) >= 12 and len(data) == 10 and \
       email.endswith(".exchange.io") and \
       "@" in email and \
       parecer == "CONCLUIDO":

        print(f"\nSUCESSO: auditor {nome}, parecer {parecer} registrado.")
        break

    else:
        print(f"\nERRO: cadastro inválido, Tentativa {tentativa + 1} de 5")
        print("-" * 40)

else:
    print("\nBLOQUEADO: Limite de 5 tentativas excedido.")
