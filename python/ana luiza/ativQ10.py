print("--- DESPACHO DE PEDIDOS E-COMMERCE ---")
for tentativa in range(5):
    comprador = input("Nome do Comprador: ").strip().title()
    sobrenome = input("Sobrenome: ").strip().title()
    cidade = input("Cidade de Entrega: ").strip().title()
    estado = input("Estado Federativo: ").strip().upper()
    rastreamento = input("Código de Rastreamento: ").strip()
    sku = input("SKU do Produto: ").strip()
    quantidade = input("Quantidade Comprada: ").strip()
    valor = input("Valor Total em Reais: ").strip()
    data = input("Data da Postagem (DD-MM-AAAA): ").strip()
    email = input("E-mail do Cliente: ").strip().lower()
    cvv = input("Código de Validação do Cartão: ").strip()
    status = input("Status da Entrega (DESPACHADO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if comprador.isalpha() and \
       sobrenome.isalpha() and \
       cidade.isalpha() and \
       rastreamento.startswith("LOG-") and \
       sku.isalnum() and \
       quantidade.isdigit() and \
       valor.isdigit() and \
       data_formatada.count("/") == 2 and \
       email.endswith(".com.br") and \
       status == "DESPACHADO":
        
        cvv_oculto = "*" * len(cvv)
        print(f"\nSUCESSO: Pedido de {comprador} {sobrenome} despacho para {cidade}-{estado}!")
        print(f"Data Padronizada: {data_formatada} | CVV Protegido: {cvv_oculto}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")