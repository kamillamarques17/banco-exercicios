print("---------------------PROJETO DE ENGENHARIA-----------------------")

for tentativa in range(1):

    projeto = input("Digite o nome do projeto :").strip()
    codigo = input("Digite o codigo:").strip()
    crea = input("Digite o crea:").strip()
    engenheiro = input("Digite o nome do engenheiro:").strip()
    setor = input("Digite o setor:").strip()
    orçamento = input("Digite o orçamento :").strip()
    data = input("Digite a data de inicio :").strip()
    dataf = input("Digite a data de fim :").strip()
    cnpj = input("Digite o cnpj :").strip()
    cidade = input("Digite a cidade :").strip()
    uf = input("Digite o UF :").strip()
    email = input("Digite o seu email:")
    propriedade = input("Digite a propriedade :").strip()
    codigo = input("Digite o codigo :").strip()
    status = input("Digite o status:").strip().upper()

    if projeto.isalnum() and projeto.isalnum() and \
    codigo.isalnum() and \
    crea.isdigit() and \
    engenheiro.isalpha() and \
    setor.isalnum() and \
    orçamento.isdigit() and \
    cnpj.isdigit() and len(cnpj) == 14 and \
    cidade.isalpha() and \
    uf.isalnum() and len(uf) == 2 and \
    propriedade.isalnum() and \
    codigo.isalnum() and \
    status == "APROVADO" and \
    data.count("/") == 2 and dataf.count("/") == 2 and \
    email.count("@") == 1 and email.endswith(".com"):
               
           print(f"Acesso liberado! Bem-vindo ao sistema do {projeto}.")
           break

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")