print("--------------locação de carros executivos--------------")
for tentativa in range (3):
 
   cliente = input ("nome do seu cliente?: ").strip()
   veículo = input ("Qual o modelo do veiculo ?: ").strip()
   cor = input("qual a cor do veiculo?").strip()
   cnh = input("Digite a CNH  (9 caracteres) :").strip()
   dias = input ("quantos dias o carro irá ficar alugado? ").strip()
   seguro = input("qual o numero do seguro : ").strip()

   if cliente.isalpha() > 3 and veículo == "SEDAN" and \
   cor > 3 and cnh.isdigit() and \
len(dias) > 3 and seguro > 3  and\
     print("Reservado!"): 
     break
   else:
    print("Erro ao reservar")

else:
 print("Erro na reservar!")
print("-"*30)
      