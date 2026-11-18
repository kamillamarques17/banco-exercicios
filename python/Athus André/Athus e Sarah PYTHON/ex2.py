# Criamos uma lista de nomes para o programa percorrer
convidados = ["Ana", "Bruno", "Carla"]

# O FOR funciona como um laço que pega um nomo por vez de lista
for pessoa in convidados:

    # O INPUT para o programa e espera o usuario digitar a idade
    # O INPUT trransforma o que foi digitado em um numero inteiro 
    idade = int(input("Qual a idade de " + pessoa + "? "))

    # O IF faz a pergunta : a idade é maior ou igual a 18?
    if idade >= 18:
        # Se for VERDADE, o payton executa esta linha:
        print(pessoa, "é maior idade. Acesso liberado! ")

        # O ELSE  é o "caso contrario" (se a pergunta do if for falsa)
    else:
        # Se for MENOR de 18, o pyton executa esta linha:
        print(pessoa, "é menor de idade. Acesso negado! ")