print("-------------------------ENTRADA DE ESTACIONAMENTO--------------------------")
for tentativas in range(5) :
 placa=input("digite a sua placa(7 carcteres): "). strip()
 if len(placa) == 7 and placa != "000000":
      print("placa invalida")
      break
 else:
    print("acesso negado, chame o segurança")