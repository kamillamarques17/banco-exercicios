temperatura = float(input("qual a temperatura de hoje "))

if temperatura > 30:
    print("use roupas leves")
elif temperatura >= 20:
    print("clima agradavel, use camiseta")
elif temperatura >= 10:
    print("leve um casaco leve")

else:
 print("esta mt frio, use roupas pesadas")