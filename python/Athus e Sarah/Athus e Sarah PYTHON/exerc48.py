print("----------------Cadastro de Agente da Interpol---------------")
for tentativa in range(3):
    Agente = input("Informe o agente: ").strip()
    Codinome = input("Informe o codinome: ").strip()
    País = input("Informe o país: ").strip()
    Id = input("Qual o id? ").strip()
    Nível = input("Informe o nível: ").strip()
    Cargo = input("Digite o cargo: ").strip()
    Especialidade = input("Qual a especialidade: ").strip()
    Senha = input("Digite a senha: ").strip()
    Pin = input("Digite o pin: (4 números) ").strip()
    Unidade = input("Qual a unidade: ").strip()
    Superior = input("Informe o superior: ").strip()
    Missão = input("Informe a missão: ").strip()
    Arma = input("Digite a arma: ").strip()
    Veículo = input("Qual o veículo: ").strip()
    Status = input("informe o status: ").strip()

    if Agente.isalpha() and Codinome.isalpha() and País() and \
    Id.isdigit() and Nível == "TOP_SECRET" and Cargo() and \
    Especialidade() and Senha() and Pin.isdigit() ==4 and Unidade.upper() =="INTERPOL" and Superior() and Missão() and Arma() and \
    Veículo() and Status != "INATIVO":

        
         print("Cadastro concluido!")
         break
    else:
       print("Erro no cadastro.")
