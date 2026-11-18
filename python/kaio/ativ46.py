print("---NAVIO CARGUEIRO---")

for tentativa in range(3):

    navio = input("Digite o navio:  ").strip()
    capitão = input("Digite o nome do capitão: ").strip()
    origem = input("Digite a origem da carga: ").strip()
    destino = input("Digite o destino: ").strip().upper()
    carga = input("Digite sua carga: ").strip()
    peso = input("Digite o peso: ").strip()
    conteiners = input("Digite o numero do conteiner : ").strip()
    valor = input("Digite o valor: ")
    seguro = input("Digite o numero do sguro : ").strip()
    porto = input("Digite o nome do porto").strip()
    empresa = input("Digite o nome da empresa").strip().upper
    licença = input("Digite sua licença: ").strip()
    rota = input("Digite a rota ").strip()
    combustivel = input("Digite o combustivel").strip()
    chegada = input("sua chegada").strip()

    if navio.isdigit() and navio.isalpha() and \
       capitão.isalpha() and \
       origem.isalpha() and \
       peso.isdigit() and \
       licença.isdigit and \
       combustivel.isalpha and \
       chegada.isdigit and \
       carga.isdigit and \
       peso.isdigit and \
       valor.isdigit and \
       seguro.isalpha() and seguro.isdigit() and \
       conteiners.isalpha() and conteiners.isdigit() and \
       len(empresa) and empresa.isalpha() != "FANTASMA" and \
       len(destino) and destino.isalpha() == "EUROPA" and \
       len(rota) and rota.isdigit() == "SUL":

        print(f"Acesso liberado! Bem-vindo ao sistema, {capitão}.")
        break

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")