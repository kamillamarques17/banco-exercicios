print ("----servidor de dados----")

for tentativa in range(5):
    nome= input("Nome do cliente: ").strip()
    cargo = input("cargo ").strip().upper()
    codigo_ser= input("digite o codigo do servidor: ").strip()
    ip = input(" digite o ip: ").strip()
    porta_rede = input("digite a porta de rede : ").strip().lower()
    setor = input("digite o setor: ").strip()
    protocolo = input("digite o protocolo: ").strip()
    senha = input("digite a senha: ").strip()
    dominio = input("qual dominio?:").strip()
    confirmação = input("status: ").strip().upper()

    if nome.isalnum() and\
    codigo_ser.isalnum() and\
    ip.isdigit() and\
    porta_rede.isdigit() and\
    setor.isalpha() and\
    protocolo.isalnum() and\
    dominio.endswith(".org") == 1 and \
    len(senha)== 8 and\
    confirmação == "APROVADO":
        print(f"\nSUCESSO: Nome {ip}, protocolo {protocolo} liberado!!")
        break
    else:
        print(f"\nERRO:Daos Inválido! {tentativa + 1} de 5")
else:
    print("\nBLOQUEADO:Limite e 5 tentativas excedido.  ")

     