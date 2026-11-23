print("-----Terminal Portuário e Controle de Atracação Marítima-----")

pratico = input("Nome do Prático: ").strip()
pais = input("País da Embarcação: ").strip()
navio = input("Nome do Navio: ").strip()
imo = input("Código IMO: ").strip()
calado = input("Calado do Navio: ").strip()
berco = input("Número do Berço: ").strip()
tonelagem = input("Tonelagem de Carga: ").strip()
rebocador = input("Código do Rebocador: ").strip()
canal = input("Canal de Atracação: ").strip()
data = input("Data da Atracação (DD/MM/AAAA): ").strip()
email = input("E-mail da Capitania: ").strip()
autorizacao = input("Autorização Portuária (CONFIRMADO): ").strip()

if pratico.isalpha() and \
pais.isalpha() and \
navio.isalpha() and \
imo.isalnum() and \
rebocador.isalnum() and \
canal.isalnum() and \
calado.isdigit() and \
berco.isdigit() and \
tonelagem.isdigit() and \
len(imo) == 7 and \
email.endswith(".marinha.mil.br") and \
autorizacao == "CONFIRMADO":

    print("Atracação confirmada!")
else:
    print("Dados inválidos!")

print("-" * 30)