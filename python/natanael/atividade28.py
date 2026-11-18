print("----------------------Reserva de Hotel Internacional---------------------------")
hóspedes = input("digite o Hópede:").strip()
país = input("digite o País:").strip()
pasaporte = input("digite o passaporte:").strip()
quarto = input("digite o quarto").strip()
data = input("Digite a data:").strip()
código = input("Digite o código da Reserva").strip()
if len(hóspedes) >3 and len(país) >3 and len(pasaporte) ==6 and len(quarto) ==3 and len(data) ==8 and len(código):
    print("reserva de Hotel Internacional")
else:
    print("reserva realizada!")