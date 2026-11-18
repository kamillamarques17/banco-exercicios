for tentativas in range(3):
    codigo = input("digite o codigo (deve conter 6 caracteristicas):").strip()
    destino = input ("digite o destino (deve conter3 letras):").strip()

    if len(codigo) == 6 and len(destino) >3:
        print(f"digite seu codigo e {codigo}seu destino e { destino}")
        break 
    else:
        print("seu codigo esta incorreto. tente novamente!")
else:
   print("seu destino esta incorreto. tente novamente!")