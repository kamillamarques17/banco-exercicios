for tentativas in range(3):

    substancia = input("substancia (Deve ser solvente) : ").strip()
    tipo = input("Tipo : ").strip()
    lote = input("Lote (não pode ser '0000'): ").strip()
    responsavel = input("Nome do responsalvel (maior que 1): ").strip()
    crm = input("CRM (5 caracteres) : ").strip()
    validade = input("validade (mais de 8 caractere): ").strip()

    if len(substancia) > 1 and substancia.isalpha() and \
       tipo.isalpha() and \
       len(lote) and lote.isdigit != "0000" and \
       responsavel.isalpha() > 1 and \
       crm.isdigit() > 5 and \
       validade.isdigit() > 8:

        print("Cadastro concluido!")
        break

    else:
        print("Erro: Verifique se está tudo correto")

    print("-" * 30)