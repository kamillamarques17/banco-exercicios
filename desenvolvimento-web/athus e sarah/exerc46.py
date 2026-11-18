print('-----Manifesto de Carga de Navio Cargueiro-----')
for tentativa in range(3):
    navio = input("informe o navio:").strip()
    capitão = input("Qual o nome do capitão?:").strip()
    origem = input("Digite a origem:").strip()
    Destino = input("Qual o destino?:").strip()
    carga = ("Digite a carga:").strip()
    peso = input("Digite o peso:").strip()
    containers = input("Qual o container?:").strip()
    valor= input("Digite o valor:").strip()
    seguro = input("Qual o seguro?:").strip()
    porto = input("Qual o porto?:").strip()
    empresa = input("digite a empresa?:").strip()
    licença = input("digite a licença:").strip()
    rota = input("informe a rota:").strip()
    combustível = input("Qual o combustível?:").strip()
    chegada = input("")

    if navio.isalpha() and capitão.isalpha() and origem.isalpha() and \
    Destino.upper() =="Europa" and peso.isdigit() and containers.isdigit() > 3 and valor.isdigit() and \
    seguro.isdigit() and porto() and empresa !="FANTASMA" and licença.isdigit() and rota == "SUL" and combustível() and chegada ():
        
        print("cadastro concluido!")
        break
    print("erro no cadastro")


    print("-" * 40)
else:
    print("tentativas bloqueadas")
