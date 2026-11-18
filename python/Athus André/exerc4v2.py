print("Bem-vindo(a) ao Consultor de Clima!")
temperatura = float(input("Digite a temperatura: "))
if temperatura >= 30:
    print("Use roupas leves.")
elif 20 <= temperatura <= 30:
    print("Clima agradável, use camiseta.")
elif 10 <= temperatura <= 20:
    print("Leve um casaco leve.")
else:
    print("Está muito frio, use roupas pesadas!")