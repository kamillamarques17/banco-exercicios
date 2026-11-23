
print("----------- Validação de embarque Nacional -----------")
for tentativa in range(3):
    passageiro = input("Passageiro: ").strip()
    destino = input("Destino: ").strip()
    passaporte = input("Passaporte: ").strip()
    voo = input("Voo: ").strip()
    portão = input("Portão: ").strip()
    assento = input("Assento: ").strip()
    if (len(passageiro) > 3 and
    destino.isalpha() and
     len(passaporte) == 8 and passaporte.isdigit() and
    len(voo) == 4 and
    portão == "A1" and
    len(assento) > 1):
     print("Embarque liberado! ")
    else:
     print("Dados inválidos!")
else:
 print("Totem bloqueado! Procure o atendimento presencial.")
        