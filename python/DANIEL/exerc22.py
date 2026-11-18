print("------aeroporto------")
for tentativas in range(3):
    voo=input("digite seu o voo:").strip()
    assento=input("digite o seu assento: ").strip()

    if len(voo) == 4 and len(assento) == 3:
     print(f"seu voo esta correto {voo} e assento {assento} aceitos ")
    break

else:
    print ("acesso negado")
    print("-"* 30)