print ("------------------------SISTEMA DE UM FOGUETE-------------------------------")

nome = input("Digite o nome da missão: ").strip()
codigo = input("Digite o codigo do foguete: ").strip()
data = input("Digite a data de lançamento: ").strip()
id = input("Digite o ID do piloto: ").strip()
email = input("digite o email da base: ").strip()
combustivel = input ("Digite o nome do combustivel: ").strip()
carga = input ("Digite a carga: ").strip()
status = input("Digite o status:").strip().upper()

if nome.isalpha() and \
codigo.isalnum() and \
id.isdigit() and \
combustivel.isdigit() and \
carga.isalnum() and \
status == "APROVADO" and \
data.count("/") == 2 and \
email.count("@") == 1 and email.endswith(".com"):
                   
           print(f"Acesso liberado! Bem-vindo ao sistema do {nome}.")

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")