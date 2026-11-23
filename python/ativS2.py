print ("----BANCO DIGITAL----")

for tentativa in range(5):
    nome_cliente = input("Nome do cliente: ").strip()
    nome_criptomoeda = input("nome da criptomoeda: ").strip().upper()
    cod_carteira = input("digite o codigo: ").strip()
    data_transação = input("digite a dta de transação (DD/MM/AAAA): ").strip()
    id = input("digite o id: ").strip().lower()
    email = input("digite o email: ").strip()
    codigo_taxa= input("digite o codigo da taxa: ").strip()
    pais = input("digite o pais da corretora: ").strip()
    quantidade = input("quantidade de moedas:").strip()
    confirmação = input("status: ").strip().upper()

    if nome_cliente.isalnum() and\
    cod_carteira.isalnum() and\
    id.isdigit() and\
    nome_criptomoeda.isalnum() and\
    codigo_taxa.isalnum() and\
    quantidade.isdigit() and\
    pais.isalpha() and\
    email.count("@") == 1 and\
    email.endswith(".crypto.com") and\
    len(data_transação) == 10 and \
    confirmação == "APROVADO":

     print(f"\nSUCESSO: Banco {nome_cliente}, codigo {cod_carteira} liberado!") 
     break
    else:
       print(f"\nERRO: Dados invalidos!! {tentativa + 1} de 5")
       print("n\BLOQUEADO: Limite de 5 tentativas excedido!")
   