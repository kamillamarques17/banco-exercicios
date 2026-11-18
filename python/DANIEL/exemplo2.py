#criamos uma lista de nomes para o programa percorrer 
convidados= ["ana","bruno","carla"]
#o FOR funciona como um laço que pega um nomw or vez da linha 
for pessoa in convidados:

        #o input para programar e esperar o usuario digitar a idade
        #o int transforma o que foi digitado em um numero inteiro 
    idade= int(input("qual a idade de "+ pessoa + "?"))
        #o IF faz a pergunta:a idade e maior ou igual a 18?
    if idade >= 18:
        #se for verdade, o python executa esta linha:
     print(pessoa, "e maior de idade. Acesso liberado!")

        #o ELSE é o "caso contrario" (se a pergunta do if for falsa)
else:
        #se for menor de 18, python executa esta linha 
    print(pessoa, "é menor de idade, acesso negado!")