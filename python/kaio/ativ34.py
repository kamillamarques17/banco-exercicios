for tentativas in range(3):

    passageiro = input("Nome do passageiro (mais de 3 letras): ").strip()
    destino = input("Destino (apenas letras): ").strip()
    passaporte = input("Passaporte (8 caracteres): ").strip()
    voo = input("Voo (4 caracteres): ").strip()
    portao = input("Portão (deve ser A1): ").strip()
    assento = input("Assento (mais de 1 caractere): ").strip()
    seguranca = input("Código de segurança (3 dígitos): ").strip()

    if len(passageiro) > 3 and passageiro.isalpha() and \
       destino.isalpha() and \
       len(passaporte) == 8 and \
       len(voo) == 4 and \
       portao == "A1" and \
       len(assento) > 1 and \
       seguranca.isdigit() and len(seguranca) == 3:

        print("Embarque concluído!")
        break
    else:
        print("Erro: Verifique se está tudo correto")

    print("-" * 30)