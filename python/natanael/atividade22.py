print("------------Voo agendado------------")
for passagem in range(3):
    numero_voo = input("Digite o número do seu voo:").strip()
    numero_acento = input("Digite o seu acento:")
    
    if len(numero_voo) == -4 and len(numero_acento)==3:
        print("Acesso liberado!")
        break
else:
    print("Acesso negado.")