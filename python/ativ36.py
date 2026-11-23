print("--------------Cadastro de Produto Químico Controlado--------------")
for tentativa in range(3):
    substância = input("Substâncias citadas:").strip()
    tipo = input("Tipo:").strip()
    lote = input ("Lote: ").strip()
    responsável = input ("Responsável: ").strip()
    CRM = input("CRM: ").strip()
    validade = input("Validade: ").strip()

    if tipo == "SOLVENTE" and lote !="000":
        len(CRM) == 5 and validade == 8

        print("Cadastro feito!")
        break
    else:
        print("Erro no cadastro!")
    
else:
    print("Muitas tentativas falhas.")
print("-"*30)
