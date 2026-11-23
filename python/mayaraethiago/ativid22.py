voo = input("Digite o código do Voo 4 caracteres: ")
assento = input("Digite o código do Assento (3 caracteres): ")
if len(voo) == 4 and len(assento) == 3:
    print("Acesso liberado. Tenha um bom voo!")
else:
    print("Erro: Verifique a quantidade de caracteres e tente novamente.")
    