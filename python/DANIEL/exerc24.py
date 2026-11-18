for tentativas in range(3):
    nome = input("digite seu nome (deve coter mais de 3 letras)").strip()
    cidade = input("digite a cidade (deve conter mais de 4 letras)").strip()
    sigla = input("digite sua sigla").strip()


    if len(nome) >3 and len(cidade) >=4 and len(sigla) == 2:
        print(f"seu nome {nome} sua cidade {cidade} sua sigla {sigla}")
        break
    else:
        print("seu nome esta incorreto. tente novamente!")

else: 
 print("sua cidade esta incorreta. tente novamente")