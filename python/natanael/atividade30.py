print("--------------------Matrícula de Veículo Pesado-------------------------")
proprietário = input("Digite o nome do propietário:").strip()
modelo = input("digite o modelo:").strip()
placa = input("digite a placa").strip()
chassi = input("digite o chassi:").strip()
cor = input("Digite a cor").strip()
ano = input("Digite o ano").strip()
if len(proprietário) >2 and len(modelo) >2 and len(placa) ==7 and len (chassi) ==10 and len(ano) ==4:
    print("Matrícula de Veículo Pesado")
else:
    print("matrícula feita!")