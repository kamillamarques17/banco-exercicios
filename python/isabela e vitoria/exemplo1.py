print("-----------------Rastreamento de encomenda--------------")

# o for garante as 3 tentativas 
for tentativa in range (3):
    codigo = input ("digite o código da encomenda (7 caracteres): ").strip()

#validação com o tamanho com len()
    if len(codigo) == 7:
        print(f"sucesso código {codigo} aceito")
        break #sai do loop caso o código seja válido
    else:
    #informa que o tamanho está errado e mostra a quantidade q vc digitou
        print(f"erro: voce digitou {len(codigo)} carcateres, mas são necessários 7")
    print("-" * 30)
else:
# este else so executa se o usuario erras as 3 vezes 
    print("limite de tentativas atingidos, tente mais tarde")