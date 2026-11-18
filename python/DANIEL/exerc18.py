print("------------seguraças em duas etapas---------")
codigo_area = "126"
senha_correta="daniel61"
for tentativas in range(3):
    
    chute=input("digite o codigo de area:")
    senha=input("digite sua senha:")
    if chute == codigo_area and senha== senha_correta:
        print ("senha correta! entrando...")
        break
    else:
        print("senha incorreta")
else:
    print ("muitas falhas. conta bloqueada! ")