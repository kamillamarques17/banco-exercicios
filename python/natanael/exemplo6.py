# criamos uma lista de nomes para o programa percorrer
convidados = ["Ana", "Bruno", "Carla"]

#O FOR funciona como um laço que pega um nome por vez da lista
for pessoa in convidados:
    # O INPUT para o programa e espera o usuário diigitar a idade
    # O INT transforma o que foi digitado em um número inteiro
    idade = int(input("Qual a idade de "+ pessoa + "?"))
    
    #O IF faz a pergunbta: a idade é maior ou igual a 18?
    if idade >= 18:
    # Se for VERDADE, o Python executa esta linha:
       print(pessoa, "é maior de idade. Acesso liberado!")
    # O ELSE é o "caso contrário" (Se a pergunta do IF for falsa)
    else:
        print(pessoa,"é menor de idade. Acesso negado!")