print("----------------Cadastro de livros----------------")
for tentativa in range(3):
    titulo = input("titulo: ").strip()
    autor = input("autor: ").strip()
    genero = input("genero: ").strip()
    isbn = input("isbn (13 números): ").strip()
    paginas = input("Digite o numero de paginas: ").strip()
    cod_estante = input("cod_estante: ").strip()




    if titulo.isalpha() > 3  and autor.isalpha and genero == "DRAMA" and isbn.isdigit > 13 and paginas.isdigit and cod_estante != "000":
       
       print("Cadastro reallizado!")
       break
    else:
       print("Erro fatal.")
       print("-" * 30)


else:
   print("Tentativas bloqueadas")
