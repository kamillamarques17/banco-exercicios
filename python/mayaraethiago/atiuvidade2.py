print("-----Plataforma de Comércio Exterior e Importação Aduaneira-----")

for Tentativa in range(5):
    nome = input("Nome do Importador: ").strip()
    razao = input("Razão Social: ").strip()
    origem = input("Porto de Origem: ").strip()
    destino = input("Porto de Destino: ").strip()
    container = input("Código do Container: ").strip()
    declaracao = input("Número da Declaração: ").strip()
    quantidade = input("Quantidade de Itens: ").strip()
    peso = input("Peso Bruto: ").strip()
    tarifario = input("Código Tarifário: ").strip()
    data = input("Data de Despacho (DD/MM/AAAA): ").strip()
    email = input("E-mail da Alfândega: ").strip().lower()
    parecer = input("Parecer Fiscal: ").strip().upper()

    if nome.isalpha() and razao.isalpha() and origem.isalpha() and \
       destino.isalpha() and  container.isalnum() and declaracao.isdigit() and \
       quantidade.isdigit() and peso.isdigit() and tarifario.isalnum() and \
       len(data) == 10 and \
       email.endswith("gov.br") and \
       "@" in email and \
       parecer == "LIBERADO":

        print(
            f"\nSUCESSO: importador {nome}, "
            f"parecer {parecer} registrado."
        )
        break

    else:

        print(f"\nERRO: cadastro inválido, Tentativa {Tentativa + 1} de 5")
        print("-" * 40)

else:

    print("\nBLOQUEADO: Limite de 5 tentativas excedido.")
