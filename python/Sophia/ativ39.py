print("-----------Cadastro de Entrega por Aplicativo----------------")
for tentativa in range(3):
    entregador = input("Entregador: ").strip()
    veículo = input("Veículo: ").strip()
    código = input("Código o Pedido (6 números): ").strip()
    distância = input("Km: ").strip()
    cidade = input("Cidade: ").strip()
    observação = input("Observação: ").strip()

    if entregador.isalpha() and  veículo.isalpha() > 3  and \
       len(código) == 6 and distância.isdigit() and \
       cidade.isalpha =="BRASILIA" and observação != "NENHUMA":
    
       print("Registro de entrega feito.")
       break 
    else: 
       print("Erro no registro.")
       print("-" * 30)
else:
  print("tentativas feitas ")