print("--------------------Matrícula de Veículo Pesado---------------------")
Propietário = input("Digite o nome do propietário:").strip() 
Modelo = input("Digite o modelo:").strip() 
Placa = input("DIgite a placa:").strip()
Chassi = input("Digite o chassi:").strip()
Cor = input("Digite a cor:").strip()
Ano = input("Digite o ano:").strip()
if len(Propietário) >2 and len(Modelo) >2 and len(Placa) ==7 and len(Chassi) ==10 and len(Cor) >2 and len(Ano) ==4:
    print("Matrícula de Veículo Pesado")
else: 
    print("Matrícula feita!")