#Transformamos em uma lista para o python entender cada nome como uma unidade
user = ["admin", "suporte", "financeiro", "funcionario comum"]
for pessoas in user:
    
    senha = input(f"Qual é a senha de acesso?:")
    if senha == "admin1":
        print(f"Acesso liberado, {pessoas}")
    else:
        print(f"senha incorreta. Acesso Negado, {pessoas}")

    # O for é uma palavra reservada que senaliza o inicio de um ciclo, ele diz ao computador
    #"Prepare-se, pois vamos repetir as instruções que vem logo abaixo para um grupo de coisas"
    # Usuario (a variavel temporária): Este nome você inventa, pense nela como uma caixa vazia que o 
    # python vai usar para carregar um nome de cada vez.
    # in funcionarios (A origem): aqui voce indica onde o python deve buscar os dados, funcionarios
    #é o nome da sua lista original que contém os três cargos
    # O Python não entende o significado das palavras (ele não sabe o que é um "usuario" ou um "gerente")
    # Ele apenas segue a regra:
    #"Pegue o proximo item da lista e coloque dentro deste nome que eu inventei".
    # funcionarios (o nome da lista): é o nome que você deu para esse grupo, é como o rotulo da pasta.