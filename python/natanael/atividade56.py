print("------------Painel de Controle de um Foguete Espacial----------------")
missao = input("Nome da missão:").strip()
codigo = input("Código do foguete:").strip()
data = input("Data de lançamento (DD/MM/AAAA):").strip()
id = input("ID do astronauta:").strip()
email = input("E-mail da base:").strip()
combustivel = input("Quantidade de combustível (em litros):").strip()
carga = input("Peso da carga (em kg):").strip()
status = input("Digite 'APROVADO' para prosseguir:").strip().upper()
if codigo.isalnum() and carga.isalnum() and id.isdigit() and combustivel.isdigit() and\
    data.count("/") == 2 and len(data) == 10 and email.count("@") == 1 and email.endswith(".com") and\
    status == "APROVADO":
        print(f"Sucesso: O foguete para a missão {missao} foi aprovado para lançamento!")