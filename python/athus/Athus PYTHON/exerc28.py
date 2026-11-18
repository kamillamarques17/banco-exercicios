print('-----Reserva de Hotel Internacional-----')
nome = input("Qual seu nome? ").strip()
pais = input("Qual país deseja visitar? ").strip()
codigo_pass = input("Qual seu código de passaporte? ").strip()
quarto = input("Qual quarto deseja reservar? ").strip()
data = input("Quando pretende usar o quarto? ").strip()
codigo_reserva = input("Qual o código de reserva? ").strip()
if len(nome) > 3 and len(pais) > 3 and len(codigo_pass) == 6 and len(quarto) == 3 and len(data) == 8 and codigo_reserva == 4 and codigo_reserva != "0000":
        print(f"Pronto! Sua reserva foi feita.")
else:
    print("Falha nos dados. Tente novamente.")
print('-'*42)