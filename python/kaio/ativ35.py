for tentativas in range(3):

    cliente = input("Nome do cliente : ").strip()
    veiculo = input("Veiculo (Apenas sedan): ").strip()
    cor = input("Cor (Apenas letras): ").strip()
    cnh = input("CNH (9 caracteres): ").strip()
    dias = input("Dias de aluguel : ").strip()
    seguro = input("Seguro (mais de 1 caractere): ").strip()
    seguranca = input("Código de segurança (3 dígitos): ").strip()

    if len(cliente) > 3 and cliente.isalpha() and \
       veiculo.isalpha() and \
       cor.isalpha() and \
       len(cnh) == 9 and \
       dias.isdigit and \
       len(seguro) > 1 and \
       seguranca.isdigit() and len(seguranca) == 3:

        print("Embarque concluído!")
        break

    else:
        print("Erro: Verifique se está tudo correto")

    print("-" * 30)