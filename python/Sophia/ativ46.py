print("----------------Manifesto de Carga de Navio Cargueiro----------------")
for tentativa in range(3):
    Navio = input("Informe o navio: ").strip()
    Capitão = input("Qual o nome do capitão: ").strip()
    Origem = input("Digite a origem: ").strip()
    Destino = input("Qual o destino: ").strip()
    Carga = input("Digite a carga: ").strip()
    Peso = input("Digite o peso: ").strip()
    Containers = input("Qual o containers: ").strip()
    Valor = input("Digite o valor: ").strip()
    Seguro = input("Qual o seguro: ").strip()
    Porto = input("Qual o porto? ").strip()
    Empresa = input("Digite a empresa: ").strip()
    Licença = input("Digite a licença: ").strip()
    Rota = input("Informe a rota: ").strip()
    Combustível = input("Qual o combustível? ").strip()
    Chegada = input("")

    if Navio.isalpha() and Capitão.isalpha() and Origem.isalpha() and \
    Destino.upper() == "Europa"  and Peso.isdigit() and Containers.isdigit() > 3 and Valor.isdigit() and \
    Seguro.isdigit() and Porto() and Empresa !="FANTASMA" and Licença.isdigit() and Rota == "SUL" and Combustível() and Chegada ():
        
         print("Cadastro concluido!")
         break
    else:
       print("Erro no cadastro.")

       
       print("-" * 30) 
else:
      print("Tentativas bloqueadas")


