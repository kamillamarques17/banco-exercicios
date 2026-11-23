print("-----Auditoria Financeira e Custódia de Criptoativos-----")

auditor = input("Nome do Auditor: ").strip()
cargo = input("Cargo na Empresa: ").strip()
token = input("Símbolo do Token: ").strip()
hash = input("Código Hash do Bloco: ").strip()
chave = input("Chave Pública: ").strip()
gas = input("Taxa de Gas: ").strip()
quantidade = input("Quantidade Transferida: ").strip()
confirmacoes = input("Número de Confirmações: ").strip()
pais = input("País da Exchange: ").strip()
data = input("Data da Operação (DD/MM/AAAA): ").strip()
email = input("E-mail de Compliance: ").strip()
parecer = input("Parecer da Auditoria (CONCLUIDO): ").strip()

if auditor.isalpha() and \
cargo.isalpha() and \
pais.isalpha() and \
token.isalnum() and \
hash.isalnum() and \
chave.isalnum() and \
gas.isdigit() and \
quantidade.isdigit() and \
confirmacoes.isdigit() and \
len(chave) >= 12 and \
email.endswith(".exchange.io") and \
parecer == "CONCLUIDO":

    print("Auditoria concluída!")
else:
    print("Dados inválidos!")

print("-" * 30)
