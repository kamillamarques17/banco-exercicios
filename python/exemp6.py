#criamos uma lista de nomes para o programa percorrer
convidados = ["Ana", "Bruno", "Carla"]

# o FOR funciona como um laço que pega um nome por vez da lista
for pessoa in convidados:
     #O INPUT para o programa e esper o usuario digitar a idade
     # O INT transforma  o que foi digitado em um número inteiro
     idade = int(input("Qual a idade de " + pessoa + "? "))

     #O IF faz a pergunta: a idade  é maior ou igual a 18?
     if idade >= 18:
          #Se for VERDADE, O Python executa esta linha:
          print(pessoa, "é maior de idade. Acesso liberado!")

     # O ELSE é o "caso contrário" (se a pergunta do IF for falsa)
     else:
          #Se for MENOR de 18, o python executa esta linha:
        print(pessoa, "é menor de idade. Acesso negado!")