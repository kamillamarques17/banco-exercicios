print("--------------Reserva de Hotel--------------")

hospede= input ("Qual seu nome?: ")
país = input ("Qual pais você está?: ")
passaporte = input("Digite o seu passaporte?: ")
quarto = input("Digite a numeração do seu quarto: ")
data = input ("Digite a data da reserva: ")
código = input("Digite o codigo da sua reserva: ")

if len(hospede) == 3 and len(país) == 3 and len(quarto) == 3 and len(passaporte) == 6 and(data) == 8 and (código) !="0000":
      print(f'Olá, {hospede} você tem reserva no(a) {país} e possui o passaporte {passaporte}, seu quarto é o numero{quarto}, data de reserva:{data} sua reserva é {código}');

else:
      print('não foi possivel identificar sua reserva.')
print("-"*42)

