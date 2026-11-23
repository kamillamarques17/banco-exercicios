print("--- LIQUIDAÇÃO DE CONTRATOS FUTUROS ---")
for tentativa in range(5):
    operador = input("Nome do Operador de Mesa: ").strip().title()
    corretora = input("Corretora Financeira: ").strip().title()
    commodity = input("Tipo de Commodity: ").strip().title()
    cidade = input("Cidade da Bolsa: ").strip().title()
    contrato = input("Código do Contrato Futuro (Ex: B3-01): ").strip()
    ordem = input("ID da Ordem de Compra: ").strip()
    lotes = input("Quantidade de Lotes: ").strip()
    margem = input("Margem de Garantia em Reais: ").strip()
    data = input("Data do Vencimento (DD-MM-AAAA): ").strip()
    email = input("E-mail da B3: ").strip().lower()
    chave = input("Chave Privada da Operação: ").strip()
    validacao = input("Validação do Negócio (EXECUTADO): ").strip().upper()
    data_formatada = data.replace("-", "/")
    if operador.isalpha() and \
       corretora.isalpha() and \
       commodity.isalpha() and \
       cidade.isalpha() and \
       contrato.startswith("B3-") and \
       ordem.isalnum() and \
       lotes.isdigit() and \
       margem.isdigit() and \
       data_formatada.count("/") == 2 and \
       len(data_formatada) == 10 and \
       email.endswith(".b3.com.br") and \
       validacao == "EXECUTADO":
        
        chave_oculta = "*" * len(chave)
        print(f"\nSUCESSO: Contrato {contrato} executado pelo operador {operador}!")
        print(f"Data Padronizada: {data_formatada} | Chave Protegida: {chave_oculta}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")
