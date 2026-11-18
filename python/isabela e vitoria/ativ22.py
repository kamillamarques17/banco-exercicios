print("-------------------------CHEIN IN--------------------------")
for tentativas in range(3) :
 voo=input("digite a sua placa(4 carcteres): "). strip()
 assento= input("digite o assento (2 carcteres): "). strip ()

 if len(voo) == 4 and len( assento) ==2:
     print(f"sucesso, voo {voo} e assento {assento} aceitos")
     break
 
else:
   print("acesso negado")
   print("-" * 30)
   