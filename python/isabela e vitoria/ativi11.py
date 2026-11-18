print("----- PLATAFORMA DE COMÉRCIO EXTERIOR -----")

for tentativa in range(5):
    nome_importador = input("Nome do Importador: ").strip()
    razao_social = input("Razão Social: ").strip()
    porto_origem = input("Porto de Origem: ").strip()
    porto_destino = input("Porto de Destino: ").strip()
    codigo_container = input("Código do Container: ").strip()
    num_declaracao = input("Número da Declaração: ").strip()
    qtd_itens = input("Quantidade de Itens: ").strip()
    peso_bruto = input("Peso Bruto: ").strip()
    codigo_tarifario = input("Código Tarifário: ").strip()
    data_despacho = input("Data do Despacho (DD/MM/AAAA): ").strip()
    email_alfandega = input("E-mail da Alfândega: ").strip().lower()
    parecer_fiscal = input("Parecer Fiscal (LIBERADO): ").strip().upper()

    if nome_importador.isalpha() and \
       razao_social.isalpha() and \
       porto_origem.isalpha() and \
       porto_destino.isalpha() and \
       codigo_container.isalnum() and \
       codigo_tarifario.isalnum() and \
       num_declaracao.isdigit() and \
       qtd_itens.isdigit() and \
       peso_bruto.isdigit() and \
       "@" in email_alfandega and \
       email_alfandega.endswith(".gov.br") and \
       data_despacho.count("/") == 2 and \
       parecer_fiscal == "LIBERADO":

        print("\nSUCESSO: Processo Aduaneiro Liberado!")
        break
    else:
        print(f"\nERRO: Dados inválidos! Tentativa {tentativa + 1} de 5")
        print("-" * 40)

else:
    print("\nBLOQUEADO: Limite de 5 tentativas excedido. Procure a fiscalização.")

