for tentativas in range(3):
    codigo = input("Digite o codigo (Deve conter 6 caracteres): "). strip()
    destino = input("Digite o destino (deve conter 3 letras): "). strip()

    if len(codigo) == 6 and len(destino) > 3:
         print(f"Digite seu codigo e {codigo} Seu destino e {destino}")
         break
    else:
         print("Seu codigo esta incorreto. Tente novamente!")
else:
 print("Seu Destino esta incorreto. Tente novamente!")

