print("--- CONTROLE DE PRODUÇÃO FARMACÊUTICA ---")
for tentativa in range(5):
    farmaceutico = input("Nome do Farmacêutico Responsável: ").strip().title()
    ativo = input("Nome do Princípio Ativo: ").strip().title()
    forma = input("Forma Farmacêutica: ").strip().title()
    cidade = input("Cidade da Fábrica: ").strip().title()
    lote = input("Número do Lote (Ex: LOTE-12): ").strip()
    anvisa = input("Registro ANVISA: ").strip()
    quantidade = input("Quantidade de Comprimidos: ").strip()
    dosagem = input("Dosagem em Mg: ").strip()
    data = input("Data da Fabricação (DD-MM-AAAA): ").strip()
    email = input("E-mail do Laboratório: ").strip().lower()
    hash_formula = input("Hash da Fórmula: ").strip()
    liberacao = input("Liberação do Lote (APROVADO): ").strip().upper()
    data_formatada = data.replace(".", "/").replace("-", "/")

    if farmaceutico.isalpha() and \
       ativo.isalpha() and \
       forma.isalpha() and \
       cidade.isalpha() and \
       lote.startswith("LOTE-") and \
       anvisa.isalnum() and \
       quantidade.isdigit() and \
       dosagem.isdigit() and \
       data_formatada.count("/") == 2 and \
       email.endswith(".pharma.ind.br") and \
       liberacao == "APROVADO":
        
        hash_oculto = "*" * len(hash_formula)
        print(f"\nSUCESSO: Lote {lote} aprovado pelo farmacêutico {farmaceutico}!")
        print(f"Data Padronizada: {data_formatada} | Hash Protegido: {hash_oculto}")
        break
    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nBLOQUEADO: 5 tentativas esgotadas.")