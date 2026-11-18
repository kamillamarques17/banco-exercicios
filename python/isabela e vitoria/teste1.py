#o usuario informa que tipo de cliente ele é:
tipo_cliente = input("digite seu perfil (1: estudante / 2: idoso /3:publico comum):")

if tipo_cliente == "1":
    print("voce tem direito a 50% de desconto (meia estudante).")
elif tipo_cliente == "2":

    print("voce tem direito a 50% de desconto (meia entrada idoso).")
else:
    print(" voce pagará o valor de entrada inteira")

    #o elif é a alternativa especifica: nao é estudante?
    #mas é idoso?

    #se nao caiu nas regras de desconto acima, cai no else
    #automaticamente 