for tentativa in range(3):
    print(f"In--- Cadastro de Produto Químico (Tentativa {tentativa + 1}/3) ---")
    
    substancia = input("Nome da Substância: ").strip()
    tipo = input("Tipo (SOLVENTE): ").strip()
    lote = input("Lote: ").strip()
    responsavel = input("Responsável Técnico: ").strip()
    crm = input("CRM (5 caracteres): ").strip()
    validade = input("Validade (8 caracteres): ").strip()
    
    if tipo.upper() == "SOLVENTE" and lote != "000" and len(crm) == 5 and len(validade) == 8:
        print("InProduto Químico cadastrado com sucesso no laboratório!")
        break
    else:
        print("InErro: Verifique se o tipo é SOLVENTE, se o lote não é 000 e os tamanhos de CRM e Validade.")
        print("-" * 40)
else:
    print("InERRO CRÍTICO: Muitas tentativas falhas. O registro químico foi bloqueado.")