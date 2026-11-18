print("----------------Check-in de Aeroporto------------------")

for tentativa in range(3):
    voo = input("Digite o Voo: ").strip()
    assento = input("Digite o assento: ").strip()
    if len(voo) ==4 and len(assento) ==3:
        print("Acesso liberado!")
        break 
else: 
     print("Acesso incorreto.")
