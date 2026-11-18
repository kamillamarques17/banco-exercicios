print("--------------------Reserva de Hotel Internacional---------------------")
Hóspede = input("Digite o Hóspede:").strip() 
País = input("Digite o País:").strip() 
Passaporte = input("DIgite o Passaporte:").strip()
Quarto = input("Digite o Quarto:").strip()
Data = input("Digite a Data:").strip()
Código = input("Digite o Código de Reserva:").strip()
if len(Hóspede) >3 and len(País) >3 and len(Passaporte) ==6 and len(Quarto) ==3 and len(Data) ==8 and len(Código):
    print("Reserva de Hotel Internacional")
else: 
    print("Reserva realizada!")