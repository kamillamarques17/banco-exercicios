print("-------------Cadastro de Novo Livro na Biblioteca-------------")
Titulo = input("Digite o título do livro:").strip()
Autor = input("Digite o nome do autor:").strip()
Gênero = input("Digite o gênero do livro:").strip()
isbn = input("Digite o ISBN do livro:").strip()
pagina = input("Digite o número de páginas do livro:").strip()
codigo-estante = input("Digite o código da estante onde o livro será armazenado:").strip()
if len(Titulo) >3 and len(Autor) >1 and Autor.isalpha() and\
    len 