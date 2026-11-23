print("---------Prontuārio mdico de cirurgia robótica----------")
for tentativa in range(3):
    navio = input("Informe o navio:").strip()
    capitão = input("Qual o nome do capitão: ").strip()
    origem = input("Digite a origem: ").strip()
    destino= input("Qual o destino?: ").strip()
    carga = input("Digite a carga;: ").strip()
    peso = input("Digite o peso: ").strip() 
    container = input("Qual container: ").strip()
    valor = input("Digite o valor: ").strip()
    seguro = input("Qual o seguro?: ").strip()
    porto = input ("Qual o porto?:")
    empresa = input("Digite a empresa: ").strip()
    licença = input("Digite a licença: ").strip()
    rota = input("Informe a rota: ").strip()
    combustivel = input("Qual o combustivel: ").strip()
    chegada = input("Hora da chegada:").strip()
     
    if navio.isalpha() and capitão.isalpha()  and origem.isalpha() and \
    destino.upper() == "Europa" and peso.isdigit() and container.isdigit() > 3 and valor.isdigit() and chegada ():
        print("Cadatsro concluido!")
        break
    else: 
        print("Erro no cadastro")
        print("-"*30)
else:
    print("Tentaticvas bloqueadas")