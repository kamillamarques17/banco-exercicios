print("----------O SISTEMA DE SEGURANÇA EM DUAS ETAPAS----------" )
numero_voo = input("Olá! Digite o número do voo: ")
numero_assento = input("Digite o número do assento: ")
for tentativa in range(3):
    if len(numero_voo) == 4 and len(numero_assento) == 3:
         print("Voo liberado.")
         break
else:
     print("Voo negado.")
print('-'*30)