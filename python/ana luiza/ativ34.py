print("--------------Embarque Internacional--------------")
for tentativa in range (3):
    passageiro = input ("Nome do cliente:").strip()
    destino =input ("Qual o seu destino:").strip()
    passaporte = input ("Qual o seu passaporte?:").strip()
    voo = input ("Qual o seu voo:").strip()
    portão = input (" Qual o seu portão de embarque:").strip()
    assento = input ("Qual a numeração do seu assento:").strip()
    
    if passageiro.isalpha() > 3 and destino.isalpha() and \
       len(passaporte).isdigit() == 8  and\
       len(voo)== 4 and \
       portão == "A1" and assento > 1:
        print ("Tudo certo, a validação de embarque ocorreu com sucesso!")

        break
    else:
        print("Tudo certo, a validação de embarque ocorreu com sucesso!")
else:
    print("Muitas tentativas. Procure o balcão presencial.")
print('-'*42) 