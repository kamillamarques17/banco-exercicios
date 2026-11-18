#o usuario informa que tipo de cliente ele é:
tipo_cliente = input("digite o que vc deseja ver (1: fotos / 2: videos /3: noticias / 4: outros ):")

if tipo_cliente == "1":
    print("voce deve usar o instagram .")
elif tipo_cliente == "2":

    print("voce deve usar o ttk.")
elif tipo_cliente =="3": 
    print(" voce deve usar twitter")

else:
    print("essa opção nao esta no banco de dados. ")


    #o elif é a alternativa especifica: nao é estudante?
    #mas é idoso?

    #se nao caiu nas regras de desconto acima, cai no else
    #automaticamente 