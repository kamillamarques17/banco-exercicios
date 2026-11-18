print('-----Matrícula de Veículo Pesado-----')
nome = input ("Qual seu nome? ")
modelo = input ("Qual o modelo? ")
placa = input ("Qual o número da placa? ")
chassi = input("Qual o chassi? ")
cor = input("Qual a cor do carro? ")
ano = input("Qual o ano de lançamento? ")
if len(nome) > 2 and len(modelo) > 2 and len(cor) > 2 and len(placa) == 7 and len(chassi) == 10 and len(ano) == 4 and ano != "2000":
        print(f"Pronto! Seus dados foram registrados.")
else:
    print("Falha nos dados. Tente novamente.")
print('-'*42)