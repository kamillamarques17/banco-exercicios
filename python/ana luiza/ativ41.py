print("-------------Cadastro de tripulçaõ-------------")
for tentativa in range(3):
    usuário = input("Nome do usuario: ").strip()
    planeta = input("Qual o planeta?: ").strip()
    email = input("Qual o seu email?: ").strip().lower()
    cargo = input("Qual o seu cargo: ").strip().upper()
    Id = input("Digite o seu ID: ").strip()
    peso = input("Peso: ").strip().lower()
    codigo = input("Digite o seu cod: ").strip()
    nave = input("Digite o nome da nave: ")


    if usuário.isalpha() and planeta.isalpha() and cargo == "PILOTO" and Id.isdigit  and peso.isdigit and codigo == "MARTE2026" and nave != "TESTE":

        print(f"Acesso liberado! Bem-vindo ao sistema. {usuário}." )
        break
    else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3. ")
        print("-"* 30)
else:
    print("SISTEMA BLOQUEADO Alerta de intrusão enviado à segurança.") 