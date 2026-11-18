# o semafaro inteligente 
cor = input("qual a cor do semafaro? (verde/amarelo/vermelho):")
if cor == "verde":
    print("ação: Acelere. o caminho está livre.")
elif cor =="amarelo":
    print("ação: atenção. reduza a velocidade e prepare-se para parar.")
elif cor == "vermelho":
    print("ação:pare imediatamente .")
else:
    print ("erro:cor invalida.")