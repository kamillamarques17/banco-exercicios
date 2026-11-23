temp = float(input("Qual a temperatura atual?"))

if temp > 30:
    print("Use roupas leves.")
elif temp >= 20:
    #o #elif cria uma faixa intermediária: entre 20 e 30
    print("Clima agradável, use camiseta.")
elif temp >= 10:
    #Este #elif só será lido se a temperatura for menor que 20
    print("Leve um casaco leve.")
else:
    print("Está muito frio, use roupas pesadas.")