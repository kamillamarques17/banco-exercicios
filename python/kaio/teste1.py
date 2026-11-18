# o usuario informa que tipo de usuario ele e
tipo_cliente = input("digite seu perfil (1: Estudante / 2: Idoso / 3: Publico comun):")
if tipo_cliente == "1":
    print("Voce tem direito a 50% de desconto (Meia estudante).")
elif tipo_cliente == "2":
    print("Voce tem direito a 50% de desconto (Meia Entrada Idoso).")
else:
    print(" Voce pagara o valor de entrada inteiro.")

    #o elif e a alternativa especifica: não e estudante?
    #mais e idoso
    #se não caiu na s regras de desconto acima, cai o else
    #automaticamente
    #Dois sinais de igual (==) e uma pergunta. dferente do = que guarda um valor 
    # O comparar os valores 