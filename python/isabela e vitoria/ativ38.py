print("------CADASTRO DE ENTREGA POR APLICATIVO------")

for tentativa in range(3):
  entregador = input("Digite o seu nome: ").strip()
  veiculo = input("Digite o seu veiculo: ").strip()
  codigo_de_pedido = input("Digite o seu codigo de pedido: ").strip()
  distancia = input("Digitea sua distancia: ").strip()
  cidade  = input("Digite a sua cidade: ").strip()
  obeservação = input("Digite a sua obervação: ").strip()

  if len(veiculo) >3 and len(codigo_de_pedido) ==6 and \
       distancia.isdigit and \
       obeservação != "nenhuma" and \
       cidade == "brasilia" :

       print("Deu tudo certo.")
       break
  else:
        print("Erro: Verifique os dados digitados.")
       
else:
    print("Muitas tentativas falhas.")