print('-----Cadastro de Entrega de Aplicativo-----')
for tentative in range (3):
 entregador= input("Nome do entregador: ").strip()
 veiculo = input("Qual o seu veiculo? ").strip()
 codigo = input("Código: ").strip()
 distancia = input("KMs: ").strip()
 cidade = input("cidade da entrega: ").strip()
 observação = input("Observação: ").strip()
 if entregador.isalpha() and len(veiculo) > 3 and \
    len (codigo) == 6 and distancia.isdigit() and \
    len (cidade) == "Brasília" and len (observação) != "NENHUMA":
    print("Sua entrega foi concluida!")
    break
else:
    print("Falha ao encontrar o endereço.")
print('-'*42)