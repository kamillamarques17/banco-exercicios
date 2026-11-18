carro = input("digite oq deseja (1: verde / 2: amarelo / 3: vermelho):")
if carro == "1":
    print("Pode passar! (verde).")
elif carro == "2":
    print("Atenção, reduza a velocidade! (amarelo)")
elif carro == "3":
    print("Pare! (vermelho).")
else:
    print("Cor invalidade!")