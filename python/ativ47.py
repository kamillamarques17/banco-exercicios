print("---------Registro de software----------")
for tentativa in range(3):
    app = input("Informe o aplicativo:").strip()
    dev = input("Qual o dev: ").strip()
    email = input("Digite o e-mail?: ").strip()
    versão = input("Qual a versão?: ").strip()
    hash = input("Digite a hash:(10 caracteres) ").strip()
    token = input("Digite o token: ").strip() 
    contrato = input("Qual contrato: (5 digitos) ").strip()
    rede = input("Digitea rede: ").strip()
    bloco = input("Qual o bloco?: ").strip()
    minerador = input ("Qual o minerador?:")
    taxa = input("Digite a taxa: ").strip()
    chave = input("digite a chave: ").strip()
    wallet = input("Informe o wallet: ").strip()
    servidor = input("Qual o servidr?: ").strip()
    protocolo = input("informe oprotocolo:").strip()
     
    if app.isalpha() and dev.isalpha()  and contrato.isdigit() and \
    bloco.isdigit() and rede.upper() == "ETHEREUM" and token != "LIXO" and\
    hash == 10 and email()  and versão() and minerador() and taxa.isdigit() and chave() and wallet() and \
    servidor.isalpha() and protocolo.isdigit():
        print("Cadatsro concluido!")
        break
    else: 
        print("Erro no cadastro")
        print("-"*30)
else:
    print("Tentaticvas bloqueadas")