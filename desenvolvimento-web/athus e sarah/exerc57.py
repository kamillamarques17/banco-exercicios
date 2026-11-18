print("---------Registro de Criptoativos (Banco Digital)---------")

nome_cliente = input("Nome do cliente: ").strip()
nome_cripto = input("Nome da criptomoeda: ").strip()
codigo_hash = input("Qual o código HASH da carteira? ").strip()
data_transacao = input ("Data da transação: ").strip()
id_bloco = input("ID númerico do bloco: ").strip()
email_suporte = input("E-mail do suporte: ").strip()
qtde_moedas = input("Quantidade de moedas: ").strip()
conf_autentic = input("Confirmar autenticação: ").strip()

if nome_cripto.isalnum() and codigo_hash.isalnum() and \
id_bloco.isdigit() and qtde_moedas.isdigit and \
email_suporte.count("@") and email_suporte.endswith(".com") and \
data_transacao.count("/") == 2 and conf_autentic == "APROVADO":
    print("Registrado com sucesso!")

print("-" * 40)