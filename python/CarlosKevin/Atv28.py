print("-------Reserva de hotel internacional-------")
hospede = input ('Qual o nome do hospede? ')
país = input ('qual o pais deseja se hospedar? ')
passaporte = input ('numero do passaporte? ')
quarto = input ('numero do quarto ')
data = input ('data ')
reserve = input ('qual o numero da reserva?')
if len('hospede') > 3 and len('país') > 3 and len('passaporte') == 6 and len('quarto') ==  3 and len('data') ==  8  and len('reserva') ==4:
    print(f'Olá, {hospede} vocÊ tem uma reserva no(a) {país} e possui o{passaporte}, seu quarto é o numero {quarto} data de reserva:{quarto}')

else:
    print('não foi possivel identificar sua reserva. ')
print('-'*42) 