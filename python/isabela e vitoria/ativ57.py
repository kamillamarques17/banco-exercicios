print("-----------registro de criptoativos(banco digital)------")

nome_cliente= input("nome do cliente: ").strip()
nome_criptomoeda = input("nome da criptomoeda: ").strip()
codigo_hash = input("codigo hash: ").strip()
data_transaçao= input("data de transição: ").strip()
ID= input("ID: ").strip()
email = input("email: ").strip()
quantidade_moedas= input("quantidade de moedas: ").strip()
status = input("confirmar autenticação:").strip()

if (nome_cliente.isalpha() and
    nome_criptomoeda.isalnum() and
    codigo_hash.isalnum() and
    data_transaçao.count("/") == 2 and
    ID.isdigit() and
    email.count("@") == 1 and
    email.endswith(".com") and
    quantidade_moedas.isdigit() and
    status == "APROVADO"):

    print("Tudo certo!")

else:
    print("Acesso bloqueado!")



