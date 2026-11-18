print("----------------Registro de Software em blockchain---------------")
for tentativa in range(3):
    App = input("Informe o aplicativo: ").strip()
    Dev = input("Qual o dev ").strip()
    email = input("Digite o e-mail: ").strip()
    versão = input("Qual a versão? ").strip()
    hash = input("Digite o hash: (10 caracteres) ").strip()
    token = input("Digite o token: ").strip()
    Contrato = input("Qual o contrato? (5 digitos) ").strip()
    rede = input("Digite a rede: ").strip()
    bloco = input("Qual o bloco: ").strip()
    minerador = input("Qual o minerador? ").strip()
    taxa = input("Digite a taxa: ").strip()
    chave = input("Digite a chave: ").strip()
    wallet = input("Informe o wallet: ").strip()
    servidor = input("Qual o servidor? ").strip()
    protocolo = input("informe o protocolo:")

    if App.isalpha() and Dev.isalpha() and Contrato.isdigit() and \
    bloco.isdigit() and rede.upper() == "ETHEREUM"  and token != "LIXO" and \
    hash == 10 and email() and versão() and minerador() and taxa.isdigit() and chave() and wallet() and \
    servidor.isalpha() and protocolo.isdigit():

        
         print("Registro concluido!")
         break
    else:
       print("Erro no cadastro.")

