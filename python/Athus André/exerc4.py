print("Bem-vindo(a) ao Consultor de Clima!")
tipo_usuario = input("Qual a temperatura atual? (1: Acima de 30°C / 2: Entre 20 e 30°C / 3: Entre 10 e 19°C / 4: Abaixo de 10°C): ")
if tipo_usuario == "1":
    print("Use roupas leves.")
elif tipo_usuario == "2":
    print("Clima agaradável, use camiseta.")
elif tipo_usuario == "3":
    print("Leve um casaco leve.")
else:
    print("Está muito frio, use roupas pesadas!")