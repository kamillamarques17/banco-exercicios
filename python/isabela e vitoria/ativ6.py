tipo_cliente = input("digite a cor q apareceu (1: verde / 2: amarelo /3: vermelho / 4: outra ):")

if tipo_cliente == "1":
    print("pode passar .")
elif tipo_cliente == "2":

    print("reduza a velocidade.")
elif tipo_cliente =="3": 
    print("pare")

else:
    print("essa cor é inválida. ")


    #o elif é a alternativa especifica: nao é estudante?
    #mas é idoso?

    #se nao caiu nas regras de desconto acima, cai no else
    #automaticamente 