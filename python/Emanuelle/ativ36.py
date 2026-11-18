print("----------------Cadastro de Produto Químico Controlado----------------")
for tentativa in range(3):
    substância = input("substância: ").strip()
    tipo = input("tipo: ").strip()
    lote = input("lote: ").strip()
    responsavel = input("resposavel: ").strip()
    CRM = input("CRM:").strip()
    Validade = input("Validade:").strip() 

    if tipo == "SOLVENTE"  and lote != "000":
        len(CRM) == 5 and Validade == 8 

        print("Cadastro feito.")
        break 
    else: 
        print("Erro no cadastro.")
        print("-" * 30)
else:
    print("Muitas tentativas falhas.")

