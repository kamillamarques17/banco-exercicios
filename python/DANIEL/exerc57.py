print("------------------------registro de cripoativos (banco digital)-------------------------------")

nome = input("Digite o nome do cliente: ").strip()
criptomoeda = input("Digite o nome da criptomoeda: ").strip()
codigo = input("Digite o codigo hash: ").strip()
data = input("digite a data de transação: ").strip()
id = input("Digite o ID numerico do bloco : ").strip()
quantidade = input("digite a quantidade de moeda: ").strip()
email = input("digite o email: ").strip()
status = input("Digite o status: ").strip().upper()

if nome.isalpha() and \
   criptomoeda.isdigit() and \
   codigo.isdigit() and \
   id.isdigit() and \
   quantidade.isdigit() and \
   status == "APROVADO" and \
   data.count("/") == 2 and \
   email.count("@") == 1 and email.endswith(".com"):

    print(f"Acesso liberado! Bem-vindo ao sistema do {nome}.")

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")