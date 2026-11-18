cores = input("Qual cor está o semáforo?(1:verde/2:amarelo/3:vermelho)")
if cores == "1":
    print("Pode passar")
elif cores == "2":
    print("Preste atenção, o sinal irá fechar!") 
elif cores == "3":
    print("Pare! O sinal está fechado.")  
else:
    print("Cor inválida.")         