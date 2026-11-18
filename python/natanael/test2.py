# o usuário informa que o tipo de cliente é:
tipo_cliente = input("Digite seu perfil (1:estudante/ 2: idoso/ 3: publico comum):")

if tipo_cliente == "1":
    print("Você tem direito a 50% de desconto (Meia estudante).")
elif tipo_cliente == "2":
    
    print("Você tem direito a 50% de desconto (Meia Entrada idoso)")
else:
    print("Você pagará o valor de entrada inteira.")
    
    #O elif é a alternativa específica: não é estudante? Mas é idoso?
    #Se não caiu na regra de deconto acima, cai no else automaticamente.
    #dois sinais de igual (==) é uma pergunta. Diferente do = que guarda o valor
    # O == compara os valores