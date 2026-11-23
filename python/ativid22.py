print("----------Voo agendado---------------")


for passagem in range(3):
    numerodo_voo = input("Digite o numero do seu voo:").strip()
    numerodo_assento = input("Digite seu assento: ").strip()

    if len(numerodo_voo) == -4  and len(numerodo_assento)==-3:
         print("Acesso liberado!")
         break
else:
     print("Acesso negado.")