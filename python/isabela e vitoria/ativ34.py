print("------RESERVA DE VEÍCULO DE LUXO------")

for tentativa in range(2):
   cliente= input("Digite seu nome: ").strip()
   veículo = input("Digite o tipo de veículo: ").strip()
   cor = input("Digite a cor desejada: ").strip()
   CNH = input("Digite a sua cnh: ").strip()
   dias= input("Digite quantos dias vc ficará com ele: ").strip()
   seguro = input("Digite a forma de seguro: ").strip()

   if len(CNH) ==9  and \
      veículo == "SEDAN" and \
      cor.isalpha:
     
     print("Deu tudo certo.")
     break
   else:
        print("Erro: Verifique os dados digitados.")
       
