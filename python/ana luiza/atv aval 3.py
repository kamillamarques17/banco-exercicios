cores = input("Qual a cor está o semáforo?(1:verde/2:amarelo/3:vermelho)")
if cores == "1":
    print ("pode passar")
elif cores == "2":
    print ("Preste atenção, o sinal irá fechar!")
elif cores == "3":
    print ("Pare! O sinal está fechado.")
else:
    print ("cor inválida.")