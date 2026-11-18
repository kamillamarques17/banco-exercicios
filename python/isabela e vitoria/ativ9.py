#criamos uma lista de nomes para o programa percorrer 
convidados= {"Vitória", "Isabela", "Geronimo"}

#O FOR funciona como um laço que pega um nome por vez da lista 
for pessoa in convidados:

    #O INPUT para o programa e espera o usuário digitar a idade 
    #O INPUT transforma o que foi digitado em um número interiro 
    idade = int(input("qual a idade de " + pessoa + "?"))

    #O IF faz a pergunta: a idade é maior ou igual a 18?
    if idade >= 18: 
    #se for vdd, o python executa essa linha:
      print(pessoa, "é maior de idade. Acesso liberado!")

    #O else é o caso contrario ( se a pergunta do IF for falsa )
else: 
    #se for menor de 18, o python executa esta linha:
    print(pessoa, "é menor de idade. Acesso negado!")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               