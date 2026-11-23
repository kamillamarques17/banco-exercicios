print("--------------Reserva de Hotel--------------")

proprietário= input ("Qual seu nome?: ")
modelo = input ("Qual o modelo do carro?: ")
placa = input("Digite a placa do carro?: ")
chassi = input("Digite a numeração do chassi: ")
cor = input ("Digite a cor do carro: ")
ano = input("Digite o ano do carro: ")

if len(proprietário) == 2 and len(modelo) == 2 and len(placa) == 7 and len(chassi) == 10 and(cor) == 2 and (ano) == 4 !="2000":
      print(f'Olá, {proprietário} o modelo de seu carro é: {modelo} e possui a placa {placa}, o chassi{chassi}, a cor do carro é:{cor} o ano do carrro é: {ano}');

else:
      print('não foi possivel confirmar as informações..')
print("-"*42)

