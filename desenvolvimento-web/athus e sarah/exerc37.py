print('-----Cadastro de Novo Livro na Biblioteca-----')
titulo = input("Título: ").strip()
autor = input("Autor: ").strip()
genero = input("Gênero: ").strip()
isbn = input("ISBN: ").strip()
paginas = input("Nº páginas: ").strip()
cod_estante = input("Código da estante: ").strip()
if isbn.isdigit() and len(isbn) == 13 and \
    autor.isalpha() and paginas.isalpha() and \
    genero == "DRAMA" and cod_estante != "000":
     print("cadastrado com sucesso!")
else:
    print("Erro: Verifique os dados.")
print('-'*42)