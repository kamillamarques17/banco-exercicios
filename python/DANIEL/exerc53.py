print("---sistema de auditoria completo ---")

for tentativa in range(3):
    projeto = input("digite o nome do seu projeto")
    codigo = input("digite seu codigo de acesso")
    engenheiro = input("digite o seu nivel de engenharia")
    crea = input("digite seu crea")
    orçamento = input("digite seu orçamento")
    data_inicial = input("digite sua data DD/MM/AAAA:")
    data_fim = input("digite sua data fim DD/MM/AAAA:")
    cidade = input("digite o seu cliente ")
    uf = input("digite sua uf:")
    email_resp = input("digite seu email de email_resp:")
    cliente = input("digite o seu cliente:")
    CNPJ = input("digite seu cnpj:")
    prioridade = input("digite sua prioridade")
    status = input("digite seu status ")

    if projeto.isalnum() and \
       uf.isalnum() and \
       status.isalnum() and \
       codigo.isalnum() and \
       engenheiro.isalpha() and \
       cidade.isalpha() and \
       crea.isdigit() and \
       orçamento.isdigit() and \
       CNPJ.isdigit() and \
       email_resp.count("@") == 1 and \
       email_resp.endswith(".com") and \
       data_inicial.count("/") == 2 and \
       status == "aprovado":

        print(f"\nSUCESSO status {status}, seu relatorio {projeto} foi enviado!")
        break

    else:
        print(f"\nERRO: dados invalidos! tentativa {tentativa + 1} de 3.")
        print("-" * 40)
else:
    print("\nbloqueado: muitas falhas. procure o diretor de segurança.")