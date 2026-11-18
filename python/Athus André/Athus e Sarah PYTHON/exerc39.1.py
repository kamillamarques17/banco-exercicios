print('-----Cadastro de Entrega por Aplicativo-----')
for tentative in range (3):
 entregador= input("Nome do entregador: ").strip()
 veiculo = input("Qual o seu veiculo? ").strip()
 codigo = input("Código: ").strip()
 distancia = input("KMs: ").strip()
 cidade = input("cidade da entrega: ").strip()
 observacao = input("Observação: ").strip()
 if entregador > 3 and veiculo > 3 and \
 codigo == 6 and distancia.isdigit() and \
 cidade == "BRASÍLIA" and observacao != "NENHUMA":
  print("Cadastrado com sucesso!")
  break
else:
    print("ERRO.")
print('-'*42)