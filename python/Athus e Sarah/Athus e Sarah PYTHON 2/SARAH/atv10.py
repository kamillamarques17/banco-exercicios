print("-----Sistema de Expedição de Pedidos-----")

comprador = input("Nome do Comprador: ").strip()
sobrenome = input("Sobrenome: ").strip()
cidade = input("Cidade de Entrega: ").strip()
estado = input("Estado: ").strip()
rastreamento = input("Código de Rastreamento: ").strip()
sku = input("Código SKU: ").strip()
quantidade = input("Quantidade de Produtos: ").strip()
valor = input("Valor da Compra: ").strip()
data = input("Data da Expedição (DD/MM/AAAA): ").strip()
email = input("E-mail do Comprador: ").strip()
cartao = input("Código de Validação do Cartão: ").strip()
status = input("Status (DESPACHADO): ").strip()

if comprador.isalpha() and \
sobrenome.isalpha() and \
cidade.isalpha() and \
estado.isalpha() and estado == estado.upper() and \
rastreamento.startswith("LOG-") and rastreamento[4:].isalnum() and \
sku.isalnum() and \
quantidade.isdigit() and \
valor.isdigit() and \
len(data) == 10 and data.count("/") == 2 and \
email.count("@") and email.endswith(".com.br") and \
cartao.isalnum() and \
status == "DESPACHADO":

    print("Pedido despachado!")
else:
    print("Dados inválidos!")

print("-" * 30)