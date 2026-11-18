#o usuario informa que tipo de cliente ele é 
tipo_cliente= input ("digite seu perfil (1:estudande/ 2: idoso / 3:publico comum)")
if tipo_cliente=="1":
    print("você tem direito a 50% de desconto (meia estudande)")
elif tipo_cliente == "2":
    print("você tem direto a 50% de desconto (meia entrada idoso).")
else:
    print("você pagará o valor de entrada inteira.")
    #o elif é a alternativa especifica: não e estudante? 
    #mas é idoso?

    #se não caiu nas regras de desconto acima , cai no else 
    #automaticamente

    #dois sinais de igual (--) é uma pergunta, diferente do - que guarda um valor 
    ##O == compara os valores  