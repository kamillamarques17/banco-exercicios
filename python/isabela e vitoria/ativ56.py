print("-----------painel e controle e um foguete espacial------")

nome_missao = input("nome da missão: ").strip()
codigo_do_foguete = input("qual o codigo do foguete: ").strip()
data = input("qual a data de lançamento: ").strip()
ID = input("ID: ").strip()
email= input("email: ").strip()
combustivel = input("combustivel: ").strip()
carga_espacial= input("carga espacial: ").strip()
status = input("Status: ").strip()

if (nome_missao.isalpha() and
    codigo_do_foguete.isalnum() and
    data.count("/") == 2 and
    ID.isdigit() and
    email.count("@") == 1 and
    email.endswith(".com") and
    combustivel.isdigit() and
    carga_espacial.isalnum() and
    status == "APROVADO"):

    print("Tudo certo")

else:
    print("Acesso bloqueado!")



