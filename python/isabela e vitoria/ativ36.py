print("------CADASTRO DO NOVO LIVRO DA BIBLIOTECA ------")

for tentativa in range(3):
   titulo = input("Digite o titulo: ").strip()
   autor = input("Digite o autor: ").strip()
   genero = input("Digite o genero: ").strip()
   ISBN = input("Digite o ISBN: ").strip()
   páginas= input("Digite quantas páginas tem: ").strip()
   codigo_da_estante = input("Digite o codigo da estante: ").strip()

   if len(titulo) >3 and len(ISBN) ==13 and ISBN.isdigit and \
       páginas.isdigit and \
       codigo_da_estante != "000":
       autor.isalpha and \
       genero == "DRAMA" 

       print("Deu tudo certo.")
       break
   else:
        print("Erro: Verifique os dados digitados.")
       
else:
    print("Muitas tentativas falhas.")