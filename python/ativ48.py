print("---------Cadastro de agente da interpol----------")
for tentativa in range(3):
    agente = input("Informe o nome do agente:").strip()
    codinome = input("Qual o codinome: ").strip()
    pais = input("Digite o país: ").strip()
    ID = input("Qual o ID?: ").strip()
    nivel = input("Digite o nivel ").strip()
    cargo  = input("Digite o crago: ").strip() 
    especialidade = input("Qual a especialidade: ").strip()
    senha = input("Digite a senha: ").strip()
    pin = input("Qual o pin?: ").strip()
    unidade = input ("Qual a unidade?:")
    superior = input("Digite o superior: ").strip()
    missão = input("digite a missao: ").strip()
    arma = input("Informe a arma ").strip()
    veiculo = input("Qual o veiculo?: ").strip()
    status = input("informe o status:").strip()
     
    if agente.isalpha() and codinome.isalpha()  and pais() and \
    ID.isdigit() and nivel == "TOP_SECRET" and cargo() and\
    especialidade() and senha() and pin.isdigit() == 4 and unidade.upper() == "INTERPOL" and superior() and missão() and arma() and\
    veiculo() and status != "INATIVO":
            print("Cadatsro concluido!")
            break
    else: 
        print("Erro no cadastro")
        print("-"*30)
else:
    print("Tentaticvas bloqueadas")