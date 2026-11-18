print("----------O SISTEMA DE SEGURANÇA EM DUAS ETAPAS----------" )
numero_placa = input("Digite o numero da sua placa: ")
for tentativa in range(5):
 if len(numero_placa) == 7 and numero_placa != "0000000":
      print("Acesso liberado!")
      break
 else:
      print("Placa inválida.")
      break
else:
 print("Acesso negado. Chame o segurança pelo interfone.")
print('-'*30)