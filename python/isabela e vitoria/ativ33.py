print("------VALIDAÇÃO DE EMBARQUE INTERNACIONAL ------")

for tentativa in range(3):
   passageiro = input("Digite seu nome: ").strip()
   destino = input("Digite o seu destino: ").strip()
   passaporte = input("Digite o passaporte: ").strip()
   voo= input("Digite o seu voo: ").strip()
   portao= input("Digite o portao: ").strip()
   assento = input("Digite o seu assento: ").strip()

   if len(passageiro) > 3 and len(passaporte) ==8 and passaporte.isdigit() and \
       destino.isalpha()  and \
       len(voo) ==4  and  \
       portao == "A1" and  \
       len(assento) > 1 :
        
     print("Deu tudo certo.")
     break
   else:
        print("Erro: Verifique os dados digitados.")
       
else:
    print("Muitas tentativas falhas. Procure o balcão.")