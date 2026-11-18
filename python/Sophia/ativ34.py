print("-----------Validação de Embarque Internacional----------------")
for tentativa in range(3):
    passageiro = input("Nome do passageiro: ").strip()
    destino = input("Informe o destino: ").strip()
    passaporte = input("Digite o passaporte (8 números): ").strip()
    voo = input("Informe o voo (4 números): ").strip()
    portão = input("Digite o portão de embarque: ").strip()
    assento = input("Assento: ").strip()

    if passageiro.isalpha() == 8 and  destino.isalpha() and \
       len(passaporte) == 8 and passaporte.isdigit() and \
       len(voo) == 4 and portão =="A1":
       len(assento) > 1 


       print("Cartão de embarque emitido.")
       break 
    else: 
       print("Erro: Verifique os dados.")
       print("-" * 30)
else:
  print("Erro no totem. Dirija - se ao balcão presencial")
