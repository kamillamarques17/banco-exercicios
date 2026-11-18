print('-----Reserva de Veículo de Luxo-----')
cliente = input("Nome: ").strip()
veiculo = input("Qual veículo deseja reservar? ").strip()
cor = input("Qual cor deseja? ").strip()
cnh = input("N° CNH: ").strip()
tempo = input("Por quanto tempo deseja reservar? ").strip()
seguro = input("Deseja assinar seguro? ").strip()

if len(cnh) == 9 and cor.isdigit() and \
   veiculo == "SEDAN":
   print("Reservado com sucesso!")

print('-'*42)