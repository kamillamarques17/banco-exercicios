print('-----Matrícula de Veículo Pesado-----')
nome = input ("Qual seu nome? ").strip()
modelo = input ("Qual o modelo? ").strip()
placa = input ("Qual o número da placa? ").strip()
chassi = input("Qual o chassi? ").strip()
cor = input("Qual a cor do carro? ").strip()
ano = input("Qual o ano de lançamento? ").strip()
if len(nome) > 2 and len(modelo) > 2 and len(cor) > 2 and len(placa) == 7 and len(chassi) == 10 and len(ano) == 4 and ano != "2000":
        print(f"Pronto! Seus dados foram registrados.")
else:
    print("Falha nos dados. Tente novamente.")
print('-'*42)