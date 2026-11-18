parquinho = "Balanço"

for tentativa in range(6):
    peso = int(input("Digite o peso da criança:"))
 
    if peso <= 40:
        print("Pode balançar!")
else:
    print("Peso acima do limite!")