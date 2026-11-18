print("-------------Cadastro de Produto Químico Controlado-------------")
nome = input("digite o nome do produto:").strip()
lote = input("digite o lote do produto:").strip()
if len(nome) == "SOLVENTE" and\
    len(lote) != "000":
    print("Produto cadastrado com sucesso.")
else:
    print("Erro: Verificar os dados.")