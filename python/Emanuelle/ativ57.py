print("------------------REGISTRO DE CRIPTOATIVOS----------------------")
for tentativa in range(3):
    nome_cliente = input("Digite o nome do cliente:")
    nome_cript = input("Digite o nome da criptomoeda:")
    codigo_hash = input("Informe o código:")
    Data_trans = input("Informe a data da transação DD/MM/AAAA:")
    ID_numero = input("Informe o número:")
    Email = input ("Digite o e-mail de suporte:")
    quantidade_moedas = input("Informe a quantidade de moedas:")
    confirmar = input("Confime a autenticação:")

    if nome_cript.isalnum() and codigo_hash.isalnum() and \
    ID_numero.isdigit() and quantidade_moedas.isdigit() and \
    Data_trans.count("/") == 2 and Email.count("@") and Email.endswith(".com") and \
    confirmar == "APROVADO":
        
        print("Registrado com sucesso!")
        break
    else:
        print("Erro ao cadastrar!")
        print("-" * 40)
else:
 print("Bloqueio muitas tentativas ")





  

    