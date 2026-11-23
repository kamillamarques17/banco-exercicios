print("--------------Cadastro de livros--------------")
for tentativa in range (3):
    titulo = input ("titulo: ").strip()
    autor = input(" autor: ").strip()
    genero = input ("genero: ").strip()
    isbn = input ("Isbn (13 números):").strip()
    paginas = input ("Digite o numero de paginas: ").strip()
    cod_estante = input ("cod_estante: ").strip()

    if titulo.isalpha() > 3 and autor.isalpha and genero == "DRAMA" and isbn.isdigit > 13 and paginas.isdigit and cod_estante !="000":
        print("Cadastro realizado")
        break
    else:
        ("Erro!")
else:
    print("Tentativas bloqueadas!")
print("-"*30)
