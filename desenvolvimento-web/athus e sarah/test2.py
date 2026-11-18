tipo_cliente = input("Digite seu perfil (1: Estudante / 2: Idoso / 3: Público comum): ")
if tipo_cliente == "1":
    print("Você tem direito a 50% de desconto (Meia Estudante).")
elif tipo_cliente == "2":
    print("Você tem direito a 50% de desconto (Meia Entrada Idoso).")
else:
    print("Você pagará o valor de entrada inteira.")