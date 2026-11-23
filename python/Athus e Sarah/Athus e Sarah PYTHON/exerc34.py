print('-----Validação de Embarque Internacional-----')
for tentativa in range(3):
    passageiro = input("Nome: ").strip()
    destino = input("Destino: ").strip()
    passaporte = input("Passaporte: ").strip()
    voo = input("N° voo: ").strip()
    portao = input("Nº portão: ").strip()
    assento = input("Nº assento: ").strip()

    if len(passageiro) > 3 and len(voo) == 4 and \
       len(assento) > 1 and destino.isalpha() and \
       len(passaporte) == 8 and passaporte.isdigit() and \
       portao == "A1":
        
         print("Pedido agendado com sucesso!")
         break
    else:
        print("Erro: Verifique os dados.")
else:
    print("Muitas tentativas. Procure o balcão presencial.")
print('-'*42)