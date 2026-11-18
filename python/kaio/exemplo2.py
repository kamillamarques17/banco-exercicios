#criamos uma lista de nomes para o progama percorrer
convidados = ["Ana", "Bruno", "Carla"]

# O FOR funcionamento como um laço que pega um nome por vez de lista
for pessoa in convidados:

    # input para o progama e espera  usuario digitar a idade
    # o INT trasforma o que foi digitado em um numero inteiro
    idade = int(input("Qual a idade de" + pessoa +"?"))

    # O IF faz a pergunta: a idade e maior ou igual a 18?
    if idade >= 18:
        # se for  VERDADE, o Python executa esta linha:
        print(pessoa, "e maior de idade. Acesso liberado!")
        # O ELSE e o "caso contrario" (se a pergunta do IF for falsa )
    else:
        # se for MENOR de 18, o python executa esta linha:
        print(pessoa, "e menor de idade. Acesso negado!")