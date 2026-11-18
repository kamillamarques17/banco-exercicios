print ("--------------------REGISTRO DE CRIPOATIVOS (BANCO DIGITAL) ---------------------")

nome = input("Digite o nome do clinte: ").strip()
criptomoeda = input("Digite o nome da criptomoeda: ").strip()
codigo = input("Digite o codigo Hash: ").strip()
data = input("Digite a data da transação: ").strip()
id = input("Digite o ID numerico do bloco: ").strip()
quantidade = input("Digite a quantidade de moeda: ").strip()
email = input("Digite o email: ").strip()
status = input("Digite o status: ").strip().upper

if nome.isalpha() and \
criptomoeda.isdigit() and \
codigo.isdigit() and \
id.isdigit() and \
quantidade.isdigit() and \
status == "APROVADO" and \
data.count("/") == 2 and \
email.count("@") == 1 and email.endswith(".com"):
    
        print(f"Acesso liberado! Bem-vindo ao sistema, {nome}.")

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")