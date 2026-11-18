print("------CADASTRO DE TRIBULAÇÃO ESPACIAL------")
for tentativa in range(3):
    nome = input("Digite seu nome: ").strip()
    planeta = input("Digite o planeta: ").strip()
    email = input("Digite o email: ").strip()
    cargo = input("Informe o cargo: ").strip()
    id = input("Digite o id: ").strip()
    peso = input("Digite o seu peso: ").strip()
    código = input("Digite o código de missão: ")
    nave = input("Informe a nave: ") 

    if nome.isalpha() and planeta.isalpha() and \
       email.lower() and cargo.upper() == "PILOTO" and \
       id.isdigit() and peso.isdigit() and \
       len(código) == "MARTE2026" and nave !="TESTE":
       
       print("Cadastro concluido.")
       break 
    else: 
        print(f"Erro nos dados!")
        
        print("-" * 30)
else: 
    print("SISTEMA BLOQUEADO.")