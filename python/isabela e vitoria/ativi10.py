print("----- CONTROLE DE ACESSO AO CENTRO DE PESQUISA NUCLEAR -----")

for tentativa in range(5):
    nome = input("Nome do Pesquisador: ").strip()
    sobrenome = input("Sobrenome: ").strip()
    codigo_reator = input("Código do Reator: ").strip()
    setor_acesso = input("Setor de Acesso: ").strip()
    nivel_radiacao = input("Nível de Radiação: ").strip()
    data_inspecao = input("Data da Inspeção (DD/MM/AAAA): ").strip()
    cartao_acesso = input("Cartão de Acesso: ").strip()
    id_cracha = input("ID do Crachá: ").strip()
    temperatura = input("Temperatura do Núcleo: ").strip()
    cidade = input("Cidade do Laboratório: ").strip()
    email = input("E-mail Institucional: ").strip().lower()
    status = input("Status de Segurança (APROVADO): ").strip().upper()

    if nome.isalpha() and \
       sobrenome.isalpha() and \
       setor_acesso.isalpha() and \
       cidade.isalpha() and \
       codigo_reator.isalnum() and \
       cartao_acesso.isalnum() and \
       nivel_radiacao.isdigit() and \
       id_cracha.isdigit() and \
       temperatura.isdigit() and \
       "@" in email and \
       email.endswith(".gov.br") and \
       data_inspecao.count("/") == 2 and \
       status == "APROVADO":

        print("\nSUCESSO: Acesso Liberado ao Centro de Pesquisa Nuclear!")
        break
    else:
        print(f"\nERRO: Dados inválidos! Tentativa {tentativa + 1} de 5")
        print("-" * 40)

else:
    print("\nBLOQUEADO: Limite de 5 tentativas excedido. Procure a segurança do centro.")
