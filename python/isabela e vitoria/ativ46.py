print("---- REGISTRO DE SOFTWARE EM BLOCKCHAIN ----")

for tentativa in range(3):

    app = input("App: ").strip()
    dev = input("Dev: ").strip()
    email = input("E-mail: ").strip().lower()
    versao = input("Versão: ").strip()
    hashh = input("Hash: ").strip()
    token = input("Token: ").strip().upper()
    contrato = input("Contrato: ").strip()
    rede = input("Rede: ").strip().upper()
    bloco = input("Bloco: ").strip()
    minerador = input("Minerador: ").strip()
    taxa = input("Taxa: ").strip()
    chave = input("Chave: ").strip()
    wallet = input("Wallet: ").strip()
    servidor = input("Servidor: ").strip()
    protocolo = input("Protocolo: ").strip()

    if (app.isalpha() and
        dev.isalpha() and
        contrato.isdigit() and len(contrato) == 5 and
        bloco.isdigit() and
        rede == "ETHEREUM" and
        token != "LIXO" and
        len(hashh) == 10):

        print("Software registrado com sucesso.")
        break

    else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3.")

else:
    print("SISTEMA BLOQUEADO.")

