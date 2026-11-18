print("-------------Registro de Criptoativos-------------")
nome = input("Nome do cliente:").strip()
criptomoeda = input("Nome da criptomoeda:").strip()
codigo = input("Código Hash da carteira:").strip()
data = input("Data da transação:").strip()
id = input("ID numérico do bloco:").strip()
email = input("E-mail de Suporte:").strip()
quantidade = input("Quantidade de criptomoedas:").strip().upper()
confirmar = input("Digite 'CONFIRMAR' para validar a transação:").strip()
if nome.isalpha() and criptomoeda.isalnum() and codigo.isalnum() and id.isdigit() and\
    quantidade.isdigit() and data.count("/") == 2 and len(data) == 10 and email.count("@") == 1 and email.endswith(".com") and\
    confirmar == "CONFIRMAR":
        print(f"Sucesso: A transação de {nome} foi realizada com êxito!")        
        
        print('-'*60)