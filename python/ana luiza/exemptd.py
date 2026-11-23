print("------RASTREAMENTO DE ENCOMENDA-------")

#O for garante as 3 tentivas
for tentativa in range(3):
    codigo = input("Digite o codigo da encomenda (7 caracteres): ").strip()

    #Validação do tamanho com len()
    if len(codigo) == 7:
        print(f"Sucesso! Código {codigo} aceito,")
        break #Sai do loop caso o codigo seja valido
    else:
    #Informa que o tamanho esta errado e mostra a quantidade que voce digitou
     print(f"Erro: você digitou {len(codigo)} caracteres, mas são necessários 7.")
    print("-" * 30)
else:
#Este else so executa se  usuario errar as 3 vezes
    print("Limite de tentaivas atingido. Tente mais tarde")
 