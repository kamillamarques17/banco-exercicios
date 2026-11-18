print("---------Painel de controle de um foguete espacial---------")

nome_missao = input("qual o nome da missão? ").strip()
codigo_foguete = input("qual o código do foguete? ").strip()
data_lanc = input("qual a data de lançamento? ").strip()
iddigital_astronauta = input ("qual o ID digital do astronauta? ").strip()
email_base = input("qual o email da base? ").strip()
combustível = input("QTDE. de combustível: ").strip()
carga_espacial = input("possui carga especial? ").strip()
status_sistema = input("status do sistema: ").strip()

if codigo_foguete.isalnum() and carga_espacial.isalnum() and \
iddigital_astronauta.isdigit() and combustível.isdigit() and \
email_base.count("@") and email_base.endswith(".com") and data_lanc.count("/") == 2 and \
status_sistema == "APROVADO":
    print("Registrado com sucesso!")

print("-" * 40)
